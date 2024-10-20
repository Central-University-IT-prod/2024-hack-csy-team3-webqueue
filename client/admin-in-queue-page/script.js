const URL_TO_GET_USER_EVENT_LIST = "/get-user-event-list";
const URL_TO_GET_QUEUE_MEMBERS = "/admin-in-queue-page/get-members"
const URL_TO_DELETE_QUEUE_MEMBERS = "/admin-in-queue-page/delete-members"
const QUEUE_ID = new URL(window.location.href).searchParams.get("queueId");
let ARRAY_TO_DELETE = new Array();
const deleteButton = document.getElementById("delete");

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

    let eventNameHtml = document.getElementById("event-name");
    eventNameHtml.innerHTML = '<h2 class="event-title" id="event-name">'+eventName+'</h2>';
}

function setQueueMembers(){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_GET_QUEUE_MEMBERS + "?queueId=" + QUEUE_ID, false);
    xhr.send();
    let response = JSON.parse(JSON.parse(xhr.response)["message"]);

    const containerHtml = document.getElementById("container1");
    let innerHTML = '<div class="queue-container" id="container1">';
    for(const member of response){
        innerHTML = innerHTML + getButtonHtml(member);
    }
    innerHTML = innerHTML + "</div>";
    containerHtml.innerHTML = innerHTML;
}

function getButtonHtml(member){
    return '<button class="queue-item" onclick="moveToBin(`' + member[0] + '`)">'+member[0]+'</button>'
}

function moveToBin(login){
    for(const i of ARRAY_TO_DELETE){
        if(i === login){
            return;
        }
    }
    ARRAY_TO_DELETE.push(login);
}

function deleteFromDatabase(){
    let xhr = new XMLHttpRequest();
    xhr.open("POST", URL_TO_DELETE_QUEUE_MEMBERS, false);
    ARRAY_TO_DELETE.push(QUEUE_ID);
    xhr.send(JSON.stringify(ARRAY_TO_DELETE));
    ARRAY_TO_DELETE = new Array();
    if(xhr.status != 200){
        alert("Будьте добры, повторите попытку");
    }else{
        setQueueMembers();
    }
}

setEventName();
setQueueMembers();

deleteButton.addEventListener("click", () => {
    deleteFromDatabase();
})
