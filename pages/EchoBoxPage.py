from base.BasePage import BasePage
import utilities.CustomLogger as cl

class EchoBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators value in Echobox page
    _msgField = "messageInput"  # name
    _msgSaveBtn = "messageSaveBtn"  # name
    _pageTitle = "Here's what you said before:"  # id
    _savedMessage = "savedMessage"  # id

    def verifyEchoBoxPage(self):
        element = self.isDisplayed(self._pageTitle, "id")
        assert element == True
        #ele = self.getText(self._savedMessage, "id")
        cl.allureLogs("Echo box page has been displayed")

    def enterTextInMsgField(self, text):
        self.sendText(text, self._msgField, "name")
        cl.allureLogs("User has entered the text for echo box")

    def clickSaveBtn(self):
        self.clickElement(self._msgSaveBtn, "id")
        cl.allureLogs("User has saved the text for echo box")

    def deleteText(self):
        self.deleteTextField(self._msgField, "name")
        cl.allureLogs("User has deleted the text for echo box")
