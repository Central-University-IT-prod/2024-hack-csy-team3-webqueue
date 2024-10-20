from fastapi import File
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def importDatabase():
    import sys
    sys.path.insert(0, ROOT_DIR + "\\server\\database")

importDatabase()
import database

DIR = os.path.dirname(os.path.abspath(__file__))

class LastQueueId:
    def __init__(self, filepath: str):
        self.__file = filepath

    def create(self):
        if(not os.path.exists(self.__file)):
            with open(self.__file, "w") as file:
                pass

    def get(self):
        file = open(self.__file, "r")
        lastId = file.read()
        file.close()
        if(len(lastId) == 0):
            file = open(self.__file, "w")
            file.write("0")
            file.close()
            return 0
        else:
            return int(lastId)

    def update(self, newValue: int):
        with open(self.__file, "w") as file:
            pass

        file = open(self.__file, "w")
        file.write(str(newValue))
        file.close()

class AdminCreaterEventsHandler:
    indexUrl: str = "/admin-create-events-page"
    scriptUrl: str = "/admin-create-events-page/script.js"
    styleUrl: str = "/admin-create-events-page/style.css"
    getQueueIdUrl: str = "/admin-create-events-page/get-event-id"
    loadPictureUrl: str = "/admin-create-events-page/load-event-picture"

    def __init__(self):
        self.lastId = LastQueueId(DIR + "/lastQueueId.txt")
        self.lastId.create()

    def loadIndex(self):
        return FileResponse(ROOT_DIR + "/client/admin-create-events-page/index.html")

    def loadStyle(self):
        return FileResponse(ROOT_DIR + "/client/admin-create-events-page/style.css")

    def loadScript(self):
        return FileResponse(ROOT_DIR + "/client/admin-create-events-page/script.js")

    def getQueueId(self, eventName: str, description: str, avgTime: int):
        queueId = self.lastId.get() + 1
        self.lastId.update(queueId)

        queueTable = database.DatabaseTable(ROOT_DIR + "/server/api/QUEUES.db", "QUEUES_INFORMATION")
        queueTable.create("number PRIMARY KEY, queueId INTEGER, eventName TEXT NOT NULL, description TEXT NOT NULL, avgTime TEXT")
        queueTable.insert(("queueId", "eventName", "description", "avgTime",) , (queueId, eventName, description, avgTime, ))
        queueTable.endWork()

        return JSONResponse(status_code=200, content={"message":queueId})