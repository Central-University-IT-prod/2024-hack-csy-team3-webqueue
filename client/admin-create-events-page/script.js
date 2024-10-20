const inputEventName = document.getElementById("eventName");
const inputDescription = document.getElementById("description");
const inputTime = document.getElementById("avgTimeOnOnePerson");
const createButton = document.getElementById("createButton");
const URL_TO_GET_NEW_EVENT_ID = "/admin-create-events-page/get-event-id?data=";

function sendEventInformation(){
    let xhr = new XMLHttpRequest();
    const json = {
        eventName: inputEventName.value,
        description: inputDescription.value,
        avgTime: inputTime.value
    };

    xhr.open("GET", URL_TO_GET_NEW_EVENT_ID+json.eventName+"+"+json.description+"+"+json.avgTime, false);
    xhr.send();
    if(xhr.status != 200){
        alert("Произошла ошибка, пожалуйста попробуйте ещё раз.");
    }else{
        const queueId = JSON.parse(xhr.response)["message"];
        alert("Мероприятие создано");
    }
}

createButton.addEventListener("click", (evt) => {
    evt.stopPropagation();
    sendEventInformation();
});