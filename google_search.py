from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = 'chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.get('http://www.google.com')

search = driver.find_element_by_xpath('//*[@id="input"]')

search.send_keys('曲面螢幕')
search.send_keys(Keys.RETURN)
