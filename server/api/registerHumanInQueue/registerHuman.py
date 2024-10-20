from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
from dataclasses import dataclass
import json
import os

"""
QUEUE_I - Current database for queue status (id PRIMARY KEY, number INTEGER, login TEXT NOT NULL, timestamp INTEGER)
"""

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def import_database():
    import sys
    sys.path.insert(0, os.path.join(ROOT_DIR, "server", "database"))

import_database()
import database

URL_FOR_REGISTER_PAGE = "/register-human-in-queue"
REGISTER_PAGE_PATH = os.path.join(ROOT_DIR, "client", "register-human-in-queue")

@dataclass
class UserData:
    login: str
    queueId: int

class RegisterHumanHandler:
    indexUrl: str = URL_FOR_REGISTER_PAGE
    scriptUrl: str = URL_FOR_REGISTER_PAGE+"/script.js"
    createRecordUrl: str = URL_FOR_REGISTER_PAGE+"/create-record"
    checkLoginUrl: str = URL_FOR_REGISTER_PAGE+"/check-login"
        
    def loadIndex(self):
        return FileResponse(REGISTER_PAGE_PATH+"/index.html")

    def loadScript(self):
        return FileResponse(REGISTER_PAGE_PATH+"/script.js")

    def checkLogin(self, login: str, queueId: str):
        queueTable = database.DatabaseTable(ROOT_DIR + "/server/api/QUEUES.db", "Q"+queueId)
        queueTable.create("login TEXT, number TEXT, queueId TEXT")
        logins = queueTable.get(("login", ), "login = ?", (login, ))
        queueTable.endWork()
        
        if(len(logins) == 0):
            return JSONResponse(status_code=200, content={"message":"ok"})
            
        return JSONResponse(status_code=200, content={"message":"bebebe"})
    
    def createRecord(self, userData: UserData):
        userData = json.loads(userData)
        queueTable = database.DatabaseTable(ROOT_DIR + "/server/api/QUEUES.db", "Q"+userData["queueId"])
        queueTable.create("login TEXT, number TEXT, queueId number")
        number = len(queueTable.get("*", )) + 1
        queueTable.insert(("login", "number"), (userData["login"], number))
        queueTable.endWork()