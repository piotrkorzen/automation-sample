import os
import allure
from allure_commons.types import AttachmentType
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--URL', action='store', default='', help='url environment address')
    parser.addoption('--LOGIN', action='store', default='', help='user environment login')
    parser.addoption('--PASSWORD', action='store', default='', help='user environment password')
    parser.addoption('--BROWSER', action='store', default='CH', help='browser')


def pytest_configure(config):
    os.environ['URL'] = config.getoption('URL')
    os.environ['LOGIN'] = config.getoption('LOGIN')
    os.environ['PASSWORD'] = config.getoption('PASSWORD')
    os.environ['BROWSER'] = config.getoption('BROWSER')


# def pytest_exception_interact(node, call, report):
#     """function for taking screenshot after failure and attach to allure report"""
#     driver = node.instance.driver
#     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#     allure.attach(driver.instance.get_screenshot_as_png(),
#                   name="{}".format(now),
#                   attachment_type=AttachmentType.PNG)
