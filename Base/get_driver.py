from appium import webdriver

class GetDriver:
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            deisred_caps={}
            deisred_caps["platformName"]="android"
            deisred_caps["platformVersion"]="5.1.1"
            deisred_caps["deviceName"]="emulator-5554"
            deisred_caps["appPackage"]="com.android.settings"
            deisred_caps["appActivity"]=".Settings"
            deisred_caps["unicodeKeyboard"]=True
            deisred_caps["resetKeyboard"]=True
            cls.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",deisred_caps)
        return cls.driver

    @classmethod
    def close_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver=None