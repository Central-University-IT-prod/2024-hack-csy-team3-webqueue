import os
import sys

# Determine the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    # Insert the given path into the system path for module importing
    sys.path.insert(0, path)

# Import the userEventListPage module
import_module(os.path.join(API_DIR, "userEventListPage"))
import userEventList

USER_EVENT_LIST_PAGE = userEventList.UserEventListHandler()
def setUserEventListPage(SERVER):
    @SERVER.get(USER_EVENT_LIST_PAGE.indexUrl)
    async def loadUserEventListPageIndex():
        return USER_EVENT_LIST_PAGE.loadIndex()

    @SERVER.get(USER_EVENT_LIST_PAGE.scriptUrl)
    async def loadUserEventListPageScript():
        return USER_EVENT_LIST_PAGE.loadScript()

    @SERVER.get(USER_EVENT_LIST_PAGE.pictureUrl)
    async def loadUserEventListPagePicture():
        return USER_EVENT_LIST_PAGE.loadPicture()

    @SERVER.get(USER_EVENT_LIST_PAGE.styleUrl)
    async def loadUserEventListPageStyle():
        return USER_EVENT_LIST_PAGE.loadStyle()

    @SERVER.get(USER_EVENT_LIST_PAGE.getUserEventListUrl)
    async def getUserEventList():
        return USER_EVENT_LIST_PAGE.getUserEventList()