from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
# from openpyxl import load_workbook

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demoqa.com/webtables')

# driver.find_element(By.XPATH,'//*[@id="delete-record-1"]/svg/path').click()

driver.find_element(By.ID,'addNewRecordButton').click()

x = ("paijo","siswanto","mandiri@gmail.com","34","1000","front")

element = ["firstName","lastName","userEmail","age","salary","department"]

for i in element:
    driver.find_element(By.ID,i).send_keys(x)

time.sleep(10)
driver.find_element(By.ID,'submit').click()

try:
    webdriver(driver,10).until(EC.presence_of_element_located((By.ID,'submit'))).click()

    expect:
        pass