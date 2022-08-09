import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import Levenshtein as lev
DIR = '/home/matito/Downloads/'
REG = 'USA' #Europe
driver = uc.Chrome()
excel = 'P.n. 03' #aquí va el texto exportado del excel
lev2 = 99
driver.get("https://cdromance.com/")
driver.implicitly_wait(30)
sb = driver.find_element(By.CLASS_NAME, "search-field")
sb.click()
sb.send_keys(excel) 
sb.submit()
gc = driver.find_elements(By.CLASS_NAME, 'game-container')
li = driver.find_elements(By.CLASS_NAME, 'game-title')
for items in li:
    print(items.text)
    lev1 = lev.distance(items.text,excel)
    if lev1 < lev2:
        lev2 = lev1
        final_text = items.text
for items in li:
    if final_text == items.text:
        game = items
game.click()
dl = driver.find_element(By.ID, 'dl-btn-0')
name = dl.get_attribute("data-filename")
dl.click()
while True:
        if os.path.exists(dir + name):
            break
        else:
            print('else')
            time.sleep(10)
driver.close()