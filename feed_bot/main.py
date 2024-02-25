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
            btn1 = types.InlineKeyboardButton("5", callback_data="5")
            btn2 = types.InlineKeyboardButton("10", callback_data="10")
            btn3 = types.InlineKeyboardButton("15", callback_data="15")
            
            markup.row(btn1, btn2, btn3)
            
            bot.edit_message_text("Кол-во полученных баллов", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

        if callback.data == "5":
            markup = types.ReplyKeyboardMarkup()
            rdy_btn = types.KeyboardButton("✅Готово")

            markup.add(rdy_btn)

            bot.send_message(message.chat.id, "Что именно ты сделал?", reply_markup=markup)

            bot.register_next_step_handler(message, mid_on_click)

        if callback.data == "10":
            pass

        if callback.data == "15":
            pass            
        
@bot.message_handler()
def mid_on_click(message):
    if message.text != " ":
        bot.register_next_step_handler(message, on_click3)
    
@bot.message_handler()
def on_click3(message):
    if message.text == "✅Готово":

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Мыслить", callback_data="Мыслить")
        btn2 = types.InlineKeyboardButton("Коммуницировать", callback_data="Коммуницировать")
        btn3 = types.InlineKeyboardButton("Уметь рисковать", callback_data="Уметь-рисковать")
        btn4 = types.InlineKeyboardButton("Быть гибким", callback_data="Быть-гибким")
        btn5 = types.InlineKeyboardButton("Быть упорным", callback_data="Быть-упорным")
        btn6 = types.InlineKeyboardButton("Работать в команде", callback_data="Командная-работа")
        btn7 = types.InlineKeyboardButton("Уметь планировать", callback_data="Уметь-планировать")
        btn8 = types.InlineKeyboardButton("Осознавать важноть глобального мышления", callback_data="Глобальное-мышление")
        btn9 = types.InlineKeyboardButton("Осознавать важность этических норм", callback_data="Этические-нормы")
        btn10 = types.InlineKeyboardButton("Уметь принимать решения", callback_data="Принимать-решения")
        btn11 = types.InlineKeyboardButton("Нести ответственность за решение", callback_data="Ответственность-решение")
        btn12 = types.InlineKeyboardButton("Оценивать сильные стороны и точки роста", callback_data="Сильные-стороны")
        btn13 = types.InlineKeyboardButton("Верить в собственную эффективность", callback_data="Эффективность")
        
        btns = ["Мыслить", "Коммуницировать", "Уметь-рисковать", "Быть-гибким", "Быть-упорным", "Командная-работа", "Уметь-планировать", "Глобальное-мышление", "Этические-нормы", "Принимать-решения", "Ответственность-решение", "Сильные-стороны", "Эффективность"]
        
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn6)
        markup.row(btn7)
        markup.row(btn8)
        markup.row(btn9)
        markup.row(btn10)
        markup.row(btn11)
        markup.row(btn12)
        markup.row(btn13)
        
        bot.send_message(message.chat.id, "Какой/какие skill/skills удалось прокачать во время планирования и реализации опыта?", reply_markup=markup)
        btns_callbacks = {
            btn1.callback_data: btn1.text,
            btn2.callback_data: btn2.text,
            btn3.callback_data: btn3.text,
            btn4.callback_data: btn4.text,
            btn5.callback_data: btn5.text,
            btn6.callback_data: btn6.text,
            btn7.callback_data: btn7.text,
            btn8.callback_data: btn8.text,
            btn9.callback_data: btn9.text,
            btn10.callback_data: btn10.text,
            btn11.callback_data: btn11.text,
            btn12.callback_data: btn12.text,
            btn13.callback_data: btn13.text,
        }

        @bot.callback_query_handler(func=lambda callback: True)
        def callback_message2(callback):
            btns_callbacks = {
            btn1.callback_data: btn1.text,
            btn2.callback_data: btn2.text,
            btn3.callback_data: btn3.text,
            btn4.callback_data: btn4.text,
            btn5.callback_data: btn5.text,
            btn6.callback_data: btn6.text,
            btn7.callback_data: btn7.text,
            btn8.callback_data: btn8.text,
            btn9.callback_data: btn9.text,
            btn10.callback_data: btn10.text,
            btn11.callback_data: btn11.text,
            btn12.callback_data: btn12.text,
            btn13.callback_data: btn13.text,
            }
            if callback.data == "Мыслить":
                print(btns_callbacks) # по сути я обращаюсь по колбеку к тексту первой кнопки и должен получить "Мыслить"

bot.polling(non_stop=True) # постоянное выполнение кода