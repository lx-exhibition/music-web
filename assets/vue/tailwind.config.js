/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      spacing: {
        1.1: '20rem'
      },
      backgroundImage: {
        sex: "url('https://sex.nyan.xyz/api/v2/img?r18=true&author_uuid=66371932&author_uuid=70395770&author_uuid=17516104&author_uuid=14496985&author_uuid=13835102&author_uuid=1642433&author_uuid=23040640')",
        gif: "url('http://localhost:8001/media/m/preview.gif')"
      },
      keyframes: {
        'wiggle': {
          '0%, 100%': { transform: 'rotate(-30deg)' },
          '50%': { transform: 'rotate(30deg)' },
        },
        'circle': {
          '0%': { transform: 'rotate(0deg)' },
          '100%': { transform: 'rotate(360deg)' },
        },
      },
      animation: {
        wiggle: 'wiggle 0.1s ease-in-out infinite',
        circle: 'circle 0.2s ease-in-out infinite',
        'up-down': 'bounce 0.2s ease-in-out infinite',
        'slow-circle': 'circle 5s infinite',
        'slow-spin': 'spin 5s linear infinite',
      }
    },
  },
  plugins: [],
  corePlugins: {
    // preflight: false,
  }
}

