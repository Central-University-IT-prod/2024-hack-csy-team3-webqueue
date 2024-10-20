const inputLogin = document.getElementById("login");
const registerButton = document.getElementById("register-button");
const URL_FOR_CREATE_ACCOUNT = "/register-human-in-queue/create-record"; //хакеры идите в жопу
const URL_FOR_CHECK_LOGIN = "/register-human-in-queue/check-login"
const URL_TO_GET_USER_EVENT_LIST = "/get-user-event-list";
const currentUrl = new URL(window.location.href)

const QUEUE_ID = currentUrl.searchParams.get("queueId");

//извлечь из url queueId

class UserData{
    collect(){
        this.login = this.getLogin();
    }
    getLogin(){
        return inputLogin.value;
    }
    clearLogin(){
        inputLogin.value = "";
    }
}

function writeDescription(){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_GET_USER_EVENT_LIST, false);
    xhr.send();
    let response = JSON.parse(JSON.parse(xhr.response)["message"]);
    let description = "";
    for(const event of response){
        if(event[1] == QUEUE_ID){
            description = event[2];
            break;
        }
    }

    let descriptionHtml = document.getElementById("description");
    descriptionHtml.innerHTML = '<div id="description">'+description+'</div>';
}

function checkLogin(login){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_FOR_CHECK_LOGIN + "?login="+login+"&queueId="+QUEUE_ID, false);
    xhr.send();
    if(xhr.status != 200){
        alert("Произошла внезапная ошибка! Попробуйте снова отправить данные!")
    }else{
        if(JSON.parse(xhr.response)["message"] != "ok"){
            alert("Человек с таким логином уже есть, введите новый.");
            return false;
        }else{
            return true;
        }
    }
}

function createRecord(userData){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", URL_FOR_CREATE_ACCOUNT, false);
    const jsonUserData = JSON.stringify({
        login: userData.login,
        queueId: QUEUE_ID,
    });
    xhr.send(jsonUserData);
    if(xhr.status != 200){
        alert("Произошла внезапная ошибка! Попробуйте снова отправить данные!")
    }else{
        window.location.href = "/wait-page?login=" + userData.login+"&queueId="+QUEUE_ID;     
    }
}

writeDescription();
const userData = new UserData();
registerButton.addEventListener("click", (evt) => {
    userData.collect();
    if(userData.login == ""){
        alert("Пожалуйста, введите свой логин.");
    }else if(checkLogin(userData.login)){
        createRecord(userData);
    }else{
        userData.clearLogin();
    }
});