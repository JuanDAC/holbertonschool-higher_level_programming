
const url = 'https://fourtonfish.com/hellosalut/?lang=';

window.onload = () => {
  const helloElement = document.querySelector('DIV#hello');
  const inputLanguageCode = document.querySelector('INPUT#language_code');
  const bottonTranslate = document.querySelector('INPUT#btn_translate');
  let { value } = inputLanguageCode;

  bottonTranslate.addEventListener('click', event => {
    event.preventDefault();
    if (inputLanguageCode.value && value !== inputLanguageCode.value) {
      value = inputLanguageCode.value;
      fetch(`${ url }${ value }`)
        .then(dataRaw => dataRaw.json())
        .then(({ hello }) => helloElement.innerText = hello);
    }
  });
};

