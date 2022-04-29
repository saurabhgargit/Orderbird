
from appium import  webdriver

class Driver:

    def getDriverMethod(self):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '13.6'
        desired_caps['deviceName'] = 'iPhone 11'
        desired_caps['app'] = ('/Users/saurabhgarg/Downloads/TheApp2.app')

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        return driver

