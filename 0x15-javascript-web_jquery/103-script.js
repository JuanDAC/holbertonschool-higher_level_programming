
const changeHello = (() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  let value;
  return (helloElement, { value: languageCode }) => {
    if (languageCode && value !== languageCode) {
      fetch(`${ url }${ languageCode }`)
        .then(dataRaw => dataRaw.json())
        .then(({ hello }) => helloElement.innerText = hello);
      value = languageCode;
    }
  }
})();

window.onload = () => {
  const helloElement = document.querySelector('DIV#hello');
  const bottonTranslate = document.querySelector('INPUT#btn_translate');
  const inputLanguageCode = document.querySelector('INPUT#language_code');

  inputLanguageCode.addEventListener('keypress', ({ keyCode }) => {
    if (keyCode === 13) {
      changeHello(helloElement, inputLanguageCode);
    }
  });

  bottonTranslate.addEventListener('click', event => {
    event.preventDefault();
    changeHello(helloElement, inputLanguageCode);
  });
};

