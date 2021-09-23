const addItem = (list) => {
  if (list instanceof HTMLElement) {
    const textNode = document.createTextNode('Item');
    const newItem = document.createElement('LI');
    newItem?.appendChild(textNode);
    list.appendChild(newItem);
  }
};

const removeItem = (list) => {
  if (list instanceof HTMLElement) {
    [...list.children]?.pop()?.remove();
  }
};

const clearList = (list) => {
  if (list instanceof HTMLElement) {
    const textNode = document.createTextNode('Item');
    const newItem = document.createElement('LI');
    [...list.children]?.forEach(item => item?.remove());
  }
};

window.onload = () => {
  const listToAdd = document.querySelector('UL.my_list');
  document.querySelector('DIV#add_item')
    .addEventListener('click', () => addItem(listToAdd));
  document.querySelector('DIV#remove_item')
    .addEventListener('click', () => removeItem(listToAdd));
  document.querySelector('DIV#clear_list')
    .addEventListener('click', () => clearList(listToAdd));
}

