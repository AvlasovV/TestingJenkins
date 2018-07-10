import time
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


with open("password.txt", "r") as file:
    array = [row.strip() for row in file]
login = array[0]
password = array[1]

NAME = "Aulasau"

driver = webdriver.Chrome("D:\DOWNLOADS\chromedriver.exe")
try:
    wait = WebDriverWait(driver,10)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://portal.iba.by/")
    # pam param
    elem = driver.find_element_by_xpath(".//*[@id='sign-in']/i")
    elem.click()

    a = driver.switch_to_active_element()

    elem = driver.find_element_by_xpath(".//*[@id='_com_liferay_login_web_portlet_LoginPortlet_login']")
    elem.send_keys(login)
    elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_password")
    elem.send_keys(password)
    elem.submit()

    time.sleep(3)

    elem = driver.find_element_by_xpath(".//*[@id='banner']/div/div[2]/div/div[2]/ul/li[2]/a")
    elem.click()
    elem = driver.find_element_by_xpath(".//*[@id='banner']/div/div[2]/div/div[2]/ul/li[2]/ul/li[2]/a")
    elem.click()

    elem = driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[1]/div[1]/div/input")

    elem.send_keys(NAME)
    elem = driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[1]/div[3]/button")
    elem.click()
    try:
        if driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[3]/table").is_enabled():
            print("We found something")
    except(selenium.common.exceptions.NoSuchElementException):
        print("No results found")

    print("ending test")
finally:
    time.sleep(3)
    driver.close()