# -*- coding: utf-8 -*-
import time
import os
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# jenkinsJobName=os.getenv("JOB_NAME")
url="http://www.csdn.net"
print(url)
save_fn = "testResult.png"
option = webdriver.ChromeOptions()
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')
option.add_argument("--window-size=1280,1024")
option.add_argument("--hide-scrollbars")
 
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()
driver.get(url)
print(driver.title)
 
scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
driver.set_window_size(scroll_width, scroll_height)
driver.save_screenshot(save_fn)
driver.quit()