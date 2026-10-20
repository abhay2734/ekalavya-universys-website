
document.addEventListener("DOMContentLoaded", function () {
    function toggleVideoFields(videoType, clearInactiveFields) {
        const row = videoType.closest("tr") || videoType.closest(".inline-related");
        if (!row) return;

        const fields = {
            youtube: row.querySelector('[name$="-youtube_url"], #id_youtube_url'),
            upload: row.querySelector('[name$="-uploaded_video"], #id_uploaded_video'),
            other: row.querySelector('[name$="-other_url"], #id_other_url')
        };

        Object.entries(fields).forEach(function ([type, field]) {
            if (!field) return;

            const shouldEnable = videoType.value === type;

            if (!shouldEnable && clearInactiveFields) {
                field.value = "";
            }

            field.disabled = !shouldEnable;
        });
    }

    function initializeVideoType(videoType) {
        toggleVideoFields(videoType, false);

        videoType.addEventListener("change", function () {
            toggleVideoFields(videoType, true);
        });
    }

    function initializeRows(container) {
        container.querySelectorAll(
            '[name="video_type"], [name$="-video_type"], #id_video_type'
        ).forEach(function (videoType) {
            if (videoType.dataset.videoToggleInitialized === "true") return;

            videoType.dataset.videoToggleInitialized = "true";
            initializeVideoType(videoType);
        });
    }

    initializeRows(document);

    document.addEventListener("formset:added", function (event) {
        initializeRows(event.target);
    });
});
