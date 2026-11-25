// Click any project image to view it full size with its caption.
(function () {
  var box = document.createElement('div');
  box.className = 'lightbox';
  box.setAttribute('role', 'dialog');
  box.setAttribute('aria-label', 'Image viewer');
  box.innerHTML = '<img alt=""><p></p>';
  document.body.appendChild(box);
  var big = box.querySelector('img'), cap = box.querySelector('p');

  document.querySelectorAll('figure .frame img').forEach(function (img) {
    img.parentElement.addEventListener('click', function () {
      big.src = img.src;
      big.alt = img.alt;
      var fc = img.closest('figure').querySelector('figcaption');
      cap.textContent = fc ? fc.textContent : '';
      box.classList.add('open');
    });
  });
  function close() { box.classList.remove('open'); }
  box.addEventListener('click', close);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();
