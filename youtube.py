from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://youtu.be/EadLGsh2RgU')
driver.maximize_window()  # 滿版視窗
time.sleep(1)
fullscreen = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[24]/div[2]/div[2]/button[10]")
fullscreen.click()

time.sleep(185)

stopfullscreen = driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div/ytd-player/div/div/div[24]/div[2]/div[2]/button[10]")
stopfullscreen.click()
driver.quit()

