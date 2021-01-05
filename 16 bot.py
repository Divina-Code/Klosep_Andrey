import telebot
from myToken import ("1489351950:AAF5tFAj30coOwCoPImHl-K_AA1xYoCxLUQ")
from random import randint

bot = telebot.TeleBot("1489351950:AAF5tFAj30coOwCoPImHl-K_AA1xYoCxLUQ")


@bot.message_handler(commands=['start'])
def komanda_start(message):
    bot.send_message(message.chat.id, "Я умею много разного, например текстовые сообщения я разворачиваю задом наперёд")

@bot.message_handler(commands=['pass'])
def komanda_start(message):
    bot.send_message(message.chat.id, "Я сгенерирую тебе пароль из 4х цифр")
    rand_number = randint(1000, 9999)
    bot.send_message(message.chat.id, str(rand_number) )





@bot.message_handler(content_types=['text'])
def otvet_na_text(message):
    print(message)
    bot.send_message(message.chat.id, message.text[::-1])



