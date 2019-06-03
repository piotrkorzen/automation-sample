import os


def pytest_addoption(parser):
    parser.addoption('--u', action='store', default='', help='url environment address')
    parser.addoption('--lg', action='store', default='', help='user environment login')
    parser.addoption('--pwd', action='store', default='', help='user environment password')
    parser.addoption('--ack', action='store', default='', help='api customer key')
    parser.addoption('--alog', action='store', default='', help='api authorization login')
    parser.addoption('--ap', action='store', default='', help='api authorization password')
    parser.addoption('--loops', action='store', default='', help='amount of loops in tests or tools')


def pytest_configure(config):
    os.environ['u'] = config.getoption('u')
    os.environ['lg'] = config.getoption('lg')
    os.environ['pwd'] = config.getoption('pwd')
    os.environ['ack'] = config.getoption('ack')
    os.environ['alog'] = config.getoption('alog')
    os.environ['ap'] = config.getoption('ap')
    os.environ['loops'] = config.getoption('loops')