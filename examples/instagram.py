from drivers.webdriver import WebDriver

from time import sleep

def login(driver: WebDriver, email: str, password: str):

    driver.get("https://www.instagram.com")
    sleep(5) # wait for the page loading is finished
    # find username fields
    username_field=driver.find_element_by_css_selector("input[name='username']")
    # find password fields
    password_field=driver.find_element_by_css_selector("input[name='password']")
    username_field.clear()
    password_field.clear()
    # send email in username field
    username_field.send_keys(email)
    # send password in password field
    password_field.send_keys(password)
    sleep(5)

    # click login button
    driver.find_element_by_css_selector("button[type='submit']").click()
    __post_login(driver)

def __post_login(driver: WebDriver):

    # mute notification
    ele = driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")
    if len(ele) > 0:
        ele[0].click()
    #turn on notif
    sleep(10)
    ele2 = driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")
    if len(ele2) > 0:
        ele2[0].click()
