

function reelDetailed() {

    let reelBox = this.parentElement.parentElement;
    let index_reel = reelBox.id;
    console.log(index_reel);
    console.log(stored[index_reel]['id']);


    let current_play_video = document.querySelector('.current_play_video');

        if (current_play_video) {

          if (!current_play_video.paused) {
            let current_play_video_btn_img = current_play_video.parentElement.parentElement.querySelector('.btn-box img');
            current_play_video_btn_img.style.visibility = 'visible';
            current_play_video.pause();
            current_play_video.classList.remove("current_play_video");
          }
        }

    let popUp = document.querySelector('.reels-detailed')
    popUp.querySelector('#video').poster = '/static/posters/' + stored[index_reel]['id'] + '.jpg';
    popUp.querySelector('#video source').src = '/static/video/' + stored[index_reel]['id'] + '.mp4';
    popUp.querySelector('.name').innerText = stored[index_reel]['author']['nick'];
    popUp.querySelector('.metrics .reels-count h4').innerText = stored[index_reel]['author']['reels_count'];
    popUp.querySelector('.metrics .subs h4').innerText = stored[index_reel]['author']['subscribers'];
    popUp.querySelector('.metrics .sub h4').innerText = stored[index_reel]['author']['subscriptions'];
    popUp.querySelector('.author .about').innerText = stored[index_reel]['author']['description'];
    popUp.querySelector('.reels-info .about').innerText = stored[index_reel]['description'];

    popUp.querySelector('.video-box .btn-box img').style.visibility = 'visible';

    popUp.classList.remove("popUpClose");
    popUp.classList.add("popUpOpen");
}

function reelDetailedClose() {
    let current_play_video = document.querySelector('.current_play_video');

    if (current_play_video) {

      if (!current_play_video.paused) {
        let current_play_video_btn_img = current_play_video.parentElement.parentElement.querySelector('.btn-box img');

        current_play_video_btn_img.style.visibility = 'hidden';
        current_play_video.pause();
        current_play_video.classList.remove("current_play_video");
      }
    }

    let popUp = document.querySelector('.reels-detailed');
    popUp.querySelector('.video-box .btn-box img').style.visibility = 'hidden';
    popUp.classList.add("popUpClose");
    popUp.classList.remove("popUpOpen");
}