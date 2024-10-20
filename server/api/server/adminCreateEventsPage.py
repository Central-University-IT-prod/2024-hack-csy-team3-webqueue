import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = ROOT_DIR + "\\server"
API_DIR = SERVER_DIR + "\\api"

def importModule(path: str):
    sys.path.insert(0, path)

importModule(API_DIR + "\\adminCreateEventsPage")
import adminCreateEvents

ADMIN_CREATE_EVENTS_PAGE = adminCreateEvents.AdminCreaterEventsHandler()
def setAdminCreateEventsPage(SERVER):
    @SERVER.get(ADMIN_CREATE_EVENTS_PAGE.indexUrl)
    async def loadAdminCreateEventsPageIndex():
        return ADMIN_CREATE_EVENTS_PAGE.loadIndex()

    @SERVER.get(ADMIN_CREATE_EVENTS_PAGE.scriptUrl)
    async def loadAdminCreateEventsPageScript():
        return ADMIN_CREATE_EVENTS_PAGE.loadScript()

    @SERVER.get(ADMIN_CREATE_EVENTS_PAGE.scriptUrl)
    async def loadAdminCreateEventsPageScript():
        return ADMIN_CREATE_EVENTS_PAGE.loadScript()

    @SERVER.get(ADMIN_CREATE_EVENTS_PAGE.styleUrl)
    async def loadAdminCreateEventsPageStyle():
        return ADMIN_CREATE_EVENTS_PAGE.loadStyle()

    @SERVER.get(ADMIN_CREATE_EVENTS_PAGE.getQueueIdUrl)
    async def getQueueId(data: str):
        eventName, description, avgTime = data.split(" ")[0], data.split(" ")[1], data.split(" ")[2]
        return ADMIN_CREATE_EVENTS_PAGE.getQueueId(eventName, description, avgTime)