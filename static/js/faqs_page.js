document.addEventListener('DOMContentLoaded', function () {
    /* ==========================================
       FLOATING PARTICLES
       ========================================== */
    var particlesContainer = document.querySelector('.faqs-particles');
    var particlesGenerated = false;

    function generateParticles(count) {
        if (!particlesContainer || particlesGenerated) return;
        particlesGenerated = true;

        for (var i = 0; i < count; i++) {
            var particle = document.createElement('div');
            particle.classList.add('faqs-particle');

            var size = Math.random() * 4 + 2;
            particle.style.width = size + 'px';
            particle.style.height = size + 'px';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDuration = (Math.random() * 8 + 6) + 's';
            particle.style.animationDelay = Math.random() * 6 + 's';

            particlesContainer.appendChild(particle);
        }
    }

    generateParticles(35);

    /* ==========================================
       PARALLAX ON SCROLL GLOW
       ========================================== */
    function initParallax() {
        var scrollGlows = document.querySelectorAll('.faqs-scroll-glow');

        window.addEventListener('scroll', function () {
            var scrollY = window.pageYOffset;
            scrollGlows.forEach(function (glow) {
                var speed = 0.03;
                glow.style.transform = 'translateX(-50%) translateY(' + (scrollY * speed) + 'px)';
            });
        }, { passive: true });
    }

    initParallax();

    /* ==========================================
       SCROLL REVEAL - FADE UP
       ========================================== */
    var revealTargets = document.querySelectorAll('.faqs-fade-up');
    if (revealTargets.length) {
        var observerOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        };

        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('faqs-revealed');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        revealTargets.forEach(function (el) {
            revealObserver.observe(el);
        });
    }

    /* ==========================================
       ACCORDION
       ========================================== */
    var accordionItems = document.querySelectorAll('.faqs-accordion-item');
    if (!accordionItems.length) return;

    accordionItems.forEach(function (item) {
        var trigger = item.querySelector('.faqs-accordion-trigger');
        var panel = item.querySelector('.faqs-accordion-panel');

        trigger.addEventListener('click', function () {
            var isActive = item.classList.contains('active');

            if (isActive) {
                closeItem(item);
            } else {
                closeAllItems(accordionItems);
                openItem(item);
            }
        });
    });

    function openItem(item) {
        var trigger = item.querySelector('.faqs-accordion-trigger');
        var panel = item.querySelector('.faqs-accordion-panel');

        item.classList.add('active');
        trigger.setAttribute('aria-expanded', 'true');
        panel.hidden = false;

        var contentHeight = panel.scrollHeight;
        panel.style.maxHeight = contentHeight + 'px';

        requestAnimationFrame(function () {
            panel.style.maxHeight = contentHeight + 'px';
        });
    }

    function closeItem(item) {
        var trigger = item.querySelector('.faqs-accordion-trigger');
        var panel = item.querySelector('.faqs-accordion-panel');

        item.classList.remove('active');
        trigger.setAttribute('aria-expanded', 'false');
        panel.style.maxHeight = '0px';

        panel.addEventListener('transitionend', function handler() {
            if (!item.classList.contains('active')) {
                panel.hidden = true;
            }
            panel.removeEventListener('transitionend', handler);
        });
    }

    function closeAllItems(items) {
        items.forEach(function (item) {
            if (item.classList.contains('active')) {
                closeItem(item);
            }
        });
    }
});