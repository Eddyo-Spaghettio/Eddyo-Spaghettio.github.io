// A short, native-scroll opening sequence. Navigation never depends on animation.
(() => {
  const opening = document.querySelector('.opening');
  const frame = document.querySelector('.opening-frame');
  if (!opening || !frame) return;
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let pending = 0;
  function paint() {
    pending = 0;
    const distance = opening.offsetHeight - frame.offsetHeight;
    const progress = distance > 0 ? Math.min(1, Math.max(0, -opening.getBoundingClientRect().top / distance)) : 0;
    opening.style.setProperty('--progress', progress.toFixed(4));
  }
  function schedule() {
    if (!pending) pending = requestAnimationFrame(paint);
  }
  function configure() {
    document.documentElement.classList.remove('scroll-opening');
    // On short screens / large text, let the full introduction scroll normally.
    const fits = frame.scrollHeight <= window.innerHeight - 20;
    document.documentElement.classList.toggle('scroll-opening', !preference.matches && fits);
    paint();
  }
  window.addEventListener('scroll', schedule, { passive: true });
  window.addEventListener('resize', configure);
  window.addEventListener('pageshow', configure);
  preference.addEventListener('change', configure);
  configure();
})();
