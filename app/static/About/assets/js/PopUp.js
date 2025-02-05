function PopUp(window) {
    console.log('.pop-up .' + window);
    let popUp = document.querySelector('.popUp.' + window)
    popUp.style.display = 'block'
}

function PopupClose(){
    let window = this
    window.style.display = 'none';
}