from Base.base import Base
import Data
class PageSearch(Base):
    def __init__(self,driver):
        self.driver=driver

    #点击搜索图标
    def page_click_search(self):
        self.base_click_element(Data.search_click_icon)

    #输入信息
    def page_input_text(self,value):
        self.base_input_text(Data.search_input_text,value)

    #点击返回按钮
    def page_click_back(self):
        self.base_click_element(Data.search_click_back)

    #截图
    def page_get_screenshot(self,name):
        self.base_get_screenshot(name)