function ghtml(url){
  var x = true;
  window.addEventListener('load', function (evt) {
    chrome.extension.getBackgroundPage().chrome.tabs.executeScript(null, {
      file: 'get.js'
    });
    x = false;
  });
  while(x);
}
ghtml("https://www.github.com/login");