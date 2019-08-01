from selenium import webdriver
import os
from pyvirtualdisplay import Display


class Driver:
    VISIBLE = 1  # 0 - do not run GUI mode, 1 - run GUI mode
    ORIG = os.environ["DISPLAY"]

    def __init__(self):
        """PyVirtualDisplay library for run tests without GUI mode e.g. on Jenkins.
        On machine must be installed xvfb module or Xephyr - sudo apt-get install xvfb xserver-xephyr"""
        self.display = Display(visible=self.VISIBLE, size=(2560, 2560))
        self.display.start()
        # reset of DISPLAY instance - it is neccesery for parallel testing
        os.environ["DISPLAY"] = self.ORIG
        if os.getenv('BROWSER') == "CH":
            self.instance = webdriver.Chrome(
                executable_path='./automationpractice.com/chromedriver.exe')
        elif os.getenv('BROWSER') == "FF":
            self.instance = webdriver.Firefox(executable_path='./automationpractice.com/geckodriver.exe')
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

    def teardown(self):
        self.instance.quit()
        self.display.stop()
