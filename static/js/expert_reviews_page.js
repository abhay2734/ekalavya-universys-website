
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
    var scrollGlows = document.querySelectorAll('.er-scroll-glow');

    if (scrollGlows.length) {
        window.addEventListener('scroll', function () {
            var scrollY = window.pageYOffset;

            scrollGlows.forEach(function (glow) {
                var speed = 0.03;
                glow.style.transform =
                    'translateX(-50%) translateY(' + (scrollY * speed) + 'px)';
            });
        }, { passive: true });
    }

    /* ==========================================
       SCROLL REVEAL - FADE UP
       ========================================== */
    var revealTargets = document.querySelectorAll('.er-fade-up');

    if (revealTargets.length && 'IntersectionObserver' in window) {
        var observerOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        };

        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('er-revealed');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, observerOptions);

        revealTargets.forEach(function (element) {
            revealObserver.observe(element);
        });
    } else {
        revealTargets.forEach(function (element) {
            element.classList.add('er-revealed');
        });
    }

    /* ==========================================
       INDEPENDENT TESTIMONIAL EXPANSION
       Each review opens and closes independently.
       ========================================== */
    var reviewRows = document.querySelectorAll('.er-review-row');

    reviewRows.forEach(function (row) {
        var trigger = row.querySelector('[data-er-toggle]');
        var panel = row.querySelector('.er-review-expanded');

        if (!trigger || !panel) return;

        // Preserve the button text configured in Django Admin.
        var originalButtonText = trigger.textContent.trim();

        trigger.setAttribute('aria-expanded', 'false');
        panel.hidden = true;
        panel.style.maxHeight = '0px';
        panel.style.opacity = '0';

        trigger.addEventListener('click', function () {
            var isExpanded = row.classList.contains('expanded');

            if (isExpanded) {
                closeReview(row, trigger, panel, originalButtonText);
            } else {
                openReview(row, trigger, panel);
            }
        });

        // Recalculate panel height if a testimonial image loads late.
        panel.querySelectorAll('img').forEach(function (image) {
            image.addEventListener('load', function () {
                if (row.classList.contains('expanded')) {
                    panel.style.maxHeight = panel.scrollHeight + 'px';
                }
            });
        });
    });

    function openReview(row, trigger, panel) {
        // Make the panel measurable before starting the animation.
        panel.hidden = false;
        panel.style.maxHeight = '0px';
        panel.style.opacity = '0';

        // Apply the initial collapsed state before expanding.
        panel.offsetHeight;

        row.classList.add('expanded');
        trigger.setAttribute('aria-expanded', 'true');
        trigger.textContent = 'Hide Testimonial ▲';

        requestAnimationFrame(function () {
            if (!row.classList.contains('expanded')) return;

            panel.style.maxHeight = panel.scrollHeight + 'px';
            panel.style.opacity = '1';
        });
    }

    function closeReview(row, trigger, panel, originalButtonText) {
        // Start from the current height so the closing animation is smooth.
        panel.style.maxHeight = panel.scrollHeight + 'px';
        panel.offsetHeight;

        row.classList.remove('expanded');
        trigger.setAttribute('aria-expanded', 'false');
        trigger.textContent = originalButtonText;

        requestAnimationFrame(function () {
            panel.style.maxHeight = '0px';
            panel.style.opacity = '0';
        });

        function finishClosing(event) {
            // Ignore opacity and other transitions; wait for the height.
            if (event.propertyName !== 'max-height') return;

            panel.removeEventListener('transitionend', finishClosing);

            if (!row.classList.contains('expanded')) {
                panel.hidden = true;
            }
        }

        panel.addEventListener('transitionend', finishClosing);
    }
});
