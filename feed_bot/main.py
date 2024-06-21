import telebot
from telebot import types
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

user_form = {}

@bot.message_handler(commands=["start"])
def start(message):
    user_form[message.chat.id] = {"skills": ""}
    conn = sqlite3.connect("feed_bot.sql") 
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(50), house varchar(50), exp varchar(50), points varchar(5), done varchar(50), skills varchar(170), repeat varchar(3), exactly varchar(50), difficulties varchar(50), team_work varchar(50), motivation varchar(50), moment varchar(50), result varchar(2))")
    conn.commit()
    cur.close() 
    conn.close()


    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("✏️Заполнить форму")
    btn2 = types.KeyboardButton("🌐Сайт House System")

    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в бота обратной связи! Чтобы отправить ответы, написанные от руки необходимо нажать кнопку 'Готово'", reply_markup=markup)

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
        bot.register_next_step_handler(message, user_name)
    
    if message.text == "🙅‍♂️Отменить":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("✏️Заполнить форму")
        btn2 = types.KeyboardButton("🌐Сайт House System")

        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, f"{message.from_user.first_name}, добро пожаловать в бота обратной связи!", reply_markup=markup)
    
    if message.text == "📩Отправить":
        conn = sqlite3.connect("feed_bot.sql")
        cur = conn.cursor()

        if user_form[message.chat.id]["points"] == "5":
            cur.execute(f"INSERT INTO users (name, house, exp, points, done, skills, repeat, result) VALUES ('{user_form[message.chat.id]['name']}', '{user_form[message.chat.id]['house']}', '{user_form[message.chat.id]['exp']}', '{user_form[message.chat.id]['points']}', '{user_form[message.chat.id]['done']}', '{user_form[message.chat.id]['skills']}', '{user_form[message.chat.id]['repeat']}', '{user_form[message.chat.id]['result']}')")
        elif user_form[message.chat.id]["points"] == "10":
            cur.execute(f"INSERT INTO users (name, house, exp, points, done, skills, exactly, difficulties, team_work, result) VALUES ('{user_form[message.chat.id]['name']}', '{user_form[message.chat.id]['house']}', '{user_form[message.chat.id]['exp']}', '{user_form[message.chat.id]['points']}', '{user_form[message.chat.id]['done']}', '{user_form[message.chat.id]['skills']}', '{user_form[message.chat.id]['exactly']}', '{user_form[message.chat.id]['difficulties']}', '{user_form[message.chat.id]['team_work']}', '{user_form[message.chat.id]['result']}')")
        elif user_form[message.chat.id]["points"] == "15":
            cur.execute(f"INSERT INTO users (name, house, exp, points, done, skills, exactly, difficulties, team_work, motivation, moment, result) VALUES ('{user_form[message.chat.id]['name']}', '{user_form[message.chat.id]['house']}', '{user_form[message.chat.id]['exp']}', '{user_form[message.chat.id]['points']}', '{user_form[message.chat.id]['done']}', '{user_form[message.chat.id]['skills']}', '{user_form[message.chat.id]['exactly']}', '{user_form[message.chat.id]['difficulties']}', '{user_form[message.chat.id]['team_work']}', '{user_form[message.chat.id]['motivation']}', '{user_form[message.chat.id]['moment']}', '{user_form[message.chat.id]['result']}')")

        conn.commit()
        cur.close()
        conn.close() 

        # print(user_form)
        user_form[message.chat.id] = {"skills": ""}

        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("✏️Заполнить форму")
        btn2 = types.KeyboardButton("🌐Сайт House System")

        markup.add(btn1, btn2)

        bot.send_message(message.chat.id, "Форма успешно отправлена!", reply_markup=markup)

    if message.text == "✅Готово" and message.text != "":
        markup.row(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, "Выберите House", reply_markup=markup)

