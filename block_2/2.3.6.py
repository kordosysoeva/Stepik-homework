import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from pages.Base import Base
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from tests.conftest import headless
from selenium.webdriver.support import expected_conditions as EC
import math
fake = Faker("ru_RU")

chrome_options = webdriver.ChromeOptions()
service = ChromeService(ChromeDriverManager().install())
chrome_options.add_argument("--window-size=1920,1080")
browser = webdriver.Chrome(service=service, chrome_options=chrome_options)
browser.get("http://suninjuly.github.io/redirect_accept.html")
button_magical = browser.find_element(By.XPATH,"//button[@type='submit']")
button_magical.click()
time.sleep(2)
browser.switch_to.window(browser.window_handles[1])


""" MATH """
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.ID, 'input_value')
x = x_element.text
print(calc(x))
textarea_for_answer = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,'answer')))
textarea_for_answer.send_keys(str(calc(x)))
button_submit = browser.find_element(By.XPATH,"//button[@type='submit']")
print("не нажал")
button_submit.click()
print("нажал")
time.sleep(5)
