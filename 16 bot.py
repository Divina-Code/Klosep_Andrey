import telebot

bot = telebot.Telebot("1489351950:AAF5tFAj30coOwCoPImHl-K_AA1xYoCxLUQ")

@bot.message_handler(content_types=['text'])
def otvet_na_text(messege):
    print(messege)
    bot.send_messange(messange.chat.id,"Hellow")


bot.polling()


