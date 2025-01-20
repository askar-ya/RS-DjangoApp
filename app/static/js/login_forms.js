let email = document.querySelector('#id_email');
if (email) {
    email.placeholder = 'E-mail'
}


let username = document.querySelector('#id_username');
if (username) {
    let currentUrl = window.location.href;
    if (currentUrl.includes('login')) {
        username.placeholder = 'E-mail'
    }
    else {
        username.placeholder = 'Имя'
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

    let InputField = target.parentElement.querySelector('input');

    if (InputField.getAttribute('type') === 'password') {
        target.classList.add('view');
        InputField.setAttribute('type', 'text');
    } else {
        target.classList.remove('view');
        InputField.setAttribute('type', 'password');
    }
    return false;
}