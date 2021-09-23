const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

const addHello = (hello) => {
  const textNode = document.createTextNode(hello);
  const helloDiv = document.querySelector('DIV#hello');
  if (helloDiv && textNode) {
    helloDiv.appendChild(textNode);
  }
};

fetch(url)
  .then((dataRaw) => dataRaw.json())
  .then(({ hello }) => {
    if (document.readyState === 'ready' || document.readyState === 'complete') {
      addHello(hello);
    } else {
      window.onload = () => addHello(hello);
    }
  });
