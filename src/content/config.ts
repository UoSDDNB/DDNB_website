import { defineCollection, z } from 'astro:content';

const themes = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    image: z.string(),
    description: z.string().max(200, 'Description must be 200 words or less'),
    order: z.number().int().positive(),
  }),
});

const tools = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    type: z.enum(['dataset', 'tool', 'resource']),
    description: z.string().max(200, 'Description must be 200 words or less'),
    image: z.string(),
    imageAlt: z.string(),
    urls: z.object({
      github: z.string().url().optional(),
      paper: z.string().url().optional(),
      website: z.string().url().optional(),
      viewer: z.string().url().optional(),
    }),
    authors: z.array(z.object({
      name: z.string(),
      role: z.string(),
      orcid: z.string().optional(),
    })),
    tags: z.array(z.string()),
    version: z.string().optional(),
    releaseDate: z.string().optional(),
    status: z.enum(['active', 'maintenance', 'archived']).default('active'),
    license: z.string().optional(),
    citation: z.string().optional(),
    doi: z.string().optional(),
    funding: z.array(z.string()).optional(),
    related: z.array(z.string()).optional(),
    requirements: z.string().optional(),
    dataAccess: z.enum(['open', 'controlled', 'upon request']).default('open'),
    contact: z.string().email().default('ddnetbio@soton.ac.uk'),
  }),
});

const hacks = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.string(),
    image: z.string(),
    summary: z.string().max(200, 'Summary must be 200 words or less'),
    links: z.object({
      github: z.string().url().optional(),
      datasets: z.array(z.string().url()).optional(),
    }),
    objectives: z.array(z.string()),
    accomplishments: z.array(z.string()),
    importance: z.string(),
  }),
});

const publications = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    authors: z.array(z.string()),
    year: z.number().int().min(1900).max(2030),
    journal: z.string(),
    doi: z.string().optional(),
    url: z.string().url().optional(),
    openAccessPdf: z.string().url().optional(),
    featured: z.boolean().default(false),
    theme: z.array(z.string()),
    socialTags: z.array(z.string()).optional(),
    abstract: z.string().optional(),
  }),
});

const team = defineCollection({
  type: 'content',
  schema: z.object({
    name: z.string(),
    role: z.string(),
    image: z.string(),
    quote: z.string().optional(),
    github: z.string().url().optional(),
    scholar: z.string().url().optional(),
    website: z.string().url().optional(),
    bioLong: z.string(),
    background: z.object({
      degrees: z.array(z.string()),
    }),
    email: z.string().email(),
  }),
});

export const collections = {
  themes,
  tools,
  hacks,
  publications,
  team,
};
