// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.ddnetbio.com',
  // Remove base path for local development
  // base: '/DDNB_website/', // Only needed for GitHub Pages deployment
  output: 'static',
  integrations: [tailwind()]
});