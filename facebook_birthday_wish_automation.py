from selenium import webdriver 
import time 

driver = webdriver.Chrome('/home/vamsi/Downloads/chromedriver')
driver.maximize_window()
driver.get('https://www.facebook.com')
login_number = driver.find_element_by_xpath('//*[@id="email"]')
login_number.click()
login_number.send_keys('8148419876')
password_field = driver.find_element_by_xpath('//*[@id="pass"]')
password_field.click()
password_field.send_keys('vamsi19958148')
login_button = driver.find_element_by_id('loginbutton')
login_button.click()
time.sleep(5)
header_notification = driver.find_element_by_xpath('//*[@id="fbNotificationsJewel"]/a').click()
