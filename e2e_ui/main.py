from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
from selenium.webdriver.common.timeouts import Timeouts

browser = Firefox()

load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


def test_site():
    browser.get('https://www.saucedemo.com/')
    assert(browser.current_url)

def test_auth():
    browser.get('http://www.saucedemo.com/')
    browser.find_element(By.XPATH,"//input[@data-test='username']").send_keys(login)
    browser.find_element(By.XPATH,"//input[@data-test='password']").send_keys(password)
    browser.find_element(By.XPATH,"//input[@data-test='login-button']").click()

    assert(browser.current_url == 'https://www.saucedemo.com/inventory.html')
    browser.delete_all_cookies()


def test_purchase():
    browser.get('http://www.saucedemo.com/')
    browser.find_element(By.XPATH,"//input[@data-test='username']").send_keys(login)
    browser.find_element(By.XPATH,"//input[@data-test='password']").send_keys(password)
    browser.find_element(By.XPATH,"//input[@data-test='login-button']").click()

    browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    browser.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    assert('Sauce Labs Backpack' in [ i.text for i in browser.find_elements(By.XPATH, "//div[@data-test='inventory-item-name']")])
    browser.get('https://www.saucedemo.com/inventory.html')
    browser.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']").click()
    browser.delete_all_cookies()

def test_delete():
    browser.get('http://www.saucedemo.com/')
    browser.find_element(By.XPATH,"//input[@data-test='username']").send_keys(login)
    browser.find_element(By.XPATH,"//input[@data-test='password']").send_keys(password)
    browser.find_element(By.XPATH,"//input[@data-test='login-button']").click()

    browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    browser.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    browser.get('https://www.saucedemo.com/inventory.html')
    browser.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']").click()
    browser.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
    assert( [] == browser.find_elements(By.XPATH, "//div[@data-test='inventory-item']"))

def test_timeout():

    browser.set_page_load_timeout(5)

    browser.get('http://www.saucedemo.com/')
    browser.find_element(By.XPATH,"//input[@data-test='username']").send_keys(login)
    browser.find_element(By.XPATH,"//input[@data-test='password']").send_keys(password)
    browser.find_element(By.XPATH,"//input[@data-test='login-button']").click()


def test_order():
    browser.get('http://www.saucedemo.com/')
    browser.find_element(By.XPATH,"//input[@data-test='username']").send_keys(login)
    browser.find_element(By.XPATH,"//input[@data-test='password']").send_keys(password)
    browser.find_element(By.XPATH,"//input[@data-test='login-button']").click()
    browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
    browser.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()

    browser.find_element(By.XPATH, "//button[@data-test='checkout']").click()
    browser.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys('qwerty')
    browser.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys('qwerty')
    browser.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys('1234567')

    browser.find_element(By.XPATH, "//input[@data-test='continue']").click()

    browser.find_element(By.XPATH, "//button[@data-test='finish']").click()
    assert("Thank you for your order!" == browser.find_element(By.XPATH, "//h2[@data-test='complete-header']").text)
    browser.delete_all_cookies()
