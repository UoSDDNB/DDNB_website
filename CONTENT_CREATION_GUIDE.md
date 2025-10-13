# DDNB Website Content Creation Guide

This guide provides everything you need to create content for the Data-Driven Network Biology Group website. All content is managed through markdown files in the `src/content/` directory.

## 📁 Directory Structure

```
src/content/
├── themes/          # Research themes (one MD per theme)
├── tools/           # Tools & datasets (one MD per item)
├── hacks/           # Research hackathons (one MD per hack)
├── publications/    # Publications (one MD per paper)
└── team/            # Team members (one MD per member)
```

---

## 🧬 Research Themes (`src/content/themes/`)

**Purpose**: Showcase your main research areas and focus areas.

### Required Files
- Replace `single-cell-biology.md` with your actual single-cell research theme
- Replace `network-biology.md` with your actual network biology theme
- Add additional themes as needed

### Template for Each Theme

```markdown
---
title: "Your Research Theme Title"
image: "/hero/your-theme-image.jpg"
description: "Brief description (≤200 words) of your research theme and its significance."
order: 1
---

Your detailed description of the research theme goes here. This can be longer and more detailed than the front-matter description.
```

### Required Fields
- **title**: Theme name
- **image**: Hero image path (`/hero/theme-name.jpg`)
- **description**: Brief description (≤200 words)
- **order**: Display order (1, 2, 3, etc.)

### Example Themes to Create
- Single-cell biology
- Network biology
- Machine learning in biology
- Systems biology
- Translational genomics
- Computational drug discovery

---

## 🛠️ Tools & Datasets (`src/content/tools/`)

**Purpose**: Showcase your software tools, datasets, and resources.

### Required Files
- Replace `shinysell.md` with your actual ShinyCell tool
- Add your other tools and datasets

### Template for Each Tool

```markdown
---
title: "Your Tool Name"
type: "tool" # or "dataset" | "resource"
description: "Brief description (≤200 words) of what the tool does."
image: "/assets/tools/your-tool.png"
imageAlt: "Descriptive alt text for the image"
urls:
  github: "https://github.com/your-org/your-tool"
  paper: "https://doi.org/10.xxxx/xxxxx"
  website: "https://your-tool.com"
  viewer: "https://your-tool.com/viewer" # Optional: for ShinyCell-style viewers
authors:
  - name: "Your Name"
    role: "Maintainer"
    orcid: "0000-0000-0000-0000"
tags: ["single-cell", "RNA-seq", "R", "Shiny", "Python", "webapp"]
version: "v1.0.0"
releaseDate: "2024-01-15"
status: "active" # or "maintenance" | "archived"
license: "MIT"
citation: "Your Name et al. Your Tool: A brief description. Journal Name (2024)."
doi: "10.xxxx/xxxxx"
funding: ["MRC MR/xxxx", "Wellcome 2xxxxx"]
requirements: "R 4.0+, Shiny"
dataAccess: "open" # or "controlled" | "upon request"
contact: "your.email@soton.ac.uk"
---

Detailed description of your tool, including usage examples and documentation links.
```

### Required Fields
- **title**: Tool/dataset name
- **type**: "tool", "dataset", or "resource"
- **description**: Brief description (≤200 words)
- **image**: Screenshot path (`/assets/tools/tool-name.png`)
- **imageAlt**: Alt text for accessibility
- **urls**: GitHub, paper, website, viewer URLs
- **authors**: List of authors with roles
- **tags**: Relevant tags for filtering
- **contact**: Contact email

### Example Tools to Create
- ShinyCell (single-cell visualization)
- Your analysis pipeline
- Your dataset
- Your web application
- Your R/Python package

---

## 🏃‍♂️ Research Hacks (`src/content/hacks/`)

**Purpose**: Document your research hackathons and intensive collaboration sessions.

### Required Files
- Replace `covid19-single-cell.md` with your actual COVID-19 hack
- Add other hackathons

### Template for Each Hack

```markdown
---
title: "Your Hack Title"
date: "2024-07-15"
image: "/assets/hacks/your-hack.jpg"
summary: |
  Brief summary (≤200 words) covering:
  - Main aim
  - Main achievement
links:
  github: "https://github.com/your-org/your-hack"
  datasets: ["https://dataset1.com", "https://dataset2.com"]
objectives:
  - "Objective 1: What you aimed to achieve"
  - "Objective 2: Another goal"
accomplishments:
  - "We built X and validated Y"
  - "We discovered Z"
importance: "Why this hack mattered and its impact on the field."
---

Detailed background and methodology for your hack.
```

