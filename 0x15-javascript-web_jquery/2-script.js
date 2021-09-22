const clickMe = document.querySelector('DIV#red_header');
const header = document.querySelector('header');

clickMe?.addEventListener('click', () => 
  header?.style?.setProperty('background-color', '#ff0000')
);

