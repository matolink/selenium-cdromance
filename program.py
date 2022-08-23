import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import Levenshtein as lev
import waitdl as wd
from re import search

def pg(excel,DIR,CON):
    list1 = []
    list2 = []
    detlist = []
    regionlist = []
    a = []
    cn = []
    li = []
    roms = []
    erase = []
    disc = False
    REG = ['Region USA','Region Japan','Region Europe'] #Europe
    lev2=99
    driver = uc.Chrome()
    driver.implicitly_wait(30)
    driver.get("https://cdromance.com/")
    sb = driver.find_element(By.CLASS_NAME, "search-field")
    sb.click()
    sb.send_keys(excel) 
    sb.submit()
    time.sleep(5)

    if driver.find_elements(By.CLASS_NAME, 'no-results'):
        driver.close()
        print('Game not Found')
        not_found = True
        return 
    gc = driver.find_elements(By.CLASS_NAME, 'game-container')

    for i in range(len(gc)):
        if gc[i].get_attribute("style"):
            erase.append(i)
            continue
        else:
            detlist.append(gc[i].find_element(By.CLASS_NAME, 'details'))

    if len(erase) != 0:
        for i in range(len(erase)):
            del gc[erase[i]]

    for i in range(len(detlist)):
        regionlist.append(detlist[i].find_element(By.CLASS_NAME, 'region'))

    for i in range(len(regionlist)):
        if regionlist[i].get_attribute("title") == REG[0]:
            list1.append(gc[i])
        else:
            continue

    if len(list1) == 0:
        for i in range(len(regionlist)):
            if regionlist[i].get_attribute("title") == REG[1]:
                list1.append(gc[i])
            else:
                continue

    if len(list1) == 0:
        for i in range(len(regionlist)):
            if regionlist[i].get_attribute("title") == REG[2]:
                list1.append(gc[i])
            else:
                continue

    for i in range(len(list1)):
        a.append(list1[i].find_element(By.TAG_NAME, "a"))

    for i in range(len(a)):
        cn.append(a[i].find_element(By.CLASS_NAME, 'console'))

    for i in range(len(cn)):
        if cn[i].text == CON:
            list2.append(list1[i])

    if(len(list2)==0):
        print("Console not found")
        not_found = True
        return not_found

    for i in range(len(list2)):
        li.append(list2[i].find_element(By.CLASS_NAME, 'game-title'))

    for titles in li:
        lev1 = lev.distance(titles.text,excel)
        if lev1 < lev2:
            lev2 = lev1
            final_text = titles.text

    for i in range(len(li)):
        if final_text == li[i].text:
            game = list2[i]

    game.click()

    table = driver.find_element(By.CLASS_NAME, 'download-links')
    roms = table.find_elements(By. TAG_NAME, 'button')
    for i in range(len(roms)):
        if search('Disc',roms[i].get_attribute('data-filename')):
            name = roms[i].get_attribute('data-filename')
            roms[i].click()
            wd.waitdl(name, DIR)
            disc = True
        else:
            continue

    if disc == False:
        name = roms[0].get_attribute('data-filename')
        roms[0].click()
        wd.waitdl(name, DIR)

    driver.close()