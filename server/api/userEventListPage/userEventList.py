from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
import json
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def importDatabase():
    import sys
    sys.path.insert(0, ROOT_DIR + '\\server\\database')

importDatabase()
import database

class UserEventListHandler:
    indexUrl: str = "/"
    scriptUrl: str = "/script.js"
    pictureUrl: str = "/picture.jpg"
    styleUrl: str = "/style.css"
    getUserEventListUrl: str = "/get-user-event-list"

    def loadIndex(self):
        return FileResponse(ROOT_DIR + "\\client\\user-event-list-page\\index.html")

    def loadScript(self):
        return FileResponse(ROOT_DIR + "\\client\\user-event-list-page\\script.js")

    def loadPicture(self):
        return FileResponse(ROOT_DIR + "\\client\\user-event-list-page\\picture.jpg")

    def loadStyle(self):
        return FileResponse(ROOT_DIR + "\\client\\user-event-list-page\\style.css")

    def getUserEventList(self):
        queueTable = database.DatabaseTable(ROOT_DIR + "\\server\\api\\QUEUES.db", "QUEUES_INFORMATION")
        eventNames = queueTable.get(("eventName", "queueId", "description"))

        for i in range(len(eventNames)):
            eventNames[i] = [eventNames[i][0], eventNames[i][1], eventNames[i][2]]

        queueTable.endWork()
        return JSONResponse(status_code=200, content={"message":json.dumps(eventNames)})