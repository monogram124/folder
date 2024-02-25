import telebot
from telebot import types
import random

bot = telebot.TeleBot("6398602578:AAHownULBZ77SackdjTyGa0oFf63uvLsO9Q")

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("🎮Играть")
    markup.add(btn1)

    photo = open("img/menu.png", "rb")
    bot.send_photo(message.chat.id, photo, caption=f"{message.from_user.first_name} привет! Ты попал в бота для игры в камень ножницы бумага, нажми '🎮Играть' чтобы начать", reply_markup=markup)

    bot.register_next_step_handler(message, on_click)
    
@bot.message_handler()
def on_click(message):
    signs = ["🪨", "✂️", "📄"]
 
    if message.text == "🎮Играть":

        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton(f"{signs[0]}")
        btn2 = types.KeyboardButton(f"{signs[1]}")
        btn3 = types.KeyboardButton(f"{signs[2]}")
        btn4 = types.KeyboardButton("🔙Назад")

        markup.row(btn1, btn2, btn3)
        markup.row(btn4)
        
        photo = open("img/pick_a_sign.png", "rb")
        bot.send_photo(message.chat.id, photo, caption="Выбери знак", reply_markup=markup)
    
    if message.text == "🔙Назад":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("🎮Играть")
        markup.add(btn1)

        photo = open("img/menu.png", "rb")
        bot.send_photo(message.chat.id, photo, caption=f"{message.from_user.first_name} привет! Ты попал в бота для игры в камень ножницы бумага, нажми '🎮Играть' чтобы начать", reply_markup=markup)

    if message.text in signs:
        player_sign = message.text
        bot_sign = random.choice(signs)
        print(player_sign, bot_sign, message.from_user.first_name, message.from_user.username)

        if player_sign == signs[0] and bot_sign == signs[2]:
            bot.send_message(message.chat.id, f"{signs[2]}❌")
        elif player_sign == signs[0] and bot_sign == signs[1]:
            bot.send_message(message.chat.id, f"{signs[1]}✅")
        
        if player_sign == signs[2] and bot_sign == signs[0]:
            bot.send_message(message.chat.id, f"{signs[0]}✅")
        elif player_sign == signs[2] and bot_sign == signs[1]:
            bot.send_message(message.chat.id, f"{signs[1]}❌")
        
        if player_sign == signs[1] and bot_sign == signs[2]:
            bot.send_message(message.chat.id, f"{signs[2]}✅")
        elif player_sign == signs[1] and bot_sign == signs[0]:
            bot.send_message(message.chat.id, f"{signs[0]}❌")

        if player_sign == bot_sign:
            bot.send_message(message.chat.id, f"{bot_sign}🏳")

bot.polling(non_stop=True)