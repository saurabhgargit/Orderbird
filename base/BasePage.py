import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
            return element
        elif locatorType == "name":
            element = wait.until(lambda x: x.find_element(AppiumBy.NAME,locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
            return element
        elif locatorType == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            #element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH,  locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False


    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False


    def getText(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            self.log.info(
                "Getting text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return element.text
        except:
            self.log.info(
                "Unable to fetch text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False


    def isDisplayed(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            return False

    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(),name=text, attachment_type=AttachmentType.PNG)

    def deleteTextField(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            action = TouchAction(self.driver)
            action.tap(element,60,0,2)
            action.perform()
            element.send_keys(Keys.BACKSPACE)
            self.log.info(
                "Getting text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return element.text
        except:
            self.log.info(
                "Unable to fetch text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def acceptAlert(self):
        try:
            self.driver.switch_to.alert.accept()
        except:
            self.takeScreenshot("couldn't switch to alert")
            assert False



