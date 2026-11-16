/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        gold: {
          light: '#F5E6BE',
          DEFAULT: '#D4AF37',
          dark: '#996515',
          metallic: '#C5A059',
          glow: '#FFE29A',
        },
        maroon: {
          light: '#801323',
          DEFAULT: '#5B0616',
          dark: '#3D030E',
          royal: '#6B0B1D',
        },
        sage: {
          50: '#F4F7F4',
          100: '#E5EBE5',
          200: '#CBD7CB',
          300: '#A8BEA8',
          DEFAULT: '#8A9A86',
          dark: '#586A55',
        },
        ivory: {
          DEFAULT: '#FCFAF5',
          soft: '#F5F0E6',
          card: '#FDFCF7',
        },
        blush: {
          light: '#FFF0F3',
          DEFAULT: '#FAD2E1',
          rose: '#E8A5B8',
        }
      },
      fontFamily: {
        serif: ['var(--font-cinzel)', 'Georgia', 'serif'],
        script: ['var(--font-great-vibes)', 'cursive', 'Georgia'],
        sans: ['var(--font-inter)', 'system-ui', 'sans-serif'],
      },
      animation: {
        'float-slow': 'float 6s ease-in-out infinite',
        'pulse-glow': 'pulseGlow 2.5s ease-in-out infinite',
        'sparkle': 'sparkle 1.8s ease-in-out infinite',
        'shimmer': 'shimmer 2.5s linear infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        pulseGlow: {
          '0%, 100%': { opacity: '0.6', transform: 'scale(1)' },
          '50%': { opacity: '1', transform: 'scale(1.05)' },
        },
        sparkle: {
          '0%, 100%': { opacity: '0.2', transform: 'scale(0.8) rotate(0deg)' },
          '50%': { opacity: '1', transform: 'scale(1.2) rotate(180deg)' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-200% 0' },
          '100%': { backgroundPosition: '200% 0' },
        }
      }
    },
  },
  plugins: [],
};
