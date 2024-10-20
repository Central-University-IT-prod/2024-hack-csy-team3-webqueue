import sys
import os

# Determine the root directory using forward slashes
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    sys.path.insert(0, path)

# Import the adminLoginPage module
import_module(os.path.join(API_DIR, "adminLoginPage"))
import adminLogin

ADMIN_LOGIN_PAGE = adminLogin.AdminLoginHandler()

def setAdminLoginPage(SERVER):
    @SERVER.get(ADMIN_LOGIN_PAGE.indexUrl)
    async def loadAdminLoginPageIndex():
        return ADMIN_LOGIN_PAGE.loadIndex()

    @SERVER.get(ADMIN_LOGIN_PAGE.scriptUrl)
    async def loadAdminLoginPageScript():
        return ADMIN_LOGIN_PAGE.loadScript()

    @SERVER.get(ADMIN_LOGIN_PAGE.checkDataUrl)
    async def checkData(data: str):
        login, password = data.split(" ")[0], data.split(" ")[1]
        return ADMIN_LOGIN_PAGE.checkData(login, password)