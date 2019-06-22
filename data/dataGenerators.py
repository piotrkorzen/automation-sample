import random
import string
import csv

domains = ["xyz.com", "123.abc", "asd.zxc", "qwerty.dot", "dot.com"]


def mail_generator():
    random_string = ''.join([random.choice(string.ascii_lowercase + string.digits) for n in range(16)])
    random_mail = random_string + "@" + random.choice(domains)
    return random_mail


name_list = []


def name_generator():
    with open("./automationpractice.com/data/files/users.csv") as csv_names:
        csv_reader = csv.DictReader(csv_names)
        for name in csv_reader:
            name_list.append(name['First Name'])
        random_name = random.choice(name_list)
        return random_name


surname_list = []


def surname_generator():
    with open("./automationpractice.com/data/files/users.csv") as csv_names:
        csv_reader = csv.DictReader(csv_names)
        for surname in csv_reader:
            surname_list.append(surname['Last Name'])
        random_surname = random.choice(surname_list)
        return random_surname


password_list = []


def password_generator():
    random_password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
    return random_password
