// Minimal UI helpers for loading overlay
(function () {
  const OVERLAY_ID = 'appLoadingOverlay';

  function createOverlay() {
    if (document.getElementById(OVERLAY_ID)) return;
    const overlay = document.createElement('div');
    overlay.id = OVERLAY_ID;
    overlay.className = 'loading-overlay';
    overlay.style.display = 'none';

    const spinner = document.createElement('div');
    spinner.className = 'spinner';
    overlay.appendChild(spinner);

    const msg = document.createElement('p');
    msg.className = 'loading-message';
    msg.textContent = 'Loading...';
    overlay.appendChild(msg);

    document.body.appendChild(overlay);
  }

  function showLoading(text = 'Loading...') {
    createOverlay();
    const overlay = document.getElementById(OVERLAY_ID);
    const msg = overlay.querySelector('.loading-message');
    if (msg) msg.textContent = text;
    overlay.style.display = 'flex';
    // small repaint to ensure overlay is shown before navigation
    requestAnimationFrame(() => {});
  }

  function hideLoading() {
    const overlay = document.getElementById(OVERLAY_ID);
    if (overlay) overlay.style.display = 'none';
  }

  window.showLoading = showLoading;
  window.hideLoading = hideLoading;
})();
