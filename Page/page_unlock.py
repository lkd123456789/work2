from appium.webdriver.common.touch_action import TouchAction
from Base.base import Base
import Data
from Base.get_driver import GetDriver
from time import sleep
class PageUnlock(Base):
    def __init__(self,driver):
        self.driver=driver

    #进入设置，向上滑动，使得页面显示“安全”
    def page_scorll_safety(self):
        self.base_scroll(Data.unlock_storage,Data.unlock_WLAN)

    #点击安全
    def page_click_safety(self):
        elements=self.base_find_elements(Data.unlock_safety)
        for element in elements:
            if "安全" in element.text:
                element.click()
                break
    #点击锁屏锁定方式
    def page_click_lock_screen_way(self):
        self.base_click_element(Data.unlock_lock_screen_way)

    #点击图案
    def page_click_icon(self):
        self.base_click_element(Data.unlock_lock_icon)

    #设置图案,1(90,320)   2(270,320)  3(450,320) 4(450,500)
    def page_press_move_to(self):
        TouchAction(self.driver).press(x=90,y=320).wait(2000).move_to(x=270,y=320).release().perform()


if __name__ == '__main__':
    d=GetDriver().get_driver()
    p=PageUnlock(d)
    p.page_scorll_safety()
    sleep(2)
    p.page_click_safety()
    sleep(2)
    p.page_click_lock_screen_way()
    p.page_click_icon()
    p.page_press_move_to()