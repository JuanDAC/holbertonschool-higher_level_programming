const clickMe = document.querySelector('DIV#update_header');
const header = document.querySelector('header');

clickMe?.addEventListener('click', () => {
  const textNode = document.createTextNode('New Header!!!');
  if (header && textNode) {
    [...header.childNodes].pop()?.remove();
    header.appendChild(textNode);
  }
});
