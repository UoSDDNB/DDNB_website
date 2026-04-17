import os
import json
import urllib.request
import re

# ==========================================
# Configuration
# ==========================================
# Replace with actual ORCID IDs you want to query
ORCID_IDS = [
    "0009-0006-0867-1441", # Juri Westendorf
    "0009-0002-9226-1816", # Luke Green
    "0000-0002-4390-0872", # Owen Rackham
    "0000-0003-0164-7773", # Ahmed Dawoud
    "0000-0002-5609-868X", # Moi Nicholas
    "0009-0002-7999-859X", # Charlotte Ellison
    "0000-0002-7266-854X", # Disha Mehta
]

### temporary hack for interactive work
# Try to use __file__, but if running interactively, fall back to current directory
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    script_dir = os.path.abspath(os.getcwd())

# If the script is being run from the 'scripts' folder, go up one level to find the root.
# If it's already running from the project root, just use the current dir.
if os.path.basename(script_dir) == "scripts":
    PROJECT_ROOT = os.path.abspath(os.path.join(script_dir, ".."))
else:
    PROJECT_ROOT = script_dir

# Automatically finds the src/content/publications directory relative to this script
#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "src", "content", "publications")
# ==========================================

def fetch_json(url, headers=None):
    if headers is None:
        headers = {}
    headers["Accept"] = "application/json"
    
    req = urllib.request.Request(url, headers=headers)
    # Required to avoid being blocked by Crossref APIs
    req.add_header("User-Agent", "DDNBScript/1.0 (mailto:ddnetbio@soton.ac.uk)")
    
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def fetch_dois_from_orcid(orcid):
    print(f"Fetching works for ORCID: {orcid}...")
    url = f"https://pub.orcid.org/v3.0/{orcid}/works"
    data = fetch_json(url)
    
    if not data: return []
    
    dois = []
    # Parse the deeply nested ORCID JSON response for DOIs
    for group in data.get("group", []):
        for work in group.get("work-summary", []):
            for ext_id in work.get("external-ids", {}).get("external-id", []):
                if ext_id.get("external-id-type") == "doi":
                    dois.append(ext_id.get("external-id-value"))
                    break # Just need the first DOI for each work
                    
    unique_dois = list(set(dois))
    print(f"Found {len(unique_dois)} unique DOIs.")
    return unique_dois

def fetch_crossref_metadata(doi):
    url = f"https://api.crossref.org/works/{doi}"
    data = fetch_json(url)
    if not data or "message" not in data: return None
    
    msg = data["message"]
    
    # Format authors
    authors = []
    
    # regex maps to handle middle names and varied formatting
    TEAM_MEMBER_REGEX = {
        r"\bA[a-z]*\.?\s*[\w\.\s-]*?Dawoud\b": "Ahmed Dawoud",
        r"\bC[a-z]*\.?\s*[\w\.\s-]*?Ellison\b": "Charlotte Ellison",
        r"\bD[a-z]*\.?\s*[\w\.\s-]*?Mehta\b": "Disha Mehta",
        r"\bJ[a-z]*\.?\s*[\w\.\s-]*?Westendorf\b": "Juri Westendorf",
        r"\bL[a-z]*\.?\s*[\w\.\s-]*?Green\b": "Luke Green",
        r"\bM[a-z]*\.?\s*[\w\.\s-]*?Nicholas\b": "Moi Taiga Nicholas",
        r"\b(?:O[a-z]*\.?\s*[\w\.\s-]*?)?Rackham\b": "Owen Rackham"
    }

    for author in msg.get("author", []):
        # Handle consortium/group authors which don't have 'given'/'family' names
        if "name" in author:
            name = author["name"].strip()
        else:
            name = f"{author.get('given', '')} {author.get('family', '')}".strip()
            
        if name:
            for pattern, standard_name in TEAM_MEMBER_REGEX.items():
                if re.search(pattern, name, re.IGNORECASE):
                    name = standard_name
                    break
            authors.append(name)
        
    # Find year published
    year = "2024"
    published = msg.get("published-print") or msg.get("published-online") or msg.get("created")
    if published and "date-parts" in published:
        year = str(published["date-parts"][0][0])
        
    # Safely get title 
    title_list = msg.get("title", [])
    title = title_list[0].replace('"', "'").strip() if title_list else "Unknown Title"
    
    # Safely get journal / container-title
    journal_list = msg.get("container-title", [])
    journal = journal_list[0].replace('"', "'") if journal_list else "Preprint"

    # Add Owen Rackham if FANTOM consortium is an author
    is_fantom = any(re.search(r'fantom', a, re.IGNORECASE) for a in authors)
    if is_fantom and "Owen Rackham" not in authors:
        authors.append("Owen Rackham")
        
    # Extra deduplication step just in case
    authors = list(dict.fromkeys(authors))

    return {
        "doi": doi,
        "title": title,
        "authors": authors,
        "year": year,
        "journal": journal,
        "url": msg.get("URL", f"https://doi.org/{doi}"),
        "abstract": msg.get("abstract", "") # Note: Crossref rarely has full abstracts
    }

