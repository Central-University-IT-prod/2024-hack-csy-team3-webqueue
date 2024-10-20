from fastapi import Body
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = ROOT_DIR + "\\server"
API_DIR = SERVER_DIR + "\\api"

def importModule(path: str):
    sys.path.insert(0, path)

importModule(API_DIR + "\\registerHumanInQueue")
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
