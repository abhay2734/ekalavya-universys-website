document.addEventListener("DOMContentLoaded", function () {

    function toggleVideoFields() {

        const videoType = document.getElementById("id_video_type");
        const youtubeField = document.getElementById("id_youtube_url");
        const uploadField = document.getElementById("id_uploaded_video");

        if (!videoType) return;

        if (videoType.value === "youtube") {

            youtubeField.disabled = false;
            uploadField.disabled = true;

        }

        else if (videoType.value === "upload") {

            youtubeField.disabled = true;
            uploadField.disabled = false;

        }

        else {

            youtubeField.disabled = false;
            uploadField.disabled = false;

        }

    }

    const videoType = document.getElementById("id_video_type");

    if (videoType) {

        toggleVideoFields();

        videoType.addEventListener("change", toggleVideoFields);

    }

});