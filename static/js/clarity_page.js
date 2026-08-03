/* ============================================
   CLARITY PAGE - ROYAL SCROLL EXPERIENCE
   ============================================ */

(function () {
    'use strict';

    var CONFETTI_CONTAINER = document.querySelector('.clarity-particles');
    var particlesGenerated = false;

    /* --- Generate Floating Particles --- */
    function generateParticles(count) {
        if (!CONFETTI_CONTAINER || particlesGenerated) return;
        particlesGenerated = true;

        for (var i = 0; i < count; i++) {
            var particle = document.createElement('div');
            particle.classList.add('clarity-particle');

            var size = Math.random() * 4 + 2;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDuration = (Math.random() * 8 + 6) + 's';
            particle.style.animationDelay = Math.random() * 6 + 's';

            CONFETTI_CONTAINER.appendChild(particle);
        }
    }

    /* --- Reveal sections on scroll --- */
    function revealSections() {
        var sections = document.querySelectorAll('.clarity-reveal');
        if (!sections.length) return;

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.15,
            rootMargin: '0px 0px -40px 0px'
        });

        sections.forEach(function (section, index) {
            section.style.transitionDelay = (index * 0.12) + 's';
            observer.observe(section);
        });
    }

    /* --- Parallax on scroll (subtle) --- */
    function initParallax() {
        var scrollGems = document.querySelectorAll('.clarity-scroll-glow');

        window.addEventListener('scroll', function () {
            var scrollY = window.pageYOffset;
            scrollGems.forEach(function (gem) {
                var speed = 0.03;
                gem.style.transform = 'translateX(-50%) translateY(' + (scrollY * speed) + 'px)';
            });
        }, { passive: true });
    }

    /* --- Initialize --- */
    generateParticles(35);
    revealSections();
    initParallax();

})();