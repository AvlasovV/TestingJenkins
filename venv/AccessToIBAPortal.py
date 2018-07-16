import argparse
import time
import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import sys

# just for security add txt-file and we shouldn't push it into the repo

def input_from_file(fileName):
    with open(fileName, "r") as file:
        array = [row.strip() for row in file]
    return array

def input_from_cmd():
    parser = argparse.ArgumentParser(description="Just parameters for cmd line")
    parser.add_argument('login', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('searchName', type=str)
    return parser.parse_args()

# def test_checking_name(name):
#     elem = driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[1]/div[1]/div/input")
#     elem.send_keys(name)
#     elem.click()
#     time.sleep(1)
#     assert driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[3]/table").is_enabled()
    # try:
    #     if driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[3]/table").is_enabled():
    #         print("We found something")
    # except(selenium.common.exceptions.NoSuchElementException):
    #     print("No results found")

# input_from_file(args[0], args[1], args[2], r"D:\Aulasau_U\PycharmProjects\TasksForStudy\TryingSelenium\venv\password.txt")
#   args = input_from_file(r"D:\Aulasau_U\PycharmProjects\TasksForStudy\TryingSelenium\venv\password.txt")


args = input_from_cmd()

# driver = webdriver.Chrome("D:\DOWNLOADS\chromedriver.exe")
driver = webdriver.Firefox(executable_path=r"D:\DOWNLOADS\geckodriver.exe")
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
    elem.clear()
    elem.send_keys(args.login)
    elem = driver.find_element_by_id("_com_liferay_login_web_portlet_LoginPortlet_password")
    elem.send_keys(args.password)
    elem.submit()

    time.sleep(3)
    elem = driver.find_element_by_xpath("//ul[@class='nav navbar-nav']//li[2]//a[1]//i[1]")
    elem.click()

    time.sleep(1)
    elem = driver.find_element_by_xpath("//a[@href='https://portal.iba.by/web/guest/poisk-sotrudnikov']")
    elem.click()



    elem = driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[1]/div[1]/div/input")

    elem.send_keys(args.searchName)

    elem = driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[1]/div[3]/button")
    driver.execute_script("arguments[0].click();", elem)


    try:
        if driver.find_element_by_xpath(".//*[@id='_SearchPerson_INSTANCE_6NvxyekxSIB6_']/div/div[3]/table").is_enabled():
            elements = driver.find_elements_by_xpath("//div[@class='page-wrapper']//tbody//tr[*]")
            print(elements.__len__())

            for i in elements:
                str = i.text
                if ((" " + args.searchName + " ").upper() in str.upper()) or ((args.searchName + " ").upper() in str.upper()):
                    print("We found:", end=" ")
                    print(str)

    except(selenium.common.exceptions.NoSuchElementException):
        print("No results found")

    print("ending test")
finally:
    time.sleep(3)
    driver.close()
    # driver.quit()