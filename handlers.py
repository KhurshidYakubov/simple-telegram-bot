from telegram import ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ConversationHandler

from utility import *


def sms(bot, update):
    print('Kto-to napisal start')
    bot.message.reply_text('Здравсвуйте {}!'.format(bot.message.chat.first_name), reply_markup=get_keyboard())


def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def anketa_start(bot, update):
    bot.message.reply_text('Как вас зовут?', reply_markup=ReplyKeyboardRemove())
    return "user_name"


def anketa_get_name(bot, update):
    update.user_data['name'] = bot.message.text  # временно сохраняем ответ
    location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    bot.message.reply_text("Отправьте локацию", reply_markup=ReplyKeyboardMarkup(
        [[location_button]], resize_keyboard=True))
    return "user_location"  # ключ для определения следующего шага


def anketa_get_location(bot, update):
    update.user_data['location'] = bot.message.location
    contact_button = KeyboardButton('Отправить номер', request_contact=True)
    bot.message.reply_text("Отправьте ваш контактный номер :)", reply_markup=ReplyKeyboardMarkup(
        [[contact_button]], resize_keyboard=True))

    return "user_contact"


def anketa_get_contact(bot, update):
    update.user_data['phone_number'] = bot.message.contact
    reply_keyboard = [["Пропустить"]]  # создаем клавиатуру
    bot.message.reply_text("Напишите комментарий для заказа или нажмите кнопку пропустить.",
                           reply_markup=ReplyKeyboardMarkup(
                               reply_keyboard, resize_keyboard=True, one_time_keyboard=True))  # клава исчезает

    return "comment"


def anketa_comment(bot, update):
    update.user_data['comment'] = bot.message.text  # временно сохраняем ответ
    bot.message.reply_text("Регистрация завершена теперь можете заказать!",
                           reply_markup=get_keyboard_order())  # сообщение и возвр. осн. клаву
    return ConversationHandler.END  # выходим из диалога


def anketa_exit_comment(bot, update):
    update.user_data['comment'] = None
    bot.message.reply_text("Регистрация завершена теперь можете заказать!",
                           reply_markup=get_keyboard_order())  # отправляем сообщение и возвращаем осн. клаву
    return ConversationHandler.END  # выходим из диалога


def dontknow(bot, update):
    bot.message.reply_text("Я вас не понимаю, выберите оценку на клавиатуре!")


def restoran_list(update, context):
    keyboard = [[InlineKeyboardButton("Baraka", callback_data='1'),
                 InlineKeyboardButton("Chinor", callback_data='2')],

                [InlineKeyboardButton("The Best", callback_data='3'),
                 InlineKeyboardButton("Стейкхус", callback_data='4')],

                [InlineKeyboardButton("Bella Italia", callback_data='5'),
                 InlineKeyboardButton("Bon Bon", callback_data='6')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выбирайте откуда вы хотите заказать еду:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    query.answer()

    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('images/{}.jpg'.format(query.data), 'rb'))


def image(bot, update):
    update.bot.send_photo(chat_id=bot.message.chat.id, photo=open('images/1.jpg', 'rb'))