### Required Fields
- **title**: Hack name
- **date**: Date in YYYY-MM-DD format
- **image**: Hack photo (`/assets/hacks/hack-name.jpg`)
- **summary**: Brief summary (≤200 words)
- **links**: GitHub and dataset links
- **objectives**: List of objectives
- **accomplishments**: List of achievements
- **importance**: Why it mattered

### Example Hacks to Create
- COVID-19 single-cell data integration
- Cancer genomics hackathon
- Spatial transcriptomics hack
- Multi-omics integration hack

---

## 📚 Publications (`src/content/publications/`)

**Purpose**: Showcase your research publications with search and filtering.

### Required Files
- Replace `smith2024.md` with your actual 2024 publication
- Add all your publications

### Template for Each Publication

```markdown
---
title: "Your Paper Title"
authors:
  - "Smith, Jane"    # Lab members will be automatically highlighted in bold
  - "Johnson, Mike"
  - "Brown, Sarah"
year: 2024
journal: "Nature Methods"
doi: "10.1038/s41592-024-xxxxx"
url: "https://doi.org/10.1038/s41592-024-xxxxx"
openAccessPdf: "https://www.nature.com/articles/s41592-024-xxxxx.pdf"
featured: true # Featured papers show expandable abstracts
theme: ["single-cell-biology", "network-biology"]
socialTags: ["#SingleCell", "#YourTag"]
abstract: "Brief abstract for featured papers only"
---

Your paper summary and additional context.
```

### Required Fields
- **title**: Paper title
- **authors**: Author list (lab members auto-highlighted)
- **year**: Publication year
- **journal**: Journal name
- **doi**: DOI (optional)
- **url**: Paper URL
- **theme**: Research themes for filtering
- **featured**: true/false (shows expandable abstract)

### Author Highlighting
Lab members are automatically highlighted in **bold** in publication author lists. The system matches:
- Full names (case-insensitive)
- Surnames only
- Names from the team collection

### Example Publications to Create
- Recent papers (2023-2024)
- High-impact publications
- Method papers
- Review articles

---

## 👥 Team Members (`src/content/team/`)

**Purpose**: Showcase your team members with profiles and bios.

### Required Files
- Replace `jane-smith.md` with actual PI profile
- Replace `michael-johnson.md` with actual postdoc profile
- Add all team members

### Template for Each Team Member

```markdown
---
name: "Your Full Name"
role: "Your Position"
image: "/assets/team/your-photo.jpg"
quote: "Your personal quote or research philosophy."
github: "https://github.com/yourusername"
scholar: "https://scholar.google.com/citations?user=youruserid"
website: "https://your-website.com"
bioLong: "Your detailed bio describing your research interests and background."
background:
  degrees:
    - "PhD, Your Institution"
    - "BSc, Your Institution"
email: "your.email@soton.ac.uk"
---

Additional biographical information.
```

### Required Fields
- **name**: Full name
- **role**: Position/role
- **image**: Profile photo (`/assets/team/member-name.jpg`)
- **bioLong**: Detailed bio
- **background**: Educational background
- **email**: Contact email

### Example Team Members to Create
- Principal Investigator
- Postdoctoral researchers
- PhD students
- Research assistants
- Visiting researchers

---

## 🖼️ Images & Assets (`public/`)

### Hero Images (`public/hero/`)
**Purpose**: Eye-catching background images for themes and pages.

**Required Images:**
- `biology-visualization.jpg` - Main hero background (1920x1080px)
- `single-cell-hero.jpg` - Single-cell theme image (800x600px)
- `network-biology-hero.jpg` - Network biology theme image (800x600px)
- `lab-group-photo.jpg` - Team photo for About page (1200x800px)

**Image Guidelines:**
- High quality, professional images
- Biology/computational themes
- Consistent color palette
- Optimized file sizes

### Team Photos (`public/assets/team/`)
**Purpose**: Professional headshots for team members.

**Required Images:**
- `jane-smith.jpg` - PI photo (400x400px)
- `michael-johnson.jpg` - Postdoc photo (400x400px)
- Add photos for all team members

