import os


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
