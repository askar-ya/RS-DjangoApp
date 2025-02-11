function PopUp(window) {
    console.log('.popUp .' + window);
    let popUp = document.querySelector('.popUp.' + window);
    console.log(popUp)
    popUp.style.display = 'block'
}

function PopupClose(){
    let window = this
    window.style.display = 'none';
}