**Image Guidelines:**
- Professional headshots
- Consistent lighting and background
- Square aspect ratio (1:1)
- High resolution but optimized

### Tool Screenshots (`public/assets/tools/`)
**Purpose**: Interface screenshots for tools and datasets.

**Required Images:**
- `shinysell.png` - ShinyCell interface screenshot (800x600px)
- Add screenshots for all your tools

**Image Guidelines:**
- Clear interface screenshots
- Show key features
- Consistent styling
- PNG format for screenshots

### Hack Images (`public/assets/hacks/`)
**Purpose**: Photos from research hackathons.

**Required Images:**
- `covid19-hack.jpg` - COVID-19 hack photo (800x600px)
- Add photos for all your hacks

**Image Guidelines:**
- Event photos
- Team collaboration shots
- Results presentations
- High quality, well-lit

### Open Graph Images (`public/og/`)
**Purpose**: Social media preview images.

**Required Images:**
- `default-og.jpg` - Default social media preview (1200x630px)

---

## 📋 Content Creation Priority

### High Priority (Essential for launch)
1. ✅ **Team Members** - Replace sample profiles with real team
2. ✅ **Research Themes** - Replace with your actual research areas
3. ✅ **Publications** - Add your recent publications
4. ✅ **Hero Images** - Add compelling biology visualizations

### Medium Priority (Important for functionality)
5. ✅ **Tools & Datasets** - Add your actual tools
6. ✅ **Research Hacks** - Add your actual hackathons
7. ✅ **Team Photos** - Professional headshots

### Low Priority (Nice to have)
8. ✅ **Tool Screenshots** - Interface screenshots
9. ✅ **Hack Photos** - Event photos
10. ✅ **Open Graph Images** - Social media previews

---

## 🚀 Quick Start Guide

### Step 1: Update Team Members
1. Copy `src/content/team/jane-smith.md`
2. Replace with actual PI information
3. Add profile photo to `public/assets/team/`
4. Repeat for all team members

### Step 2: Add Research Themes
1. Copy `src/content/themes/single-cell-biology.md`
2. Replace with your actual research themes
3. Add hero images to `public/hero/`
4. Update descriptions and order

### Step 3: Add Publications
1. Copy `src/content/publications/smith2024.md`
2. Replace with your actual publications
3. Ensure lab member names match team collection
4. Mark important papers as featured

### Step 4: Add Tools
1. Copy `src/content/tools/shinysell.md`
2. Replace with your actual tools
3. Add screenshots to `public/assets/tools/`
4. Include all relevant metadata

### Step 5: Add Hacks
1. Copy `src/content/hacks/covid19-single-cell.md`
2. Replace with your actual hackathons
3. Add photos to `public/assets/hacks/`
4. Document objectives and achievements

---

## 📝 Content Guidelines

### Writing Style
- **Professional but accessible** - Write for both academic and general audiences
- **Concise descriptions** - Keep front-matter descriptions under 200 words
- **Consistent tone** - Maintain professional academic tone
- **Clear structure** - Use bullet points and short paragraphs

### Image Requirements
- **High quality** - Use professional, high-resolution images
- **Consistent style** - Maintain visual consistency across the site
- **Optimized sizes** - Compress images for web performance
- **Alt text** - Always include descriptive alt text for accessibility

### Technical Requirements
- **Markdown format** - Use proper markdown syntax
- **YAML front-matter** - Follow the exact schema requirements
- **File naming** - Use kebab-case for file names
- **Character limits** - Respect the 200-word limits for descriptions

---

## 🔧 Content Validation

The build process automatically validates:
- ✅ Required fields are present
- ✅ Description limits (≤200 words)
- ✅ Image alt text is provided
- ✅ Email addresses are valid
- ✅ URLs are properly formatted
- ✅ Team member names match for highlighting

---

## 📞 Support

If you need help creating content:
- **Email**: ddnetbio@soton.ac.uk
- **GitHub Issues**: [Create an issue](https://github.com/SGDDNB/DDNB_website/issues)
- **Documentation**: [Astro Docs](https://docs.astro.build)

---

**Happy content creating! 🎉**

Remember: The website automatically rebuilds when you save changes to any markdown file. Just edit, save, and refresh your browser to see the updates!
