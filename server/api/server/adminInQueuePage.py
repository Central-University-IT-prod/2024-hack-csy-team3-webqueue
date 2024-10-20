from fastapi import Body
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = ROOT_DIR + "\\server"
API_DIR = SERVER_DIR + "\\api"

def importModule(path: str):
    sys.path.insert(0, path)

importModule(API_DIR + "\\adminInQueuePage")
import adminInQueue

adminInQueueHandler = adminInQueue.AdminInQueueHandler()

def setAdminInQueuePage(SERVER):
    @SERVER.get(adminInQueueHandler.indexUrl)
    async def loadAdminInQueueHandlerIndex():
        return adminInQueueHandler.loadIndex()

    @SERVER.get(adminInQueueHandler.scriptUrl)
    async def loadAdminInQueueHandlerScript():
        return adminInQueueHandler.loadScript()

    @SERVER.get(adminInQueueHandler.styleUrl)
    async def loadAdminInQueueHandlerStyle():
        return adminInQueueHandler.loadStyle()

    @SERVER.get(adminInQueueHandler.getMembersUrl)
    async def getMembers(queueId: str):
        return adminInQueueHandler.getMembers(queueId)

    @SERVER.post(adminInQueueHandler.deleteMembersUrl)
    async def deleteMembers(members = Body()):
        return adminInQueueHandler.deleteMembers(members)

