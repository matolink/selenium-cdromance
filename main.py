import os
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import Levenshtein as lev

DIR = '/home/matito/Downloads/'
REG = ['Region USA','Region Japan','Region Europe'] #Europe
CON = 'PSX'
lev2 = 99
excel = 'ldskajflkdsjlfkdsaj'
list1 = []
list2 = []
detlist = []
regionlist = []
a = []
cn = []
li = []

driver = uc.Chrome()
driver.implicitly_wait(30)
driver.get("https://cdromance.com/")
sb = driver.find_element(By.CLASS_NAME, "search-field")
sb.click()
sb.send_keys(excel) 
sb.submit()


gc = driver.find_elements(By.CLASS_NAME, 'game-container')
assert(len(gc)!=0), "ERROR WITH GAME " + excel + ": Console not found"

for i in range(len(gc)):
    detlist.append(gc[i].find_element(By.CLASS_NAME, 'details'))

for i in range(len(detlist)):
    regionlist.append(detlist[i].find_element(By.CLASS_NAME, 'region'))

for i in range(len(regionlist)):
    if regionlist[i].get_attribute("title") == REG[0]:
        list1.append(gc[i])
        print('se agrega a la lista list1[filtro region]')

if len(list1) == 0:
    for i in range(len(regionlist)):
        if regionlist[i].get_attribute("title") == REG[1]:
            list1.append(gc[i])
            print('se agrega a la lista list1[filtro region]')

if len(list1) == 0:
    for i in range(len(regionlist)):
        if regionlist[i].get_attribute("title") == REG[2]:
            list1.append(gc[i])
            print('se agrega a la lista list1[filtro region]')

for i in range(len(list1)):
    a.append(list1[i].find_element(By.TAG_NAME, 'a'))

for i in range(len(a)):
    cn.append(a[i].find_element(By.CLASS_NAME, 'console'))

for i in range(len(cn)):
    if cn[i].text == CON:
        list2.append(list1[i])
        print('se agrega a la lista list2[filtro consola]')

print(list2)
print(len(list2))
assert(len(list2)!=0), "ERROR WITH GAME " + excel + ": Console not found"

for i in range(len(list2)):
    li.append(list2[i].find_element(By.CLASS_NAME, 'game-title'))

for titles in li:
    print(titles.text)
    lev1 = lev.distance(titles.text,excel)
    if lev1 < lev2:
        lev2 = lev1
        final_text = titles.text
        print(final_text)

for i in range(len(li)):
    if final_text == li[i].text:
        game = list2[i]

game.click()

dl = driver.find_element(By.ID, 'dl-btn-0')
name = dl.get_attribute("data-filename")
dl.click()
while True:
        if os.path.exists(DIR + name):
            break
        else:
            print('else')
            time.sleep(10)
driver.close()