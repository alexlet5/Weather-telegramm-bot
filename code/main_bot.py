import telebot
import random
import pyowm.commons.exceptions as ex
import re

import weather as we

bot = telebot.TeleBot('1450627779:AAHg-42ELxZ30z-dlIyhKX8T2qvQkSOqIw0')


def text_shortener(text):
    if(len(text) > 20):
        return text[0:19] + "..."
    return text


def cheking_message(message):
    if re.fullmatch('[0-9]*', message):
        bot.send_message(message.chat.id, 'Некоректное название города.')
        return False
    return True


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(
        message.chat.id, "Просто напишите точное имя города на русском языке и бот напишет примерную погоду.")


@bot.message_handler(commands=['start'])
def start(message):
    get_help(message)


@bot.message_handler(content_types=['text'])
def weather(message):
    print(message.text + " - " + str(len(message.text)))

    if not cheking_message(message.text):
        return

    places_list = []

    text = text_shortener(message.text)

    try:
        places_list = we.get_citys_list(text, 'accurate')
    except ex.APIRequestError:
        bot.send_message(message.chat.id, "Некоректное название города.")
        return

    if(not len(places_list)):
        bot.send_message(message.chat.id, 'Города с названием "' +
                         text + '" не существует')
        return

    bot.send_message(message.chat.id, we.get_city_info(
        places_list, text), parse_mode='Markdown')


if __name__ == '__main__':
    bot.polling(none_stop=True)
