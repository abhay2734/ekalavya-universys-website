document.addEventListener('DOMContentLoaded', function () {
    /* ==========================================
       SCROLL REVEAL - FADE UP
       Isolated so a failure here can never block
       the video modal from initialising.
       ========================================== */
    try {
        const revealTargets = document.querySelectorAll('.ft-fade-up');

        if (revealTargets.length) {
            const observerOptions = {
                root: null,
                rootMargin: '0px 0px -50px 0px',
                threshold: 0.1
            };

            const revealObserver = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('ft-revealed');
                        revealObserver.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            revealTargets.forEach(function (el) {
                revealObserver.observe(el);
            });
        }
    } catch (e) {
        /* Scroll reveal is non-critical; ignore failures. */
    }

    /* ==========================================
       GENERIC VIDEO MODAL
       Handles both YouTube and uploaded videos
       ========================================== */
    const modal = document.getElementById('ftVideoModal');
    const container = document.getElementById('ftVideoContainer');
    const closeBtn = document.getElementById('ftCloseVideo');

    if (!modal || !container || !closeBtn) return;

    const triggers = document.querySelectorAll('.ft-video-card');
    const state = { currentVideo: null, currentIframe: null };

    function closeVideoModal() {
        modal.style.display = 'none';
        modal.setAttribute('hidden', '');

        if (state.currentIframe) {
            state.currentIframe.src = 'about:blank';
        }

        if (state.currentVideo) {
            state.currentVideo.pause();
            state.currentVideo.removeAttribute('src');
            state.currentVideo.load();
        }

        container.innerHTML = '';
        state.currentVideo = null;
        state.currentIframe = null;
    }

    function parseYouTubeId(url) {
        if (!url) return null;
        const trimmed = url.trim();
        const patterns = [
            /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/shorts\/|m\.youtube\.com\/watch\?v=|youtube\.com\/v\/)([^&\s?#]+)/,
            /youtube\.com\/watch\?.*[?&]v=([^&\s?#]+)/
        ];
        for (let i = 0; i < patterns.length; i++) {
            const match = trimmed.match(patterns[i]);
            if (match) return match[1];
        }
        return null;
    }

    function openVideoModal(videoType, youtubeUrl, uploadUrl) {
        container.innerHTML = '';
        const trimmedYoutube = youtubeUrl ? youtubeUrl.trim() : '';
        const trimmedUpload = uploadUrl ? uploadUrl.trim() : '';

        if (videoType === 'youtube' && trimmedYoutube) {
            const videoId = parseYouTubeId(trimmedYoutube);
            if (videoId) {
                const iframe = document.createElement('iframe');
                iframe.src = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&rel=0';
                iframe.style.width = '100%';
                iframe.style.height = '100%';
                iframe.style.border = 'none';
                iframe.style.aspectRatio = '16 / 9';
                iframe.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
                iframe.referrerpolicy = 'strict-origin-when-cross-origin';
                iframe.allowFullscreen = true;
                container.appendChild(iframe);
                state.currentIframe = iframe;
            } else if (trimmedYoutube) {
                const video = document.createElement('video');
                video.src = trimmedYoutube;
                video.controls = true;
                video.autoplay = true;
                video.style.width = '100%';
                video.style.maxHeight = '80vh';
                video.style.background = '#000';
                container.appendChild(video);
                state.currentVideo = video;
            }
        } else if (videoType === 'upload' && trimmedUpload) {
            const video = document.createElement('video');
            video.src = trimmedUpload;
            video.controls = true;
            video.autoplay = true;
            video.style.width = '100%';
            video.style.maxHeight = '80vh';
            video.style.background = '#000';
            container.appendChild(video);
            state.currentVideo = video;
        }

        modal.removeAttribute('hidden');
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }

    triggers.forEach(function (trigger) {
        trigger.addEventListener('click', function () {
            const thumbFrame = trigger.querySelector('.ft-video-thumb-frame');
            const videoType = thumbFrame ? (thumbFrame.getAttribute('data-video-type') || 'youtube') : 'youtube';
            const youtubeUrl = thumbFrame ? (thumbFrame.getAttribute('data-youtube-url') || '') : '';
            const uploadUrl = thumbFrame ? (thumbFrame.getAttribute('data-upload-url') || '') : '';
            openVideoModal(videoType, youtubeUrl, uploadUrl);
        });
    });

    closeBtn.addEventListener('click', function () {
        closeVideoModal();
        document.body.style.overflow = '';
    });

    modal.addEventListener('click', function (e) {
        if (e.target === modal) {
            closeVideoModal();
            document.body.style.overflow = '';
        }
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && modal.style.display === 'flex') {
            closeVideoModal();
            document.body.style.overflow = '';
        }
    });
});
