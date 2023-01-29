from faker import Faker
from random import choice, randint


mailboxes = ["@gmail.com", "@ukr.net", "@ithillel.ua", "@business.com"]


class Human:
    def __init__(self):
        self.name = Faker().first_name()
        self.age = randint(10, 80)


def generate_one_human():
    return Human()


def generate_humans(amount=100):
    for _ in range(amount):
        yield generate_one_human()


def users_generator(amount=100):
    for _ in range(amount):
        yield f"{generate_one_human().name}{choice(mailboxes)}"
