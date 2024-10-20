from fastapi import FastAPI
import uvicorn
import registerHumanPage
import adminLoginPage
import adminCreateEventsPage
import userEventListPage
import waitPage
import adminEventListPage
import adminInQueuePage

SERVER = FastAPI()

registerHumanPage.setRegisterHumanPage(SERVER)
adminLoginPage.setAdminLoginPage(SERVER)
adminCreateEventsPage.setAdminCreateEventsPage(SERVER)
userEventListPage.setUserEventListPage(SERVER)
waitPage.setWaitPage(SERVER)
adminEventListPage.setAdminEventListPage(SERVER)
adminInQueuePage.setAdminInQueuePage(SERVER)

if __name__ == "__main__":
    uvicorn.run(SERVER, port=80, host="127.0.0.1")