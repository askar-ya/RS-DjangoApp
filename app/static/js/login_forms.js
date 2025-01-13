let username = document.querySelector('.input-box.username input');
username.placeholder = 'Имя пользователя'

let pass = document.querySelector('.input-box.pass input');
pass.placeholder = 'Пароль'

function show_hide_password(target){
    var input = document.querySelector('.input-box.pass input');
    if (input.getAttribute('type') == 'password') {
        target.classList.add('view');
        input.setAttribute('type', 'text');
    } else {
        target.classList.remove('view');
        input.setAttribute('type', 'password');
    }
    return false;
}