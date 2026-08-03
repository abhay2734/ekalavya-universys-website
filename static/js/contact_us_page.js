document.addEventListener('DOMContentLoaded', function () {
    'use strict';

    /* ==========================================
       SCROLL REVEAL - FADE UP
       ========================================== */
    var revealTargets = document.querySelectorAll('.cu-fade-up');
    if (revealTargets.length) {
        if ('IntersectionObserver' in window) {
            var observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('cu-revealed');
                        observer.unobserve(entry.target);
                    }
                });
            }, { root: null, rootMargin: '0px 0px -50px 0px', threshold: 0.1 });
            revealTargets.forEach(function (el) { observer.observe(el); });
        } else {
            revealTargets.forEach(function (el) { el.classList.add('cu-revealed'); });
        }
    }

    /* ==========================================
       SUBJECT AUTO-FILL (help cards + decision cards)
       ========================================== */
    var subjectInput = document.getElementById('cu_subject');

    function fillSubject(value) {
        if (!subjectInput || !value) return;
        subjectInput.value = value;
        subjectInput.dispatchEvent(new Event('blur'));
        subjectInput.focus();
        subjectInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    document.querySelectorAll('[data-cu-card]').forEach(function (card) {
        card.addEventListener('click', function () {
            fillSubject(card.getAttribute('data-subject'));
        });
    });

    /* ==========================================
       LIVE VALIDATION + CHARACTER COUNTER
       ========================================== */
    var MAX_MESSAGE = 2000;
    var form = document.getElementById('cuForm');
    var messageInput = document.getElementById('cu_message');
    var counter = document.getElementById('cu_char_counter');

    function validEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
    }

    function validateField(input) {
        var field = input.closest('.cu-field');
        var errorEl = field ? field.querySelector('.cu-field-error') : null;
        if (!field || !errorEl) return true;

        var name = input.getAttribute('name');
        var value = input.value.trim();
        var msg = '';

        if (name === 'full_name') {
            if (!value) msg = 'Please enter your full name.';
            else if (value.length > 200) msg = 'Name is too long.';
        } else if (name === 'email') {
            if (!value) msg = 'Please enter your email address.';
            else if (!validEmail(value)) msg = 'Please enter a valid email address.';
        } else if (name === 'phone') {
            if (value && value.replace(/[^0-9]/g, '').length > 15) msg = 'Please enter a valid phone number.';
        } else if (name === 'subject') {
            if (!value) msg = 'Please enter a subject.';
            else if (value.length > 200) msg = 'Subject is too long.';
        } else if (name === 'message') {
            if (!value) msg = 'Please enter your message.';
            else if (value.length > MAX_MESSAGE) msg = 'Message must be ' + MAX_MESSAGE + ' characters or fewer.';
        }

        field.classList.remove('cu-invalid', 'cu-valid');
        if (msg) {
            errorEl.textContent = msg;
            field.classList.add('cu-invalid');
            return false;
        }
        if (value) field.classList.add('cu-valid');
        return true;
    }

    if (form) {
        form.querySelectorAll('.cu-input').forEach(function (input) {
            input.addEventListener('blur', function () { validateField(input); });
            input.addEventListener('input', function () {
                var field = input.closest('.cu-field');
                if (field && field.classList.contains('cu-invalid')) validateField(input);
            });
        });

        if (messageInput && counter) {
            var updateCounter = function () {
                counter.textContent = messageInput.value.length + ' / ' + MAX_MESSAGE;
            };
            messageInput.addEventListener('input', updateCounter);
            updateCounter();
        }
    }

    /* ==========================================
       AJAX SUBMIT (preserve values on failure)
       ========================================== */
    var submitBtn = document.getElementById('cuSubmit');
    var successBox = document.getElementById('cuSuccess');
    var resetBtn = document.getElementById('cuSuccessReset');

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();

            var firstInvalid = null;
            form.querySelectorAll('.cu-input').forEach(function (input) {
                if (!validateField(input)) {
                    if (!firstInvalid) firstInvalid = input;
                }
            });

            if (firstInvalid) {
                firstInvalid.focus();
                return;
            }

            if (submitBtn) {
                submitBtn.classList.add('cu-loading');
                submitBtn.disabled = true;
            }

            var data = new FormData(form);

            fetch(form.getAttribute('action'), {
                method: 'POST',
                body: data,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            })
            .then(function (res) { return res.json().then(function (json) { return { ok: res.ok, json: json }; }); })
            .then(function (result) {
                if (result.ok && result.json && result.json.ok) {
                    form.hidden = true;
                    if (successBox) successBox.hidden = false;
                    successBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
                } else if (result.json && result.json.errors) {
                    Object.keys(result.json.errors).forEach(function (fieldName) {
                        var input = form.querySelector('[name="' + fieldName + '"]');
                        if (input) {
                            var field = input.closest('.cu-field');
                            var errorEl = field ? field.querySelector('.cu-field-error') : null;
                            if (field && errorEl) {
                                field.classList.remove('cu-valid');
                                field.classList.add('cu-invalid');
                                errorEl.textContent = result.json.errors[fieldName];
                            }
                        }
                    });
                    var firstErr = form.querySelector('.cu-invalid .cu-input');
                    if (firstErr) firstErr.focus();
                } else {
                    alert('Something went wrong. Please try again.');
                }
            })
            .catch(function () {
                alert('Network error. Please check your connection and try again.');
            })
            .finally(function () {
                if (submitBtn) {
                    submitBtn.classList.remove('cu-loading');
                    submitBtn.disabled = false;
                }
            });
        });
    }

    if (resetBtn && form) {
        resetBtn.addEventListener('click', function () {
            form.reset();
            form.querySelectorAll('.cu-field').forEach(function (f) {
                f.classList.remove('cu-invalid', 'cu-valid');
            });
            if (counter) counter.textContent = '0 / ' + MAX_MESSAGE;
            successBox.hidden = true;
            form.hidden = false;
            form.scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    }

    /* ==========================================
       ACCORDION (Quick FAQs)
       ========================================== */
    var faqItems = document.querySelectorAll('.cu-faq-item');
    faqItems.forEach(function (item) {
        var trigger = item.querySelector('.cu-faq-trigger');
        var panel = item.querySelector('.cu-faq-panel');

        trigger.addEventListener('click', function () {
            var isActive = item.classList.contains('active');

            if (isActive) {
                closeFaq(item);
            } else {
                faqItems.forEach(function (other) {
                    if (other.classList.contains('active')) closeFaq(other);
                });
                openFaq(item);
            }
        });

        function openFaq(it) {
            var t = it.querySelector('.cu-faq-trigger');
            var p = it.querySelector('.cu-faq-panel');
            it.classList.add('active');
            t.setAttribute('aria-expanded', 'true');
            p.hidden = false;
            p.style.maxHeight = p.scrollHeight + 'px';
        }

        function closeFaq(it) {
            var t = it.querySelector('.cu-faq-trigger');
            var p = it.querySelector('.cu-faq-panel');
            it.classList.remove('active');
            t.setAttribute('aria-expanded', 'false');
            p.style.maxHeight = '0px';
            p.addEventListener('transitionend', function handler() {
                if (!it.classList.contains('active')) p.hidden = true;
                p.removeEventListener('transitionend', handler);
            });
        }
    });

    /* ==========================================
       BUTTON RIPPLE
       ========================================== */
    document.querySelectorAll('[data-cu-ripple]').forEach(function (btn) {
        btn.addEventListener('click', function (e) {
            var rect = btn.getBoundingClientRect();
            var size = Math.max(rect.width, rect.height);
            var ripple = document.createElement('span');
            ripple.className = 'cu-ripple';
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
            ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
            btn.appendChild(ripple);
            setTimeout(function () { ripple.remove(); }, 600);
        });
    });
});
