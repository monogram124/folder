import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot("6400448974:AAEhI-uuoUsnuLUJdLsblgeBzotrFpysJu4")

@bot.message_handler(commands=["start"]) # обработка команды
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("✏️Заполнить форму")
    btn2 = types.KeyboardButton("🌐Сайт House System")

    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в бота обратной связи!", reply_markup=markup)

    bot.register_next_step_handler(message, on_click)

@bot.message_handler()
def on_click(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("🐉E", callback_data="east")
    btn2 = types.InlineKeyboardButton("🦁W", callback_data="west")
    btn3 = types.InlineKeyboardButton("🐅S", callback_data="south")
    btn4 = types.InlineKeyboardButton("🐻‍❄️N", callback_data="north")
    
    if message.text == "✏️Заполнить форму":
        
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton("✅Готово"))
        
        bot.send_message(message.chat.id, "Имя Фамилия", reply_markup=markup)

    if message.text == "✅Готово" and message.text != "":
        # удаление из ReplyKeyboardMarkup кнопки "готово"

        markup.row(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Выберите House", reply_markup=markup)

    @bot.callback_query_handler(func=lambda callback: True)
    def callback_message(callback):
        markup = types.InlineKeyboardMarkup()
        
        house = ["east", "west", "north", "south"]
        exp = ["Опыт публичного выступления", "Социальный опыт", "Организаторский опыт", "Опыт творчества", "Опыт наставничества", "Спортивный опыт", "Опыт участника", "Академические достижения"]

        if callback.data in house: 
            btn1 = types.InlineKeyboardButton("Опыт публичного выступления", callback_data="Опыт публичного выступления")
            btn2 = types.InlineKeyboardButton("Социальный опыт", callback_data="Социальный опыт")
            btn3 = types.InlineKeyboardButton("Организаторский опыт", callback_data="Организаторский опыт")
            btn4 = types.InlineKeyboardButton("Опыт творчества", callback_data="Опыт творчества")
            btn5 = types.InlineKeyboardButton("Опыт наставничества", callback_data="Опыт наставничества")
            btn6 = types.InlineKeyboardButton("Спортивный опыт", callback_data="Спортивный опыт")
            btn7 = types.InlineKeyboardButton("Опыт участника", callback_data="Опыт участника")
            btn8 = types.InlineKeyboardButton("Академические достижения", callback_data="Академические достижения")

            markup.row(btn1)
            markup.row(btn2)
            markup.row(btn3)
            markup.row(btn4)
            markup.row(btn5)
            markup.row(btn6)
            markup.row(btn7)
            markup.row(btn8)

            bot.edit_message_text("Какой опыт ты получил?", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

        if callback.data in exp:
            btn1 = types.InlineKeyboardButton("5", callback_data=5)
            btn2 = types.InlineKeyboardButton("10", callback_data=10)
            btn3 = types.InlineKeyboardButton("15", callback_data=15)
            btn4 = None
            btn5 = None
            btn6 = None
            btn7 = None
            btn8 = None
            
            markup.row(btn1, btn2, btn3)
            
            bot.edit_message_text("Кол-во полученных баллов", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

        if callback.data == 5:
            bot.register_next_step_handler(message, on_click2)

        if callback.data == 10:
            pass

        if callback.data == 15:
            pass            
        
@bot.message_handler()
def on_click2(message):
    markup = types.ReplyKeyboardMarkup()
    rdy_btn = types.KeyboardButton()
    markup.row(rdy_btn)
    bot.send_message(message, "Что именно ты сделал?", reply_markup=markup)

    if message.text == "✅Готово":
        bot.send_message(message, "пиписи")
bot.polling(non_stop=True) # постоянное выполнение кода