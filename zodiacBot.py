import telebot; bot = telebot.TeleBot('1184822377:AAFI7WcS2XEEj00lKOUXbC-tDHIuEY4Roz8')
from telebot import types

from zodiacSignInfo import allInfoSigns, dictToString
'''
@bot.message_handler(content_types=['start'])
def startMessage(message):
    bot.send_message(message.from_user.id, 'Напиши мне: Привет')
'''
@bot.message_handler(content_types=['text'])
def textButtons(message):
    if message.text.lower() == "Привет":
        bot.send_message(message.from_user.id, "Привет, я сейчас расскажу тебе про твой знак зодиака.")
        keyboard = types.InlineKeyboardMarkup()
        keyTwins = types.InlineKeyboardButton(text = 'Овен', callback_data = 'ram')
        keyboard.add(keyTwins)
        keyTaurus = types.InlineKeyboardButton(text = 'Телец', callback_data = 'bull')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Близнецы', callback_data = 'twins')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Рак', callback_data = 'crab')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Лев', callback_data = 'lion')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Дева', callback_data = 'maider')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Весы', callback_data = 'scales')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Скорпион', callback_data = 'scorpion')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Стрелец', callback_data = 'archer')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Козерог', callback_data = 'goat')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Водолей', callback_data = 'waterbearer')
        keyboard.add(keyTaurus)
        keyTaurus = types.InlineKeyboardButton(text = 'Рыбы', callback_data = 'fishes')
        keyboard.add(keyTaurus)
        bot.send_message(message.from_user.id, text = 'Выбери свой знак зодиака', reply_markup = keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Напиши мне: Привет')
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши: /help")

@bot.callback_query_handler(func=lambda call: True)
def eventButtons(call):
    if call.data == 'waterbearer':
        a = dictToString('Овен')
        bot.send_message(call.message.chat.id, a)
    if call.data == 'twins':
        b = dictToString('Близнецы')
        bot.send_message(call.message.chat.id, b)
    if call.data == 'taurus':
        t = dictToString('Телец')
        bot.send_message(call.message.chat.id, t)

bot.polling(none_stop=True, interval=0)
