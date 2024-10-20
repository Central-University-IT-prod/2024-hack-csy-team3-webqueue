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

ADMIN_IN_QUEUE_DIR = ROOT_DIR + "/client/admin-in-queue-page"
ADMIN_IN_QUEUE_URL = "/admin-in-queue-page"

class AdminInQueueHandler:
    indexUrl: str = ADMIN_IN_QUEUE_URL
    scriptUrl: str = ADMIN_IN_QUEUE_URL + "/script.js"
    styleUrl: str = ADMIN_IN_QUEUE_URL + "/style.css"
    getMembersUrl: str = ADMIN_IN_QUEUE_URL + "/get-members"
    deleteMembersUrl: str = ADMIN_IN_QUEUE_URL + "/delete-members"

    def loadIndex(self):
        return FileResponse(ADMIN_IN_QUEUE_DIR + "/index.html")
    
    def loadScript(self):
        return FileResponse(ADMIN_IN_QUEUE_DIR + "/script.js")

    def loadStyle(self):
        return FileResponse(ADMIN_IN_QUEUE_DIR + "/style.css")

    def getMembers(self, queueId: str):
        queueTable = database.DatabaseTable(ROOT_DIR + "/server/api/QUEUES.db", "Q"+queueId)

        data = queueTable.get(("login", "number", ))
        queueTable.endWork()
        data = self.__bubbleSort(data)

        return JSONResponse(status_code=200, content={"message":json.dumps(data)})

    def __bubbleSort(self, data: 'list[tuple[str]]'):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if(data[j][1] > data[j+1][1]):
                    data[j], data[j+1] = data[j+1], data[j]

        return data

    def deleteMembers(self, members: 'list[str]'):
        members = json.loads(members)
        queueId = members[-1]
        members = members[:len(members)-1]
        queueTable = database.DatabaseTable(ROOT_DIR + "/server/api/QUEUES.db", "Q"+queueId)
        
        for memb in members:
            numb = queueTable.get(("number", ), "login = ?", (memb, ))[0][0]
            bigger = queueTable.get(("login", "number", ), "number > ?", (numb, ))
            for log in bigger:
                queueTable.update("number", "login", (int(log[1])-1, log[0], ))
        
            queueTable.delete("login", memb)
        
        queueTable.endWork()