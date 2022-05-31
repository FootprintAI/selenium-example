from drivers.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def do(driver: WebDriver, q: str):
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys(q)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
