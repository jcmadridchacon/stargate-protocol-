const CACHE_NAME = 'stargate-psi-c-v1';
const urlsToCache = [
  '/stargate-protocolo/index.html',
  '/stargate-protocolo/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(urlsToCache))
  );
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});
