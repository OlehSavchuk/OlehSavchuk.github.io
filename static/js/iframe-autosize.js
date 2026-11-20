// Resize same-origin <iframe class="autosize"> elements to fit their content.
(function () {
  function fit(frame) {
    try {
      var doc = frame.contentDocument;
      if (!doc || !doc.documentElement) return;
      frame.style.height = doc.documentElement.scrollHeight + 'px';
    } catch (e) { /* cross-origin: keep CSS fallback height */ }
  }
  function attach(frame) {
    fit(frame);
    try {
      var doc = frame.contentDocument;
      if (window.ResizeObserver && doc && doc.body) {
        new ResizeObserver(function () { fit(frame); }).observe(doc.body);
      }
    } catch (e) {}
  }
  document.querySelectorAll('iframe.autosize').forEach(function (frame) {
    frame.addEventListener('load', function () { attach(frame); });
    if (frame.contentDocument && frame.contentDocument.readyState === 'complete') attach(frame);
  });
  // Re-measure when a collapsed <details> section is opened.
  document.querySelectorAll('details').forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) d.querySelectorAll('iframe.autosize').forEach(fit);
    });
  });
  window.addEventListener('resize', function () {
    document.querySelectorAll('iframe.autosize').forEach(fit);
  });
})();