def main():
    if not ORCID_IDS or ORCID_IDS[0] == "0000-0000-0000-0000":
        print("❌ Wait! Please edit this script to add actual ORCID_IDs at the top.")
        return {}

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Collect all DOIs across all provided ORCIDs
    all_dois = []
    orcid_to_dois = {}
    for orcid in ORCID_IDS:
        dois = fetch_dois_from_orcid(orcid)
        orcid_to_dois[orcid] = dois
        all_dois.extend(dois)
        
    # Remove duplicates in case multiple team members are on the same paper
    unique_dois = list(set(all_dois))
    print(f"\nFound {len(unique_dois)} unique DOIs across all team members.\n")
    
    for doi in unique_dois:
        print(f"Processing DOI: {doi}")
        meta = fetch_crossref_metadata(doi)
        if not meta: continue
        
        # NEW: Skip if no authors were found
        if not meta["authors"]:
            print(f"  ⏭ Skipped: No authors found for this DOI.")
            continue
        
        # Create a safe file name (e.g., "10_1038_s41467.md")
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', meta["doi"])
        filepath = os.path.join(OUTPUT_DIR, f"{safe_name}.md")
        
        # If we already fetched this one, skip it to avoid overwriting your manual edits!
        if os.path.exists(filepath):
            print(f"  ⏭ Skipped: file already exists.")
            continue

        authors_yaml = "\n".join([f'  - "{a}"' for a in meta["authors"]])
        abstract_clean = re.sub(r'<[^>]+>', '', meta["abstract"]).replace('\n', ' ').strip()
        
        # The markdown template mirroring ppr.md format
        md_content = f"""---
title: "{meta['title']}"
authors:
{authors_yaml}
year: {meta['year']}
journal: "{meta['journal']}"
doi: "{meta['doi']}"
url: "{meta['url']}"
openAccessPdf: ""
featured: false
theme: ["network-biology"]
socialTags: []
abstract: "{abstract_clean}"
---

More details regarding '{meta['title']}' can be added here.
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)
        
        print(f"  ✅ Created: {safe_name}.md")

    return orcid_to_dois



# Run through all of the .md files in the publications folder
# and tidy all the author names retroactively
def tidy_existing_md_files():
    print("\n--- Tidying up author names in existing .md files ---")
    TEAM_MEMBER_REGEX = {
        r"\bA[a-z]*\.?\s*[\w\.\s-]*?Dawoud\b": "Ahmed Dawoud",
        r"\bC[a-z]*\.?\s*[\w\.\s-]*?Ellison\b": "Charlotte Ellison",
        r"\bD[a-z]*\.?\s*[\w\.\s-]*?Mehta\b": "Disha Mehta",
        r"\bJ[a-z]*\.?\s*[\w\.\s-]*?Westendorf\b": "Juri Westendorf",
        r"\bL[a-z]*\.?\s*[\w\.\s-]*?Green\b": "Luke Green",
        r"\bM[a-z]*\.?\s*[\w\.\s-]*?Nicholas\b": "Moi Taiga Nicholas",
        r"\b(?:O[a-z]*\.?\s*[\w\.\s-]*?)?Rackham\b": "Owen Rackham"
    }
    
    if not os.path.exists(OUTPUT_DIR): return

    for filename in os.listdir(OUTPUT_DIR):
        if not filename.endswith(".md"): continue
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content
        for pattern, standard_name in TEAM_MEMBER_REGEX.items():
            new_content = re.sub(pattern, standard_name, new_content, flags=re.IGNORECASE)
            
        # Add Owen Rackham if "Fantom" is in the text
        if re.search(r'fantom', new_content, re.IGNORECASE):
            match = re.search(r'(authors:\s*\n.*?)\nyear:', new_content, re.DOTALL)
            if match:
                authors_block = match.group(1)
                if "Owen Rackham" not in authors_block:
                    new_authors_block = authors_block + '  - "Owen Rackham"\n'
                    new_content = new_content.replace(authors_block, new_authors_block)
                    
        # Remove duplicated Owen Rackham entries in the author block
        match = re.search(r'(authors:\s*\n.*?)\nyear:', new_content, re.DOTALL)
        if match:
            authors_section = match.group(1)
            lines = authors_section.split("\n")
            new_lines = []
            seen_owen = False
            for line in lines:
                if "Owen Rackham" in line:
                    if seen_owen:
                        continue # Skip duplicates
                    seen_owen = True
                new_lines.append(line)
            new_authors_section = "\n".join(new_lines)
            new_content = new_content.replace(authors_section, new_authors_section)
            
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  ✨ Updated names in: {filename}")


def audit_author_names(orcid_to_dois):
    print("\n==========================================")
    print("📊 AUTHOR DATA AUDIT REPORT")
    print("==========================================")
    
    # Map ORCIDs to Standard names so we can print the number of works fetched from ORCID
    ORCID_MAP = {
        "0009-0006-0867-1441": "Juri Westendorf",
        "0009-0002-9226-1816": "Luke Green",
        "0000-0002-4390-0872": "Owen Rackham",
        "0000-0003-0164-7773": "Ahmed Dawoud",
        "0000-0002-5609-868X": "Moi Taiga Nicholas",
        "0009-0002-7999-859X": "Charlotte Ellison",
        "0000-0002-7266-854X": "Disha Mehta",
    }
    
    STANDARD_NAMES = [
        "Ahmed Dawoud",
        "Charlotte Ellison",
        "Disha Mehta",
        "Juri Westendorf",
        "Luke Green",
        "Moi Taiga Nicholas",
        "Owen Rackham"
    ]
    
    md_name_counts = {name: 0 for name in STANDARD_NAMES}
    
    # Count occurrences of standard names in the 'authors' block of the markdown files
    if os.path.exists(OUTPUT_DIR):
        for filename in os.listdir(OUTPUT_DIR):
            if not filename.endswith(".md"): continue
            with open(os.path.join(OUTPUT_DIR, filename), "r", encoding="utf-8") as f:
                content = f.read()
                # Use regex to isolate the authors block only 
                match = re.search(r'authors:\s*\n(.*?)\nyear:', content, re.DOTALL)
                if match:
                    authors_block = match.group(1)
                    for name in STANDARD_NAMES:
                        # Check strictly if their name is in the authors YAML list
                        if name in authors_block:
                            md_name_counts[name] += 1
                            
    print(f"{'Team Member'.ljust(22)} | {'ORCID DOIs'.ljust(12)} | {'MD File Appearances'}")
    print("-" * 60)
    
    for name in STANDARD_NAMES:
        # Find matching ORCID count if they have one
        orcid_count = 0
        for o_id, o_name in ORCID_MAP.items():
            if o_name == name:
                orcid_count = len(orcid_to_dois.get(o_id, []))
        
        print(f"{name.ljust(22)} | {str(orcid_count).ljust(12)} | {md_name_counts[name]}")
    print("==========================================\n")


if __name__ == "__main__":
    orcid_map_data = main()
    tidy_existing_md_files()
    if orcid_map_data is not None:
        audit_author_names(orcid_map_data)

