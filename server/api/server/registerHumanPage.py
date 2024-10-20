from fastapi import Body
import sys
import os

# Determine the root directory using forward slashes
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    sys.path.insert(0, path)

# Import the registerHumanInQueue module
import_module(os.path.join(API_DIR, "registerHumanInQueue"))
import registerHuman

REGISTER_HUMAN_PAGE = registerHuman.RegisterHumanHandler()
def setRegisterHumanPage(SERVER):
    @SERVER.get(REGISTER_HUMAN_PAGE.indexUrl)
    async def loadRegisterPageIndex():
        return REGISTER_HUMAN_PAGE.loadIndex()

    @SERVER.get(REGISTER_HUMAN_PAGE.scriptUrl, include_in_schema=False)
    async def loadRegisterPageScript():
        return REGISTER_HUMAN_PAGE.loadScript()

    @SERVER.post(REGISTER_HUMAN_PAGE.createRecordUrl, summary="hhh")
    async def createRecord(userData = Body()):
        return REGISTER_HUMAN_PAGE.createRecord(userData)

    @SERVER.get(REGISTER_HUMAN_PAGE.checkLoginUrl)
    async def checkLogin(login: str, queueId: str):
        return REGISTER_HUMAN_PAGE.checkLogin(login, queueId)
