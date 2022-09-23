#IMPORTS
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select as select

#OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#DRIVER SETTINGS
os.environ['PATH'] += r".\chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.revolut.com/")

#VARIABLES
print("Enter phone number:")
phonenumber = input()
print("Country name:")
countryy = input()

#SCRAP&AUTOMATION
acceptcookies = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/button[1]'))).click()
signupbutton = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/header/div/div[1]/a[2]'))).click()
enterphonenumber = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/form/span/label[2]/div/span/span[1]/input'))).send_keys(phonenumber)
labelphonecountry = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/form/span/label[1]'))).click()
searchcountry = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div/span/div[1]/div/input'))).send_keys(countryy)
selectcountry = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list-:r3:-option-'+countryy+'"]'))).click()
sendbutton = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/form/button[2]'))).click()
phonecode = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="list-:r3:-option-'+countryy+'"]/div/span/span/span[2]')))

#RESULT
print('Succesfully sent SMS to '+phonecode.text+''+phonenumber+' !')

driver.quit()