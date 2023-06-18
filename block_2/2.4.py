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
browser.get("http://suninjuly.github.io/file_input.html")
print(os.path.abspath(__file__))
current_dir = (os.path.abspath(os.path.dirname(__file__)))
file_path = os.path.join(current_dir, 'empty.txt')
print(file_path)
first = browser.find_element(By.NAME, 'firstname')
last = browser.find_element(By.NAME, 'lastname')
email = browser.find_element(By.NAME, 'email')
first.send_keys(fake.first_name())
last.send_keys(fake.last_name())
email.send_keys(fake.ascii_free_email())
input_file = browser.find_element(By.NAME, 'file')
input_file.send_keys(file_path)
#
# """ MATH """
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# x_element = browser.find_element(By.ID, 'input_value')
# x = x_element.text
#
# print(calc(x))
# textarea_for_answer = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID,'answer')))
# textarea_for_answer.send_keys(str(calc(x)))
#

button_submit = browser.find_element(By.XPATH,"//button[@type='submit']")
# # browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
# browser.execute_script("window.scrollBy(0, 100);")
#
#
# check_box = browser.find_element(By.ID, 'robotCheckbox')
# check_box.click()
# radiobutton = browser.find_element(By.ID, 'robotsRule')
# radiobutton.click()
print("не нажал")
button_submit.click()
print("нажал")
time.sleep(5)