(function () {
    const DEFAULT_BASE = window.location.origin;

    if (window.API_BASE && typeof window.API_BASE === 'string') {
        return;
    }

    if (window.__API_BASE__ && typeof window.__API_BASE__ === 'string') {
        window.API_BASE = window.__API_BASE__;
        return;
    }

    const port = window.location.port;
    if (port && port !== '5000') {
        window.API_BASE = `${window.location.protocol}//${window.location.hostname}:5000`;
    } else {
        window.API_BASE = DEFAULT_BASE;
    }
})();

