import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
file_name = "for_upload.txt"
file_dir_path = os.path.abspath(os.path.dirname(file_name))
file_path = os.path.join(file_dir_path, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, "//input[@placeholder='Enter first name' and @required]").send_keys('John')
    browser.find_element(By.XPATH, "//input[@placeholder='Enter last name' and @required]").send_keys('Johnson')
    browser.find_element(By.XPATH, "//input[@placeholder='Enter email' and @required]").send_keys('John@gmail.jj')
    browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    sleep(15)
    browser.quit()
