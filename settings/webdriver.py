from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait


class Driver:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 1}
        chrome_options.add_experimental_option("prefs", prefs)
#         chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('window-size=1600,1200')
        self.instance = webdriver.Chrome(options=chrome_options, executable_path='./chromedriver.exe')

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.maximize_window()
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")

# webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    desired_capabilities=DesiredCapabilities.CHROME,
#             options=chrome_options)
# s
