from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.thsrc.com.tw/')
driver.maximize_window()  # 滿版視窗

# cookie = driver.find_element_by_xpath('/html/body/div[6]/div/div[3]/button[2]')
# cookie.click()

cookie = driver.find_element_by_class_name('swal2-confirm')
cookie.click()

# python selenium dropdown select
location01 = driver.find_element_by_id('select_location01')
Select(location01).select_by_visible_text('台南')

location02 = driver.find_element_by_id('select_location02')
Select(location02).select_by_visible_text('台北')

search = driver.find_element_by_id('start-search')
search.click()

driver.implicitly_wait(5)

time = driver.find_element_by_class_name('font-16r')
print(time.text)