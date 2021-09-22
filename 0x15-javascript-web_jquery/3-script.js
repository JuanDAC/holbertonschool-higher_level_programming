const header = document.querySelector('header');
const clickMe = document.querySelector('DIV#red_header');

clickMe?.addEventListener('click', () =>
  header?.style?.setAttribute('class', 'red');
);

