import sys
import os

# Determine the root directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT_DIR, "server")
API_DIR = os.path.join(SERVER_DIR, "api")

def import_module(path: str):
    # Insert the given path into the system path for module importing
    sys.path.insert(0, path)

# Import the waitPage module
import_module(os.path.join(API_DIR, "waitPage"))
import wait

WAIT_PAGE = wait.WaitPageHandler()
def setWaitPage(SERVER):
    @SERVER.get(WAIT_PAGE.indexUrl)
    async def loadWaitPageIndex():
        return WAIT_PAGE.loadIndex()

    @SERVER.get(WAIT_PAGE.scriptUrl)
    async def loadWaitPageScript():
        return WAIT_PAGE.loadScript()

    @SERVER.get(WAIT_PAGE.styleUrl)
    async def loadWaitPageStyle():
        return WAIT_PAGE.loadStyle()

    @SERVER.get(WAIT_PAGE.clockUrl)
    async def loadWaitPageClock():
        return WAIT_PAGE.loadClock()

    @SERVER.get(WAIT_PAGE.logotipUrl)
    async def loadWaitPageLogotip():
        return WAIT_PAGE.loadLogotip()

    @SERVER.get(WAIT_PAGE.getQueueStateUrl)
    async def loadWaitPageGetQueueState(login: str, queueId: str):
        return WAIT_PAGE.getQueueState(login, queueId)