import unittest

import pytest

from pages.AppLaunchPage import AppLaunchPage
from pages.LoginPage import LoginPage
from pages.UserHomePage import UserHomePage


@pytest.mark.usefixtures("beforeClass")
class LoginPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ap = AppLaunchPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.uhp = UserHomePage(self.driver)

    @pytest.mark.order(2)
    def test_loginUsingValidData(self):
        self.lp.enterEmail("alice")
        self.lp.enterPassword("mypassword")
        self.lp.clickLoginButton()
        self.uhp.verifyUserHomePage()
        self.uhp.verifyUserHomePageMsg()
        self.uhp.clickLogoutBtn()

    @pytest.mark.order(1)
    def test_openLoginPage(self):
        self.ap.clickLoginScreenBtn()
        self.lp.verifyLoginPage()

    @pytest.mark.order(3)
    def test_loginUsingInValidData(self):
        self.lp.enterEmail("alice")
        self.lp.enterPassword(" ")
        self.lp.clickLoginButton()
        self.lp.acceptAlert()

