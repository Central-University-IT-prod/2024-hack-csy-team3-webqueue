import sys
import os

# Determine the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    sys.path.insert(0, path)

# Import the adminCreateEventsPage module
import_module(os.path.join(API_DIR, "adminCreateEventsPage"))
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