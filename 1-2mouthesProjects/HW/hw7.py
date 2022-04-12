import re


class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.color = value


with open('MOCK_DATA.txt', 'r') as text:
    filenpars = text.read()


def find_color():
    color_finder = re.findall('#.*', filenpars)
    for i in color_finder:
        return f'{i}'


def find_email():
    email_finder = re.findall('(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})', filenpars)
    for i in email_finder:
        return f'{i}'


def find_file():
    file_finder = re.findall('\t\w[A-Za-z ]+?\.[a-zA-Z].*\t', filenpars)
    for i in file_finder:
        return f'{i}'


def find_name():
    name_finder = re.findall('^[A-Z-]+\t[A-Z-*.]+', filenpars)
    for i in name_finder:
        return f'{i}'

print(f'{find_color()}, {find_email()}, {find_file()}, {find_name()}')
