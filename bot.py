import os
import settings as settings
import telebot

bot = telebot.TeleBot(token = settings.BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(settings.USER_TOKEN, "Хельо, " + message.from_user.first_name)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.from_user.id, message.from_user.first_name + ", не базарь, а дай цьом Миколаїчу")


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_message(message.from_user.id, "Це Кора")



bot.infinity_polling()

