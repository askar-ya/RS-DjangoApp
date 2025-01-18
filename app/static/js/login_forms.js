let email = document.querySelector('#id_email');
if (email) {
    email.placeholder = 'email'
}


let username = document.querySelector('#id_username');
if (username) {
    let currentUrl = window.location.href;
    if (currentUrl.includes('login')) {
        username.placeholder = 'email'
    }
    else {
        username.placeholder = 'username'
    }

}


let pass = document.querySelector('#id_password');
if (pass) {
    pass.placeholder = 'Пароль'
}

let pass1 = document.querySelector('#id_password1');
if (pass1) {
    pass1.placeholder = 'Пароль'
}

let pass2 = document.querySelector('#id_password2');
if (pass2) {
    pass2.placeholder = 'Подтверждение пароля'
}


function show_hide_password(target){
    let input = document.querySelector('.input-box.pass input');
    if (input.getAttribute('type') == 'password') {
        target.classList.add('view');
        input.setAttribute('type', 'text');
    } else {
        target.classList.remove('view');
        input.setAttribute('type', 'password');
    }
    return false;
}