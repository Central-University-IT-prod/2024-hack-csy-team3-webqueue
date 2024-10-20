from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def importDatabase():
    import sys
    sys.path.insert(0, ROOT_DIR + '\\server\\database')

importDatabase()
import database

URL_WAIT_PAGE = "/wait-page"
WAIT_PAGE_DIR = ROOT_DIR + "\\client\\wait-page"

class WaitPageHandler:
    indexUrl: str = URL_WAIT_PAGE
    scriptUrl: str = URL_WAIT_PAGE + "/script.js"
    styleUrl: str = URL_WAIT_PAGE + "/style.css"
    clockUrl: str = URL_WAIT_PAGE + "/clock.png"
    logotipUrl: str = URL_WAIT_PAGE + "/logotip.png"
    getQueueStateUrl: str = URL_WAIT_PAGE + "/get-queue-state"

    def loadIndex(self):
        return FileResponse(WAIT_PAGE_DIR + "\\index.html")

    def loadScript(self):
        return FileResponse(WAIT_PAGE_DIR + "\\script.js")

    def loadStyle(self):
        return FileResponse(WAIT_PAGE_DIR + "\\style.css")

    def loadClock(self):
        return FileResponse(WAIT_PAGE_DIR + "\\clock.png")

    def loadLogotip(self):
        return FileResponse(WAIT_PAGE_DIR + "\\logotip.png")

    def getQueueState(self, login, queueId):
        informationTable = database.DatabaseTable(ROOT_DIR + "\\server\\api\\QUEUES.db", "QUEUES_INFORMATION")
        queueTable = database.DatabaseTable(ROOT_DIR + "\\server\\api\\QUEUES.db", "Q"+queueId)

        avgTime = informationTable.get(("avgTime", ), "queueId = ?", (queueId, ))[0][0]
        informationTable.endWork()

        number = queueTable.get(("number", ), "login = ?", (login, ))[0][0]
        queueTable.endWork()

        timeToWait = int(avgTime) * (int(number)-1)
        response = [number, timeToWait]

        return JSONResponse(status_code=200, content={"message":json.dumps(response)})