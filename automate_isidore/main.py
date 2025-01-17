from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import xpath as xp
import os

os.environ['PATH']+= r'C:\\Users\\manid\\OneDrive\\Desktop\\codes\\chromedriver.exe'

driver = webdriver.Chrome()
driver.get('https://isidore.udayton.edu/portal')
driver.implicitly_wait(30)
driver.find_element(By.XPATH,xp.loginpage).click()
driver.find_element(By.ID,'username').send_keys('kotturus1')
driver.find_element(By.ID,'password').send_keys('Surya1603')
driver.find_element(By.NAME,'_eventId_proceed').click()
time.sleep(5000)
driver.find_element(By.XPATH,xp.CPScourse).click()
print("subject selected")
driver.find_element(By.XPATH,xp.assignment_link).click()