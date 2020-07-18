from selenium.webdriver.common.by import By

#搜索相关
search_click_icon=By.ID,"com.android.settings:id/search"
search_input_text=By.ID,"android:id/search_src_text"
search_click_back=By.CLASS_NAME,"android.widget.ImageButton"

#图案解锁相关
unlock_storage=By.XPATH,"//*[contains(@text,'存储')]"
unlock_WLAN=By.XPATH,"//*[contains(@text,'WLAN')]"
unlock_safety=By.XPATH,"//*[contains(@class,'android.widget.TextView')]"
unlock_lock_screen_way=By.XPATH,"//*[contains(@text,'屏幕锁定方式')]"
unlock_lock_icon=By.XPATH,"//*[contains(@text,'图案')]"