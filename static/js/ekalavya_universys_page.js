document.addEventListener('DOMContentLoaded', function() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    var reveals = document.querySelectorAll('.ekalavya-landing .landing-sections .hero-wrapper');
    if (!reveals.length) return;

    var thumbIndex = 0;
    reveals.forEach(function(el) {
        if (el.querySelector('.hero-image[data-video-type]')) {
            el.style.transitionDelay = (thumbIndex * 80) + 'ms';
            thumbIndex++;
        }
    });

    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('eku-revealed');
                observer.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.1
    });

    reveals.forEach(function(el) {
        observer.observe(el);
    });
});
