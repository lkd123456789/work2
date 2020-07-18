import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from Base.get_driver import GetDriver
import Data

class Base:
    def __init__(self,driver):
        self.driver=driver

    #查找单个元素
    def base_find_element(self,loc,time=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #查找多个元素
    def base_find_elements(self,loc,time=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=time,poll_frequency=poll).until(lambda x:x.find_elements(*loc))

    #点击元素
    def base_click_element(self,loc):
        self.base_find_element(loc).click()

    #输入元素
    def base_input_text(self,loc,value):
        elem=self.base_find_element(loc)
        elem.clear()
        elem.send_keys(value)

    #截图
    def base_get_screenshot(self,name):
        self.driver.get_screenshot_as_file("../Images/{}.png".format(time.strftime("{}-%Y-%m-%d-%H-%M-%S".format(name))))

    #scroll滑动
    def base_scroll(self,loc1,loc2):
        elem1=self.base_find_element(loc1)
        elem2=self.base_find_element(loc2)
        self.driver.scroll(elem1,elem2)

