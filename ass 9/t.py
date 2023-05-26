# http://10.10.16.15/submission
# //*[@id="TextBox1"]
# //*[@id="TextBox2"]
# //*[@id="Button1"]

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
path= 'C:\selenium\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(executable_path= path)

adsURL= "http://10.10.16.15/submission"
name="id"
pwd="password"
driver.get(adsURL)

time.sleep(3)


username= driver.find_element(By.XPATH, '//*[@id="TextBox1"]')
username.send_keys(name)

pswd= driver.find_element(By.XPATH, '//*[@id="TextBox2"]')
pswd.send_keys(pwd)

login= driver.find_element(By.XPATH, '//*[@id="Button1"]').click()

time.sleep(3)