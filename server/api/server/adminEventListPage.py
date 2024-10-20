import os
import sys

# Determine the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    # Insert the given path into the system path for module importing
    sys.path.insert(0, path)

# Import the adminEventListPage module
import_module(os.path.join(API_DIR, "adminEventListPage"))
import adminEventList

ADMIN_EVENT_LIST_PAGE = adminEventList.AdminEventListHandler()
def setAdminEventListPage(SERVER):
    @SERVER.get(ADMIN_EVENT_LIST_PAGE.indexUrl)
    async def loadAdminEventListPageIndex():
        return ADMIN_EVENT_LIST_PAGE.loadIndex()

    @SERVER.get(ADMIN_EVENT_LIST_PAGE.scriptUrl)
    async def loadAdminEventListPageScript():
        return ADMIN_EVENT_LIST_PAGE.loadScript()

    @SERVER.get(ADMIN_EVENT_LIST_PAGE.pictureUrl)
    async def loadAdminEventListPagePicture():
        return ADMIN_EVENT_LIST_PAGE.loadPicture()

    @SERVER.get(ADMIN_EVENT_LIST_PAGE.styleUrl)
    async def loadAdminEventListPageStyle():
        return ADMIN_EVENT_LIST_PAGE.loadStyle()

    @SERVER.get(ADMIN_EVENT_LIST_PAGE.plusUrl)
    async def loadAdminEventListPagePlus():
        return ADMIN_EVENT_LIST_PAGE.loadPlus()

    @SERVER.get(ADMIN_EVENT_LIST_PAGE.getUserEventListUrl)
    async def getUserEventList():
        return ADMIN_EVENT_LIST_PAGE.getUserEventList()