document.addEventListener('DOMContentLoaded', function () {
    /* ==========================================
       FLOATING PARTICLES
       ========================================== */
    var particlesContainer = document.querySelector('.er-particles');
    var particlesGenerated = false;

    function generateParticles(count) {
        if (!particlesContainer || particlesGenerated) return;
        particlesGenerated = true;

        for (var i = 0; i < count; i++) {
            var particle = document.createElement('div');
            particle.classList.add('er-particle');

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
        var scrollGlows = document.querySelectorAll('.er-scroll-glow');

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
    const revealTargets = document.querySelectorAll('.er-fade-up');
    if (!revealTargets.length) return;

    const observerOptions = {
        root: null,
        rootMargin: '0px 0px -50px 0px',
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('er-revealed');
                revealObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    revealTargets.forEach(function (el) {
        revealObserver.observe(el);
    });

    /* ==========================================
       EXPANDABLE REVIEW CARDS
       ========================================== */
    const reviewCards = document.querySelectorAll('.er-review-document');
    if (!reviewCards.length) return;

    reviewCards.forEach(function (card) {
        const trigger = card.querySelector('[data-er-toggle]');
        const panel = card.querySelector('.er-review-expanded');

        if (!trigger || !panel) return;

        panel.style.transition = 'max-height 0.45s cubic-bezier(0.25, 0.46, 0.45, 0.94), opacity 0.35s ease';
        panel.style.maxHeight = '0px';

        trigger.addEventListener('click', function () {
            const isActive = card.classList.contains('expanded');

            if (isActive) {
                closeReview(card, trigger, panel);
            } else {
                closeAllReviews();
                openReview(card, trigger, panel);
            }
        });
    });

    function openReview(card, trigger, panel) {
        card.classList.add('expanded');
        trigger.setAttribute('aria-expanded', 'true');
        trigger.textContent = 'Hide Full Review ▲';
        panel.hidden = false;

        const contentHeight = panel.scrollHeight;
        panel.style.maxHeight = contentHeight + 'px';

        requestAnimationFrame(function () {
            panel.style.maxHeight = contentHeight + 'px';
        });

        panel.querySelectorAll('img').forEach(function (img) {
            if (!img.complete) {
                img.addEventListener('load', function () {
                    if (card.classList.contains('expanded')) {
                        panel.style.maxHeight = panel.scrollHeight + 'px';
                    }
                });
            }
        });
    }

    function closeReview(card, trigger, panel) {
        card.classList.remove('expanded');
        trigger.setAttribute('aria-expanded', 'false');
        trigger.textContent = 'Read Full Review ▼';
        panel.style.maxHeight = '0px';

        panel.addEventListener('transitionend', function handler() {
            if (!card.classList.contains('expanded')) {
                panel.hidden = true;
            }
            panel.removeEventListener('transitionend', handler);
        });
    }

    function closeAllReviews() {
        reviewCards.forEach(function (card) {
            if (card.classList.contains('expanded')) {
                const trigger = card.querySelector('[data-er-toggle]');
                const panel = card.querySelector('.er-review-expanded');
                if (trigger && panel) {
                    closeReview(card, trigger, panel);
                }
            }
        });
    }
});