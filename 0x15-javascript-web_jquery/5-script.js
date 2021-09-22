const clickMe = document.querySelector('DIV#add_item');
const listToAdd = document.querySelector('UL.my_list');

clickMe?.addEventListener('click', () => {
  const newLi = document.createElement('LI');
  const textNode = document.createTextNode('Item');
  if (newLi && listToAdd && textNode) {
    newLi.appendChild(textNode);
    listToAdd.appendChild(newLi);
  }
});

