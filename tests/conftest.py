import os


def pytest_addoption(parser):
    parser.addoption('--u', action='store', default='', help='url environment address')
    parser.addoption('--lg', action='store', default='', help='user environment login')
    parser.addoption('--pwd', action='store', default='', help='user environment password')
    parser.addoption('--b', action='store', default='CH', help='browser')



def pytest_configure(config):
    os.environ['u'] = config.getoption('u')
    os.environ['lg'] = config.getoption('lg')
    os.environ['pwd'] = config.getoption('pwd')
    os.environ['b'] = config.getoption('b')