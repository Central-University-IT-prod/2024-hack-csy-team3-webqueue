from fastapi import Body
import sys
import os

# Determine the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    # Insert the given path into the system path for module importing
    sys.path.insert(0, path)

# Import the adminInQueuePage module
import_module(os.path.join(API_DIR, "adminInQueuePage"))
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

