from selenium import webdriver
import os
from pyvirtualdisplay import Display
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Driver:
    VISIBLE = 0  # 0 - do not run GUI mode, 1 - run GUI mode
    GRID_URL = "http://localhost:4444/wd/hub"

    def __init__(self):
        """PyVirtualDisplay library for run tests without GUI mode e.g. on Jenkins.
        On machine must be installed xvfb module or Xephyr - sudo apt-get install xvfb xserver-xephyr"""
        # self.display = Display(visible=self.VISIBLE, size=(2560, 2560))
        # self.display.start()
        # new DISPLAY instance - it is necessary for parallel testing
        # orig = os.environ["DISPLAY"]
        if os.getenv('BROWSER') == "CH":
            self.instance = webdriver.Remote(command_executor=self.GRID_URL,
                                            desired_capabilities=webdriver.DesiredCapabilities.CHROME
                                             )
        elif os.getenv('BROWSER') == "FF":
            self.instance = webdriver.Firefox(executable_path='./geckodriver.exe')
        elif os.getenv('BROWSER') == "OP":
            self.instance = webdriver.Opera(
                executable_path='./operadriver.exe')
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
        # self.display.stop()
