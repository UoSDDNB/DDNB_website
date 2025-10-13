# Data-Driven Network Biology Group Website

A modern, professional website for the Data-Driven Network Biology Group at the University of Southampton. Built with Astro, Tailwind CSS, and TypeScript, featuring markdown-first content management and automatic GitHub Pages deployment.

## 🚀 Quick Start

### Prerequisites

- **Node.js 22.x** (required for Astro 4.x compatibility)
- **npm** (comes with Node.js)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/UoSDDNB/DDNB_website.git
   cd DDNB_website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:4321` to see the website.

## 📁 Project Structure

```
/
├── public/                     # Static assets
│   ├── logo.svg               # Group logo
│   ├── hero/                  # Hero section images
│   ├── og/                    # Open Graph images
│   └── assets/                # Team, tools, hacks images
├── src/
│   ├── components/            # Reusable components
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── HeroSection.astro
│   │   ├── ThemeCard.astro
│   │   ├── ToolCard.astro
│   │   ├── PublicationItem.astro
│   │   └── TeamMemberCard.astro
│   ├── layouts/
│   │   └── BaseLayout.astro   # Main layout template
│   ├── pages/                 # Route pages
│   │   ├── index.astro        # Home page
│   │   ├── research-themes.astro
│   │   ├── data-tools.astro
│   │   ├── hacks.astro
│   │   ├── publications.astro
│   │   └── about.astro
│   ├── styles/
│   │   └── global.css         # Global styles & Tailwind
│   └── content/
│       └── config.ts          # Content collection schemas
├── content/                   # MARKDOWN-FIRST CONTENT
│   ├── themes/               # Research themes (one MD per theme)
│   ├── tools/                # Tools & datasets (one MD per item)
│   ├── hacks/                # Hacks (one MD per hack)
│   ├── publications/         # Publications (one MD per paper)
│   └── team/                 # Team members (one MD per member)
├── .github/workflows/
│   └── pages.yml             # GitHub Pages CI/CD
├── astro.config.mjs          # Astro configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── CNAME                     # Custom domain: www.ddnetbio.com
└── README.md
```

## 📝 Content Management

This website uses a **markdown-first approach** - all content is managed through markdown files in the `content/` directory. Simply add or edit `.md` files and push to GitHub for automatic deployment.

### Adding New Content

#### Research Themes (`content/themes/`)

Create a new file `content/themes/your-theme.md`:

```markdown
---
title: "Your Theme Title"
image: "/hero/your-theme-image.jpg"
description: "Brief description (≤200 words) of your research theme and its significance."
order: 3
---

Your detailed description of the research theme goes here.
```

#### Tools & Datasets (`content/tools/`)

Create a new file `content/tools/your-tool.md`:

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
tags: ["single-cell", "RNA-seq", "R", "Shiny"]
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

#### Publications (`content/publications/`)

Create a new file `content/publications/your-paper.md`:

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

#### Team Members (`content/team/`)

Create a new file `content/team/your-name.md`:

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

#### Hacks (`content/hacks/`)

Create a new file `content/hacks/your-hack.md`:

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

### Images

Place images in the appropriate `public/` subdirectories:

- **Team photos**: `public/assets/team/`
- **Tool screenshots**: `public/assets/tools/`
- **Hack images**: `public/assets/hacks/`
- **Hero images**: `public/hero/`
- **Open Graph images**: `public/og/`

**Naming convention**: Use kebab-case (e.g., `jane-smith.jpg`, `single-cell-analysis.png`)

## 🎨 Styling & Branding

### Brand Colours

The website uses a carefully selected colour palette defined in `tailwind.config.js`:

- **Primary**: `#1C7C54` (Dark green)
- **Accent**: `#73E2A7` (Light green)
- **Soft**: `#DEF4C6` (Very light green)
- **Dark**: `#1B512D` (Darker green)
- **Lime**: `#B1CF5F` (Lime green)

### Tailwind CSS Classes

Use these utility classes for consistent styling:

```html
<!-- Buttons -->
<button class="btn-primary">Primary Button</button>
<button class="btn-secondary">Secondary Button</button>

<!-- Cards -->
<div class="card">Card content</div>

<!-- Tags -->
<span class="tag">Tag text</span>

<!-- Containers -->
<div class="container-custom">Content with max-width and padding</div>

<!-- Grid -->
<div class="grid-12">12-column grid layout</div>
```

