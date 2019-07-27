from selenium import webdriver
import os

class Driver:

    def __init__(self):

        if os.getenv('BROWSER') == "CH":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('window-size=1600,1200')
            self.instance = webdriver.Chrome(options=chrome_options,
                                             executable_path='/home/piotrko/PycharmProjects/automationpractice.com/chromedriver.exe')
        elif os.getenv('BROWSER') == "FF":
            ff_options = webdriver.FirefoxOptions()
            # ff_options.headless = True
            self.instance = webdriver.Firefox(options=ff_options,
                                              executable_path='/home/piotrko/PycharmProjects/automationpractice.com/geckodriver.exe')
        elif os.getenv('BROWSER') == "OP":
            self.instance = webdriver.Opera(
                executable_path='./automationpractice.com/operadriver.exe')
        else:
            print("Please mark a browser")

    def navigate(self, url):
        if isinstance(url, str):
            self.instance.maximize_window()
            self.instance.get(url)
        else:
            raise TypeError("URL must be a string.")
