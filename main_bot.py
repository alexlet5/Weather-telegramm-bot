import telebot
import random

import weather as we

bot = telebot.TeleBot('1450627779:AAHg-42ELxZ30z-dlIyhKX8T2qvQkSOqIw0')

users = []


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(
        message.chat.id, "Просто напишите точное имя города и бот напишет примерную погоду.")


@bot.message_handler(commands=['start'])
def start(message):
    get_help(message)


@bot.message_handler(content_types=['text'])
def weather(message):
    print(message.text)
    places_list = we.get_citys_list(message.text)
    if(len(places_list)):
        bot.send_message(message.chat.id, we.get_city_info(
            places_list, message.text))
    else:
        bot.send_message(message.chat.id, 'Города с названием "' +
                         message.text + '" не существует')


if __name__ == '__main__':
    bot.polling(none_stop=True)
