import sys,os
sys.path.append(os.getcwd())
from time import sleep
import pytest
from Base.get_driver import GetDriver
from Page.page_search import PageSearch
from Tools.read_data import ReadData

def get_data():
    data_list=[]
    datas=ReadData().read_data("search").get("Search_data")
    for data in datas.keys():
        data_list.append(datas.get(data).get("text"))
    return data_list

class TestSearch():

    def setup_class(self):
        self.driver = GetDriver().get_driver()
        self.search = PageSearch(self.driver)
        self.search.page_click_search()

    def teardown_class(self):
        self.search.page_click_back()
        GetDriver().close_driver()

    @pytest.mark.parametrize('value',get_data())
    def test_search(self,value):
        self.search.page_input_text(value)
        sleep(3)
        self.search.page_get_screenshot("search")

if __name__ == '__main__':
    pytest.main()
