const listToAdd = document.querySelector('UL#list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then((dataRaw) => dataRaw.json())
  .then(({ results }) => results?.forEach(({ title }) => {
    const newLi = document.createElement('LI');
    const textNode = document.createTextNode(title);
    if (newLi && listToAdd && textNode) {
      newLi.appendChild(textNode);
      listToAdd.appendChild(newLi);
    }
  }));
