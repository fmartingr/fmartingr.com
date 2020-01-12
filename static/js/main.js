// Fix for lektor highlight plugin
var elements = document.querySelectorAll('div.highlight');
for (var i = 0; i < elements.length; i++) {
  elements[i].classList.add('hll');
}
