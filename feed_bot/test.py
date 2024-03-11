import telebot
from telebot import types

bot = telebot.TeleBot("6458395338:AAFPgbM4e2Htyt3M5LLIIokHssSNU5c7jnk")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Готово":
        send_buttons(message.chat.id)

def send_buttons(chat_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("Мыслить", callback_data="Мыслить")
    btn2 = types.InlineKeyboardButton("Коммуницировать", callback_data="Коммуницировать")
    # Добавьте остальные кнопки
    markup.add(btn1, btn2)  # Добавьте остальные кнопки здесь

    bot.send_message(chat_id, "Выберите один из вариантов:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    bot.answer_callback_query(call.id)
    # Добавляем галочку к тексту кнопки
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=f"✅{call.data}" if call.data not in call.message.text else call.message.text.replace("✅", ""), 
                          reply_markup=call.message.reply_markup)

bot.polling()