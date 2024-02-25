import telebot

bot = telebot.TeleBot("7077312345:AAGTxtP3olNJ9jQbuWAS5sQCZCbYlNx1h5k")

@bot.message_handler(commands=["start"])
def start(message):
    file = open("pick_a_sign.png", "rb")
    bot.send_photo(message.chat.id, file, caption="Это фото")

bot.polling()