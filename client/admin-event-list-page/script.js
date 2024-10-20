const URL_PICTURES_BASEDATA = "/pictures/";
const BASE_URL_PICTURE = "/base-event-picture.png";
const URL_TO_GET_USER_EVENT_LIST = "/admin-event-list-page/get-user-event-list";

function getEventNamesInnerHtml(){
    let xhr = new XMLHttpRequest();
    xhr.open("GET", URL_TO_GET_USER_EVENT_LIST, false);
    xhr.send();
    if(xhr.status != 200){
        return "Извините, на данный момент данный сервис не работает.";
    }else{
        let response = JSON.parse(JSON.parse(xhr.response)["message"]);
        let innerHtml = '<div id="events" class="events-container"></div>';
        for(const event of response){
            innerHtml = innerHtml + getEventHtml(event);
        }
        return innerHtml;
    }
}

function getEventHtml(event){
    return '<div class="button-overlay">\
    <img class="mer1" src="/admin-event-list-page/picture.jpg"  alt="">\
    <div class="Stand"><h2 class="name">'+event[0]+'</h2></div>\
    <button class="zapicaca" onclick="onClickButton('+event[1]+')">ПРОСМОТРЕТЬ ОЧЕРЕДЬ</button>\
    </div>';
}

function onClickButton(id){
    window.location.href = '/admin-in-queue-page?queueId='+id
}

const eventList = document.getElementsByClassName("container")[0];
eventList.innerHTML = getEventNamesInnerHtml();