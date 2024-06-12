/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        chatblack: {50: '#343541'},
        login: {100: '#10A37F'},
      }
    },
  },
  plugins: [],
}

