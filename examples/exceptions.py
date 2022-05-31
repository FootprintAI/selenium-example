from drivers.webdriver import WebDriver

def exception_handling(driver: WebDriver):
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    try:
        driver.get("https://www.google.com")
    except TimeoutException:
        print("time out")
    try:
        driver.find_element_by_id("you-should-not-see-me")
    except NoSuchElementException:
        print("no element found")

