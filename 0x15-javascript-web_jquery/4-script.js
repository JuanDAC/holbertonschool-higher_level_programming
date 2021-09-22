const header = document.querySelector('header');
const clickMe = document.querySelector('DIV#toggle_header');

clickMe?.addEventListener('click', () => {
  header?.classList?.toggle('green');
  header?.classList?.toggle('red');
});

