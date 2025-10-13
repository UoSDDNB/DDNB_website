/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
        colors: {
          'skyMagenta': {
            DEFAULT: '#DA64B4',
            100: '#330c27',
            200: '#66194d',
            300: '#992574',
            400: '#cc319b',
            500: '#da64b4',
            600: '#e182c3',
            700: '#e8a1d2',
            800: '#f0c1e1',
            900: '#f7e0f0'
          },
          'tekhelet': {
            DEFAULT: '#482D8A',
            100: '#0e091c',
            200: '#1d1237',
            300: '#2b1b53',
            400: '#39246f',
            500: '#482d8a',
            600: '#613dbc',
            700: '#876bcf',
            800: '#af9cdf',
            900: '#d7ceef'
          },
          'bittersweet': {
            DEFAULT: '#F9565B',
            100: '#410204',
            200: '#820509',
            300: '#c3070d',
            400: '#f7171e',
            500: '#f9565b',
            600: '#fa797d',
            700: '#fb9b9e',
            800: '#fdbcbe',
            900: '#fededf'
          },
          'babyBlue': {
            DEFAULT: '#78C4E8',
            100: '#0a2c3c',
            200: '#145978',
            300: '#1f85b5',
            400: '#3cabde',
            500: '#78c4e8',
            600: '#93d0ed',
            700: '#aedcf1',
            800: '#c9e8f6',
            900: '#e4f3fa'
          },
          'tropicalIndigo': {
            DEFAULT: '#8488DE',
            100: '#0f1138',
            200: '#1e226f',
            300: '#2c32a7',
            400: '#4b51cf',
            500: '#8488de',
            600: '#9b9fe4',
            700: '#b4b7eb',
            800: '#cdcff2',
            900: '#e6e7f8'
          },
          // Legacy brand colors for backward compatibility
          'brand-primary': '#482D8A', // tekhelet
          'brand-accent': '#DA64B4', // sky-magenta
          'brand-soft': '#e4f3fa', // baby-blue-900
          'brand-dark': '#0e091c', // tekhelet-100
          'brand-lime': '#78C4E8', // baby-blue
        },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      lineHeight: {
        'relaxed': '1.6',
        'loose': '1.7',
      },
      gridTemplateColumns: {
        '12': 'repeat(12, minmax(0, 1fr))',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.3s ease-out',
        'float': 'float 3s ease-in-out infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(10px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
    },
  },
  plugins: [],
}
