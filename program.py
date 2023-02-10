from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
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

# email=(input('input email: '))
# password=(input('input password: '))

#menuju website
driver.get('https://shopee.co.id/buyer/login?')

# login
element = wait(driver,10).until(EC.element_to_be_clickable((By.NAME,"loginKey"))).send_keys('085651006861')
    
element = wait(driver,10).until(EC.element_to_be_clickable((By.NAME,"password"))).send_keys('Sukses75')
    
wait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#main > div > div.vtexOX > div > div > div > div:nth-child(2) > form > div > div.yXry6s > button'))).click()
    # try:
wait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME,"navbar__username")))

# mencari barang
driver.get('https://shopee.co.id/') 
element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"shopee-searchbar-input__input"))).send_keys('kacamata')
driver.find_element(By.CSS_SELECTOR,"#main > div > header > div.container-wrapper.header-with-search-wrapper > div > div.header-with-search__search-section > div.shopee-searchbar > button > svg")
# memilih kategori penjual
# element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"shopee-checkbox__label"))).click()
# element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"shopee-checkbox__label"))).click()


    # except:
        # print(f"[*] [ {email} ] Login Failed, Please wait, trying to login again!")
        # url()


time.sleep(5)
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as wait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# import time
# # from openpyxl import load_workbook

# option = webdriver.ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-logging'])
# driver = webdriver.Chrome(options=option)
# driver.implicitly_wait(10)
# driver.maximize_window()

# # email=(input('input email: '))
# # password=(input('input password: '))

# #menuju website
# # def url():
# driver.get('https://www.kai.id')

# # login
# # def login():
# element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-selection__rendered"))).send_keys('yogyakarta').click()
    
# element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"select2-search__field"))).send_keys('bandung').click()
    
# wait(driver,10).until(EC.element_to_be_clickable((By.ID,'select2-adult2-container'))).click()
#     # try:
# wait(driver,60).until(EC.presence_of_element_located((By.ID,"submittrain"))).click()

# # driver.get('https://shopee.co.id/') 
# # element = wait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"shopee-searchbar-input__input"))).send_keys('kacamata').click()


#     # except:
#         # print(f"[*] [ {email} ] Login Failed, Please wait, trying to login again!")
#         # url()


# time.sleep(5)
# # driver.quit()