def user_name(message):
    user_form[message.chat.id]['name'] = message.text

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):

    markup = types.InlineKeyboardMarkup()
    
    house = ["east", "west", "north", "south"]
    exp = ["Опыт публичного выступления", "Социальный опыт", "Организаторский опыт", "Опыт творчества", "Опыт наставничества", "Спортивный опыт", "Опыт участника"]

    if callback.data in house:
        
        user_form[callback.message.chat.id]['house'] = callback.data

        btn1 = types.InlineKeyboardButton("Опыт публичного выступления", callback_data="Опыт публичного выступления")
        btn2 = types.InlineKeyboardButton("Социальный опыт", callback_data="Социальный опыт")
        btn3 = types.InlineKeyboardButton("Организаторский опыт", callback_data="Организаторский опыт")
        btn4 = types.InlineKeyboardButton("Опыт творчества", callback_data="Опыт творчества")
        btn5 = types.InlineKeyboardButton("Опыт наставничества", callback_data="Опыт наставничества")
        btn6 = types.InlineKeyboardButton("Спортивный опыт", callback_data="Спортивный опыт")
        btn7 = types.InlineKeyboardButton("Опыт участника", callback_data="Опыт участника")
        
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        markup.row(btn4)
        markup.row(btn5)
        markup.row(btn6)
        markup.row(btn7)

        bot.edit_message_text("Какой опыт ты получил?", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data in exp:
        user_form[callback.message.chat.id]['exp'] = callback.data

        btn1 = types.InlineKeyboardButton("5", callback_data="5")
        btn2 = types.InlineKeyboardButton("10", callback_data="10")
        btn3 = types.InlineKeyboardButton("15", callback_data="15")
        
        markup.row(btn1, btn2, btn3)

        bot.edit_message_text("Кол-во полученных баллов", callback.message.chat.id, callback.message.message_id, reply_markup=markup)

    if callback.data == "5":
        user_form[callback.message.chat.id]['points'] = callback.data

        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)

        bot.send_message(callback.message.chat.id, "Что именно ты сделал?", reply_markup=markup)
        
        bot.register_next_step_handler(callback.message, mid_on_click5)
        
    btns = ["Мыслить", "Коммуницировать", "Уметь-рисковать", "Быть-гибким", "Быть-упорным", "Командная-работа", "Уметь-планировать", "Глобальное-мышление", "Этические-нормы", "Принимать-решения", "Ответственность-решение", "Сильные-стороны", "Эффективность"]
    
    callback_text = {
        "Мыслить": "Мыслить",
        "Коммуницировать": "Коммуницировать, ",
        "Уметь-рисковать": "Уметь рисковать, ",
        "Быть-гибким": "Быть гибким, ",
        "Быть-упорным": "Быть упорным, ",
        "Командная-работа": "Работать в команде, ",
        "Уметь-планировать": "Уметь планировать, ",
        "Глобальное-мышление": "Осознавать важность глобального мышления, ",
        "Этические-нормы": "Осознавать важность этических норм, ",
        "Принимать-решения": "Уметь принимать решения, ",
        "Ответственность-решение": "Нести за отвественность за свои решения, ",
        "Сильные-стороны": "Оценивать сильные стороны и точки роста, ",
        "Эффективность": "Верить в собственную эффективность, "
    }

    if callback.data in btns:
        user_form[callback.message.chat.id]["skills"] += callback_text[callback.data]
        # print(user_form)
        
    if callback.data == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton("Да", callback_data="Да")
        no = types.InlineKeyboardButton("Нет", callback_data="Нет")
        markup.row(yes, no)

        bot.send_message(callback.message.chat.id, f"Хотел бы ты повторить этот опыт/посоветовать его другу?", reply_markup=markup)
        
    if callback.data == "✅Готов":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("✅Готово")

        markup.row(btn1)

        bot.send_message(callback.message.chat.id, "Как именно ты прокачал выбранный скил (или скилы)?", reply_markup=markup)
        bot.register_next_step_handler(callback.message, mid_on_click10_skills)

    team_work = ["удалась", "не-удалась", "не-относится"]

    if callback.data == "Да" or callback.data == "Нет":
        user_form[callback.message.chat.id]['repeat'] = callback.data
        
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("👎1", callback_data="1rate")
        btn2 = types.InlineKeyboardButton("2", callback_data="2rate")
        btn3 = types.InlineKeyboardButton("3", callback_data="3rate")
        btn4 = types.InlineKeyboardButton("4", callback_data="4rate")
        btn5 = types.InlineKeyboardButton("5", callback_data="5rate")
        btn6 = types.InlineKeyboardButton("6", callback_data="6rate")
        btn7 = types.InlineKeyboardButton("7", callback_data="7rate")
        btn8 = types.InlineKeyboardButton("8", callback_data="8rate")
        btn9 = types.InlineKeyboardButton("9", callback_data="9rate")
        btn10 = types.InlineKeyboardButton("🌟10", callback_data="10rate")
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7, btn8, btn9)
        markup.row(btn10)   

        bot.send_message(callback.message.chat.id, "Оцени как ты справился с этим опытом по 10-бальной шкале", reply_markup=markup)

    if callback.data in team_work:
        user_form[callback.message.chat.id]['team_work'] = callback.data


        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("👎1", callback_data="1rate")
        btn2= types.InlineKeyboardButton("2", callback_data="2rate")
        btn3 = types.InlineKeyboardButton("3", callback_data="3rate")
        btn4 = types.InlineKeyboardButton("4", callback_data="4rate")
        btn5 = types.InlineKeyboardButton("5", callback_data="5rate")
        btn6 = types.InlineKeyboardButton("6", callback_data="6rate")
        btn7 = types.InlineKeyboardButton("7", callback_data="7rate")
        btn8 = types.InlineKeyboardButton("8", callback_data="8rate")
        btn9 = types.InlineKeyboardButton("9", callback_data="9rate")
        btn10 = types.InlineKeyboardButton("🌟10", callback_data="10rate")
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7, btn8, btn9)
        markup.row(btn10)   

        bot.send_message(callback.message.chat.id, "Оцени как ты справился с этим опытом по 10-бальной шкале", reply_markup=markup)


    rates = ["1rate","2rate","3rate","4rate","5rate","6rate","7rate","8rate","9rate","10rate",]            

    if callback.data in rates:
        user_form[callback.message.chat.id]['result'] = callback.data

        markup = types.ReplyKeyboardMarkup()
        send = types.KeyboardButton("📩Отправить")
        cancel = types.KeyboardButton("🙅‍♂️Отменить")
        
        markup.row(send, cancel)
        

        bot.send_message(callback.message.chat.id, "Отправить форму?", reply_markup=markup)
        
        bot.register_next_step_handler(callback.message, on_click)
    
    if callback.data == "10":
        user_form[callback.message.chat.id]['points'] = callback.data

        
        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)

        bot.send_message(callback.message.chat.id, "Что именно ты сделал?", reply_markup=markup)

        bot.register_next_step_handler(callback.message, mid_on_click10)

    if callback.data == "15":
        user_form[callback.message.chat.id]['points'] = callback.data

        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)
        bot.send_message(callback.message.chat.id, "Что именно ты сделал?", reply_markup=markup)

        bot.register_next_step_handler(callback.message, mid_on_click15)

    if callback.data == "✅Я готов":
        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)
        bot.send_message(callback.message.chat.id, "Как именно ты прокачал выбранный скил (или скилы)?", reply_markup=markup)

        bot.register_next_step_handler(callback.message, mid_on_click15_skills)

    team_work_15 = ["удалась-15", "не-удалась-15", "не-относится-15"]

    if callback.data in team_work_15:
        user_form[callback.message.chat.id]['team_work'] = callback.data

        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("👎1", callback_data="1rate")
        btn2= types.InlineKeyboardButton("2", callback_data="2rate")
        btn3 = types.InlineKeyboardButton("3", callback_data="3rate")
        btn4 = types.InlineKeyboardButton("4", callback_data="4rate")
        btn5 = types.InlineKeyboardButton("5", callback_data="5rate")
        btn6 = types.InlineKeyboardButton("6", callback_data="6rate")
        btn7 = types.InlineKeyboardButton("7", callback_data="7rate")
        btn8 = types.InlineKeyboardButton("8", callback_data="8rate")
        btn9 = types.InlineKeyboardButton("9", callback_data="9rate")
        btn10 = types.InlineKeyboardButton("🌟10", callback_data="10rate")
        markup.row(btn1, btn2, btn3)
        markup.row(btn4, btn5, btn6)
        markup.row(btn7, btn8, btn9)
        markup.row(btn10)   

        bot.send_message(callback.message.chat.id, "Оцени как ты справился с этим опытом по 10-бальной шкале", reply_markup=markup)

