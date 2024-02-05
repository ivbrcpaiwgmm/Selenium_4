from time import sleep
import math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_data = browser.find_element(By.ID, "input_value").text
    answer = calc(x_data)
    browser.find_element(By.ID, "answer").send_keys(answer)
    checkbox = browser.find_element(By.ID, "robotCheckbox")

    # Проскролливает экран, поднимая передаваемый элемент в самый верх, чтобы сделать его видимым.
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

    checkbox.click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    sleep(15)
    browser.quit()
