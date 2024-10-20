from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

def importDatabase():
    import sys
    sys.path.insert(0, ROOT_DIR + '\\server\\database')

importDatabase()
import database

ADMIN_LOGIN_PAGE: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) + "/client/admin-login-page"
URL_ADMIN_LOGIN = "/admin-login-page"

class AdminLoginHandler:
    indexUrl: str = URL_ADMIN_LOGIN
    scriptUrl: str = URL_ADMIN_LOGIN + "/script.js"
    checkDataUrl: str = URL_ADMIN_LOGIN + "/check-data"

    def loadIndex(self):
        return FileResponse(ADMIN_LOGIN_PAGE+"/index.html")

    def loadScript(self):
        return FileResponse(ADMIN_LOGIN_PAGE+"/script.js")

    def checkData(self, login: str, password: str):
        adminTable = database.DatabaseTable(ROOT_DIR + "/server/api/admins.db", "ADMINS")
        results = adminTable.get(("login", "password", ), "login = ?", (login, ))[0]
        adminTable.endWork()
        print(results)
        if(len(results) != 0):
            print(results)
            if(results[1] == password):
                return JSONResponse(status_code=200, content={"message":"ok"})
        
        return JSONResponse(status_code=200, content={"message":"pizdec"})