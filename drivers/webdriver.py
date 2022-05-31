import os
import platform
from selenium.webdriver import Chrome, ChromeOptions

class WebDriver(Chrome):
    def __init__(self, headless:bool=False):
        exec_path = None
        if platform.system() == "Darwin":
            exec_path = self.__wrap_abspath('chromedriver.darwin')
        elif platform.system() == "Windows":
            exec_path = self.__wrap_abspath('chromedriver.exe')
        elif platform.system() == "Linux":
            exec_path = self.__wrap_abspath('chromedriver.linux')

        chrome_options = ChromeOptions()
        # comment this to enable guest browser to show up (for debugging
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')

        Chrome.__init__(self,chrome_options=chrome_options, executable_path=exec_path)

    def __wrap_abspath(self, binary)-> str:
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), binary)
