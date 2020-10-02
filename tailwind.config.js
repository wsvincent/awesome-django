module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  purge: {
    enabled: process.env.JEKYLL_ENV == "production",
    mode: 'all',
    content: [
      '**/*.html'
    ],
  },
  plugins: [
    require("@tailwindcss/typography"),
    require("tailwindcss-debug-screens"),
  ],
  theme: {
    extend: {},
  },
  variants: {},
}
