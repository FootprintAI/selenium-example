from drivers.webdriver import WebDriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def query(driver: WebDriver, symbol: str):
    driver.get("https://goodinfo.tw/StockInfo/index.asp")
    ele = driver.find_element_by_xpath(u"//*[@id='txtStockCode']")
    ele.clear()
    ele.send_keys(symbol)
    driver.find_element_by_xpath(u"//input[@value='股票查詢']").click()

    # the following code will wait until the element is visible
    try:
        wait = WebDriverWait(driver, 30)
        wait.until(EC.visibility_of_element_located((By.XPATH, u"//*[@id='imgKC']")))
    except:
        raise Exception("target element is not show up")