### Custom CSS

Global styles are defined in `src/styles/global.css`. The file includes:

- CSS custom properties for brand colours
- Base typography (Inter font, 1.6 line-height)
- Accessibility utilities (focus states, reduced motion)
- Component classes (buttons, cards, tags)

## 🔍 Search & Filtering

### Publications Search

The publications page includes client-side search and filtering:

- **Search**: Searches title, authors, journal, and themes
- **Year filter**: Filter by publication year
- **Theme filter**: Filter by research theme
- **Featured filter**: Show only featured publications

### Author Highlighting

Lab members are automatically highlighted in **bold** in publication author lists. The system matches:

- Full names (case-insensitive)
- Surnames only
- Names from the team collection

To ensure proper highlighting, make sure team member names in `content/team/` match exactly how they appear in publication author lists.

## 🚀 Deployment

### Automatic Deployment

The website automatically deploys to GitHub Pages when you push to the `main` branch:

1. **Push your changes**
   ```bash
   git add .
   git commit -m "Add new content"
   git push origin main
   ```

2. **GitHub Actions builds and deploys**
   - Check the Actions tab in your GitHub repository
   - The workflow runs: `npm install` → `npm run build` → Deploy to Pages

3. **View your changes**
   - Visit `https://www.ddnetbio.com` (custom domain)
   - Or `https://uosddnb.github.io/DDNB_website/` (GitHub Pages URL)

### Custom Domain Setup

The website is configured for the custom domain `www.ddnetbio.com`:

1. **CNAME file**: Already created with `www.ddnetbio.com`
2. **GitHub Pages settings**:
   - Go to repository Settings → Pages
   - Set Custom Domain to `www.ddnetbio.com`
   - Enable "Enforce HTTPS"
3. **DNS configuration** (at your domain registrar):
   - Create a CNAME record: `www` → `uosddnb.github.io`

### Manual Deployment

If you need to deploy manually:

```bash
npm run build
# The built site will be in the dist/ directory
```

## 🛠️ Development Commands

| Command | Action |
|---------|--------|
| `npm run dev` | Start development server at `localhost:4321` |
| `npm run build` | Build production site to `./dist/` |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint to check for code issues |
| `npm run lint:fix` | Fix ESLint issues automatically |
| `npm run format` | Format code with Prettier |
| `npm run check` | Run Astro type checking |

## 🔧 Configuration

### Astro Configuration (`astro.config.mjs`)

```javascript
export default defineConfig({
  site: 'https://www.ddnetbio.com',
  base: '/DDNB_website/',
  output: 'static',
  // ... other config
});
```

### Tailwind Configuration (`tailwind.config.js`)

Custom colours, fonts, and utilities are defined here. The configuration extends the default Tailwind setup with:

- Brand colour palette
- Inter font family
- Custom spacing and grid
- Animation keyframes
- Component classes

### TypeScript Configuration (`tsconfig.json`)

Strict TypeScript configuration with:

- Path aliases (`@/components`, `@/layouts`)
- Strict type checking
- Astro-specific settings

## 📚 Content Validation

The build process includes validation for:

- **Required fields**: All content collections have required fields
- **Description limits**: 200-word limits are enforced
- **Image alt text**: Required for accessibility
- **Email validation**: Team member emails must be valid
- **URL validation**: All URLs must be properly formatted

## 🤝 Contributing

### Adding New Features

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Add new components in `src/components/`
   - Add new pages in `src/pages/`
   - Update content schemas in `src/content/config.ts`

3. **Test locally**
   ```bash
   npm run dev
   npm run build
   npm run lint
   ```

4. **Submit a pull request**

### Code Style

- **TypeScript**: Use strict typing, avoid `any`
- **Astro**: Follow Astro best practices
- **CSS**: Use Tailwind utilities, avoid custom CSS when possible
- **Accessibility**: Include proper ARIA labels and alt text
- **Performance**: Optimize images and use lazy loading

## 📞 Support

- **Email**: ddnetbio@soton.ac.uk
- **GitHub Issues**: [Create an issue](https://github.com/SGDDNB/DDNB_website/issues)
- **Documentation**: [Astro Docs](https://docs.astro.build)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ using [Astro](https://astro.build), [Tailwind CSS](https://tailwindcss.com), and [TypeScript](https://www.typescriptlang.org/).