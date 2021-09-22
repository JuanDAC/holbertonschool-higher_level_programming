const header = document.querySelector('header');
const clickMe = document.querySelector('DIV#toggle_header');

clickMe?.addEventListener('click', () => {
  header?.classList?.toggle('class', 'green');
  header?.classList?.toggle('class', 'red');
});

