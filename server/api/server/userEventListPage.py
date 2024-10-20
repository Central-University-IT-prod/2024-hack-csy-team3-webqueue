import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = ROOT_DIR + "\\server"
API_DIR = SERVER_DIR + "\\api"

def importModule(path: str):
    sys.path.insert(0, path)

importModule(API_DIR + "\\userEventListPage")
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