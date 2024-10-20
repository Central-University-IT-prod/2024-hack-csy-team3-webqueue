const inputLogin = document.getElementById("login");
const inputPassword = document.getElementById("password");
const inputButton = document.getElementById("input-button");

const URL_TO_CHECK_ADMIN = "/admin-login-page/check-data";

class UserData{
    collect(){
        this.login = this.getLogin();
        this.password = this.getPassword();
    }
    getLogin(){
        return inputLogin.value;
    }
    getPassword(){
        return inputPassword.value;
    }
    clearLogin(){
        inputLogin.value = "";
    }
    clearPassword(){
        inputPassword.value = "";
    }
}

function isNotNull(userData){
    return userData.login != "" && userData.password != "";
}

function checkData(userData){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_CHECK_ADMIN + "?data=" + userData.login + "+" + userData.password, false);
    xhr.send();
    if(xhr.status != 200){
        alert("Произошла ошибка, попробуйте ещё раз");
    }else{
        const response = JSON.parse(xhr.response);
        if(response["message"] == "ok"){
            window.location.href = "/admin-event-list-page/"
        }else{
            alert("Введённые данные неверны, попробуйте ещё раз");
            userData.clearLogin();
            userData.clearPassword();
        }
    }
}

const userData = new UserData();
inputButton.addEventListener("click", (evt) => {
    userData.collect();
    if(isNotNull(userData)){
        checkData(userData);
    }else{
        alert("Имеются незаполненные поля");
    }
})