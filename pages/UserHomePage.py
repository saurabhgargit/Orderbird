from base.BasePage import BasePage


class UserHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators value in UserHome page
    _pageMsg = "You are logged in as alice"  # id
    _logoutBtn = "(//XCUIElementTypeOther[@name=\"Logout\"])[2]"  # xpath
    _pageTitle = "Secret Area"  # id

    def verifyUserHomePage(self):
        element = self.isDisplayed(self._pageTitle, "id")
        assert element == True

    def verifyUserHomePageMsg(self):
        element = self.getText(self._pageMsg, "id")
        assert element == "You are logged in as alice"

    def clickLogoutBtn(self):
        self.clickElement(self._logoutBtn, "xpath")
