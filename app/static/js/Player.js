function startstop() {

    let btn_box = this;
    let btn_img = btn_box.querySelector('img');
    let video = this.parentElement.querySelector('#video');

    console.log(video);

    if (video.paused) {
        let current_play_video = document.querySelector('.current_play_video');

        if (current_play_video) {

          if (!current_play_video.paused) {
            let current_play_video_btn_img = current_play_video.parentElement.querySelector('.btn-box img');
            current_play_video_btn_img.style.visibility = 'visible';
            current_play_video.pause();
            current_play_video.classList.remove("current_play_video");
          }
        }

        video.classList.add("current_play_video");
        video.play();
        btn_img.style.visibility = 'hidden';
    }
    else {
        video.pause();
        video.classList.remove('current_play_video');
        btn_img.style.visibility = 'visible';
    }
}