@bot.message_handler()
def mid_on_click5(message):
    user_form[message.chat.id]['done'] = message.text
    
    if message.text != "":
        bot.register_next_step_handler(message, on_click5)

@bot.message_handler()
def mid_on_click10(message):
    user_form[message.chat.id]['done'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click10)

@bot.message_handler()
def mid_on_click10_skills(message):
    user_form[message.chat.id]['exactly'] = message.text
  
    if message.text != "":    
        bot.register_next_step_handler(message, on_click10_skills)

@bot.message_handler()
def mid_on_click15(message):
    user_form[message.chat.id]['done'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click15)

@bot.message_handler()
def mid_on_click15_skills(message):
    user_form[message.chat.id]['exactly'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click15_skills)

@bot.message_handler()
def on_click15_skills(message):
    if message.text == "✅Готово":
        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)

        bot.send_message(message.chat.id, "Столкнулся ли ты со сложностями при планировании или во время реализации опыта?", reply_markup=markup)
        bot.register_next_step_handler(message, mid_on_click15_difficult)

@bot.message_handler()
def mid_on_click15_difficult(message):
    user_form[message.chat.id]['difficulties'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click15_difficult)

@bot.message_handler()
def on_click15_difficult(message):
    if message.text == "✅Готово":
        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)

        bot.send_message(message.chat.id, "Что стало мотивацией для реализации опыта?", reply_markup=markup)
        bot.register_next_step_handler(message, mid_on_click15_motivation)

