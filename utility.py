from telegram import ReplyKeyboardMarkup


def get_keyboard():
    my_keyboard = ReplyKeyboardMarkup([['Заполнить анкету']], resize_keyboard=True)
    return my_keyboard


def get_keyboard_order():
    order = ReplyKeyboardMarkup([['Рестораны']], resize_keyboard=True)
    return order
