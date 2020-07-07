import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from settings import TG_TOKEN, TG_API_URL
from handlers import *

logging.basicConfig()  # for showing an errors in console


def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(
        ConversationHandler(entry_points=[MessageHandler(Filters.regex('Заполнить анкету'), anketa_start)],
                            states={
                                "user_name": [MessageHandler(Filters.text, anketa_get_name)],
                                "user_location": [MessageHandler(Filters.location, anketa_get_location)],
                                "user_contact": [MessageHandler(Filters.contact, anketa_get_contact)],
                                "comment": [MessageHandler(Filters.regex('Пропустить'), anketa_exit_comment),
                                            MessageHandler(Filters.text, anketa_comment)],
                            },
                            fallbacks=[MessageHandler(
                                Filters.text | Filters.video | Filters.photo | Filters.document, dontknow)]
                            )
    )
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Рестораны'), restoran_list))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Картинка'), image))
    my_bot.dispatcher.add_handler(CallbackQueryHandler(button))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