@bot.message_handler()
def mid_on_click15_motivation(message):
    user_form[message.chat.id]['motivation'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click15_motivation)

@bot.message_handler()
def on_click15_motivation(message):
    if message.text == "✅Готово":
        markup = types.ReplyKeyboardMarkup()
        rdy_btn = types.KeyboardButton("✅Готово")

        markup.add(rdy_btn)
        
        bot.send_message(message.chat.id, "Опиши свой самый успешный момент в работе")
        bot.register_next_step_handler(message, mid_on_click15_success)

@bot.message_handler()
def mid_on_click15_success(message):
    user_form[message.chat.id]['moment'] = message.text
    
    if message.text != "":
        bot.register_next_step_handler(message, on_click15_success)

@bot.message_handler()
def on_click15_success(message):
    if message.text == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("К этому опыту не относится", callback_data="не-относится-15")
        btn2 = types.InlineKeyboardButton("Работа в команде не удалась", callback_data="не-удалась-15")
        btn3 = types.InlineKeyboardButton("Работа в команде удалась", callback_data="удалась-15")

        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        
        bot.send_message(message.chat.id, "Удалось ли поработать в команде?", reply_markup=markup)

@bot.message_handler()
def on_click15(message):
    if message.text == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Мыслить", callback_data="Мыслить")
        btn2 = types.InlineKeyboardButton("Коммуницировать", callback_data="Коммуницировать")
        btn3 = types.InlineKeyboardButton("Уметь рисковать", callback_data="Уметь-рисковать")
        btn4 = types.InlineKeyboardButton("Быть гибким", callback_data="Быть-гибким")
        btn5 = types.InlineKeyboardButton("Быть упорным", callback_data="Быть-упорным")
        btn6 = types.InlineKeyboardButton("Работать в команде", callback_data="Командная-работа")
        btn7 = types.InlineKeyboardButton("Уметь планировать", callback_data="Уметь-планировать")
        btn8 = types.InlineKeyboardButton("Осознавать важность глобального мышления", callback_data="Глобальное-мышление")
        btn9 = types.InlineKeyboardButton("Осознавать важность этических норм", callback_data="Этические-нормы")
        btn10 = types.InlineKeyboardButton("Уметь принимать решения", callback_data="Принимать-решения")
        btn11 = types.InlineKeyboardButton("Нести ответственность за решение", callback_data="Ответственность-решение")
        btn12 = types.InlineKeyboardButton("Оценивать сильные стороны и точки роста", callback_data="Сильные-стороны")
        btn13 = types.InlineKeyboardButton("Верить в собственную эффективность", callback_data="Эффективность")
        btn14 = types.InlineKeyboardButton("✅Я готов", callback_data="✅Я готов")
        
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
        markup.row(btn14)
        
        bot.send_message(message.chat.id, "Какой/какие skill/skills удалось прокачать во время планирования и реализации опыта?", reply_markup=markup)

