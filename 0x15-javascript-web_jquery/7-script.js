const character = document.querySelector('DIV#character');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((dataRaw) => dataRaw.json())
  .then(({ name }) => {
    const textNode = document.createTextNode(name);
    character.appendChild(textNode);
  });

