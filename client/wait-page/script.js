const currentUrl = new URL(window.location.href);
const LOGIN = currentUrl.searchParams.get("login");
const QUEUE_ID = currentUrl.searchParams.get("queueId");
const URL_TO_GET_QUEUE_STATE = "/wait-page/get-queue-state";
const URL_TO_GET_USER_EVENT_LIST = "/get-user-event-list";
const cancelButton = document.getElementById("cancel-button")
const URL_TO_DELETE_QUEUE_MEMBERS = "/admin-in-queue-page/delete-members"

function setEventName(){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_GET_USER_EVENT_LIST, false);
    xhr.send();
    let response = JSON.parse(JSON.parse(xhr.response)["message"]);
    let eventName = "";
    for(const event of response){
        if(event[1] == QUEUE_ID){
            eventName = event[0];
            break;
        }
    }

    let eventNameHtml = document.getElementById("title1");
    eventNameHtml.innerHTML = eventName;
}

function getQueueState(){
    let numberInQueue;
    let waitTime;

    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_GET_QUEUE_STATE+"?login="+LOGIN+"&queueId="+QUEUE_ID, false);
    xhr.send();
    if(xhr.status != 200){
        numberInQueue = "не определено";
        waitTime = "не определено";
    }else{
        let response = JSON.parse(JSON.parse(xhr.response)["message"]);
        numberInQueue = response[0];
        waitTime = response[1];
    }
    if(waitTime == 0){
        waitTime = "Подойдите к стойке";
    }
    console.log(numberInQueue, waitTime);
    return [numberInQueue, waitTime];
}

setEventName();

function deleteFromDatabase(){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", URL_TO_DELETE_QUEUE_MEMBERS, false);
    ARRAY_TO_DELETE = [LOGIN];
    ARRAY_TO_DELETE.push(QUEUE_ID);
    xhr.send(JSON.stringify(ARRAY_TO_DELETE));
    ARRAY_TO_DELETE = new Array();
    if(xhr.status != 200){
        alert("Будьте добры, повторите попытку");
    }else{
        alert("Вы вышли из очереди");
        document.location.href = "/";
    }
}

const information = getQueueState();
let placeInQueue = document.getElementById("placeInQueue");
placeInQueue.innerHTML = '<p align="center" id="placeInQueue">'+information[0]+'</p>';
    
let timeToWait = document.getElementById("timeToWait");
timeToWait.innerHTML = '<p align="center" id="timeToWait">'+information[1]+'</p>';

cancelButton.addEventListener("click", () => {
    deleteFromDatabase();
})

setInterval(() => {
    const information = getQueueState();
    let placeInQueue = document.getElementById("placeInQueue");
    placeInQueue.innerHTML = '<p align="center" id="placeInQueue">'+information[0]+'</p>';
    
    let timeToWait = document.getElementById("timeToWait");
    timeToWait.innerHTML = '<p align="center" id="timeToWait">'+information[1]+'</p>';

}, 5000);