@bot.message_handler()
def on_click10_skills(message):
    if message.text == "✅Готово":
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton("✅Готово")

        markup.row(btn1)

        bot.send_message(message.chat.id, "Столкнулся ли ты со сложностями при планировании или во время реализации опыта? Опиши их и как с ними справился", reply_markup=markup)
        bot.register_next_step_handler(message, mid_on_click10_difficult)

@bot.message_handler()
def mid_on_click10_difficult(message):
    user_form[message.chat.id]['difficulties'] = message.text

    if message.text != "":
        bot.register_next_step_handler(message, on_click10_difficult)

@bot.message_handler()
def on_click10_difficult(message):
    if message.text == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("К этому опыту не относится", callback_data="не-относится")
        btn2 = types.InlineKeyboardButton("Работа в команде не удалась", callback_data="не-удалась")
        btn3 = types.InlineKeyboardButton("Работа в команде удалась", callback_data="удалась")

        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)

        bot.send_message(message.chat.id, "Удалась ли работа в команде", reply_markup=markup)

@bot.message_handler()
def on_click10(message):
    if message.text == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Мыслить", callback_data="Мыслить")
        btn2 = types.InlineKeyboardButton("Коммуницировать", callback_data="Коммуницировать")
        btn3 = types.InlineKeyboardButton("Уметь рисковать", callback_data="Уметь-рисковать")
        btn4 = types.InlineKeyboardButton("Быть гибким", callback_data="Быть-гибким")
        btn5 = types.InlineKeyboardButton("Быть упорным", callback_data="Быть-упорным")
        btn6 = types.InlineKeyboardButton("Работать в команде", callback_data="Командная-работа")
        btn7 = types.InlineKeyboardButton("Уметь планировать", callback_data="Уметь-планировать")
        btn8 = types.InlineKeyboardButton("Осознавать важность глобального мышления", callback_data="Глобальное-мышление")
        btn9 = types.InlineKeyboardButton("Осознавать важность этических норм", callback_data="Этические-нормы")
        btn10 = types.InlineKeyboardButton("Уметь принимать решения", callback_data="Принимать-решения")
        btn11 = types.InlineKeyboardButton("Нести ответственность за решение", callback_data="Ответственность-решение")
        btn12 = types.InlineKeyboardButton("Оценивать сильные стороны и точки роста", callback_data="Сильные-стороны")
        btn13 = types.InlineKeyboardButton("Верить в собственную эффективность", callback_data="Эффективность")
        btn14 = types.InlineKeyboardButton("✅Готов", callback_data="✅Готов")
        
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
        markup.row(btn14)
        
        bot.send_message(message.chat.id, "Какой/какие skill/skills удалось прокачать во время планирования и реализации опыта?", reply_markup=markup)

@bot.message_handler()
def on_click5(message):
    if message.text == "✅Готово":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Мыслить", callback_data="Мыслить")
        btn2 = types.InlineKeyboardButton("Коммуницировать", callback_data="Коммуницировать")
        btn3 = types.InlineKeyboardButton("Уметь рисковать", callback_data="Уметь-рисковать")
        btn4 = types.InlineKeyboardButton("Быть гибким", callback_data="Быть-гибким")
        btn5 = types.InlineKeyboardButton("Быть упорным", callback_data="Быть-упорным")
        btn6 = types.InlineKeyboardButton("Работать в команде", callback_data="Командная-работа")
        btn7 = types.InlineKeyboardButton("Уметь планировать", callback_data="Уметь-планировать")
        btn8 = types.InlineKeyboardButton("Осознавать важность глобального мышления", callback_data="Глобальное-мышление")
        btn9 = types.InlineKeyboardButton("Осознавать важность этических норм", callback_data="Этические-нормы")
        btn10 = types.InlineKeyboardButton("Уметь принимать решения", callback_data="Принимать-решения")
        btn11 = types.InlineKeyboardButton("Нести ответственность за решение", callback_data="Ответственность-решение")
        btn12 = types.InlineKeyboardButton("Оценивать сильные стороны и точки роста", callback_data="Сильные-стороны")
        btn13 = types.InlineKeyboardButton("Верить в собственную эффективность", callback_data="Эффективность")
        btn14 = types.InlineKeyboardButton("✅Готово", callback_data="✅Готово")
        
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
        markup.row(btn14)

        bot.send_message(message.chat.id, "Какой/какие skill/skills удалось прокачать во время планирования и реализации опыта?", reply_markup=markup)

bot.polling(non_stop=True)