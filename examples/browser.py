from drivers.webdriver import WebDriver

from time import sleep

def navigation(driver: WebDriver):
    driver.get("https://www.google.com")
    sleep(1)
    driver.get("https://www.python.org")
    sleep(1)
    driver.back()
    sleep(1)
    driver.forward()

def get_cookies(driver: WebDriver):
    driver.get("https://www.google.com")
    print(driver.get_cookies())

