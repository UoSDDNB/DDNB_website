// @ts-check
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.ddnetbio.com',
  base: '/DDNB_website/', // Required for GitHub Pages deployment
  output: 'static',
  integrations: [tailwind()],
  trailingSlash: 'always'
});