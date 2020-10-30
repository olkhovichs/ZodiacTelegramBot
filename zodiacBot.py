import telebot; bot = telebot.TeleBot('1184822377:AAFI7WcS2XEEj00lKOUXbC-tDHIuEY4Roz8')
from telebot import types
@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, я сейчас расскажу тебе про твой знак зодиака.")
        keyboard = types.InlineKeyboardMarkup()
        keyTwins = types.InlineKeyboardButton(text = 'Близнецы ♊', callback_data = 'twins')
        keyboard.add(keyTwins)
        keyTaurus = types.InlineKeyboardButton(text = 'Телец ♉', callback_data = 'taurus')
        keyboard.add(keyTaurus)
        bot.send_message(message.from_user.id, text = 'Выбери свой знак зодиака', reply_markup = keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши: привет с маленькой буквы еленочка")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши: /help")
@bot.callback_query_handler(func=lambda call: True)
def keybordsEvent(call):
    if call.data == 'twins':
        b = "Близнецы"
        bot.send_message(call.message.chat.id, b)
    if call.data == 'taurus':
        t = "Телец"
        bot.send_message(call.message.chat.id, t)
bot.polling(none_stop=True, interval=0)
