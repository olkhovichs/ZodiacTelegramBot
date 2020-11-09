import telebot; bot = telebot.TeleBot('1184822377:AAFI7WcS2XEEj00lKOUXbC-tDHIuEY4Roz8')
from telebot import types

from zodiacSignInfo import allInfoSigns, dictToString

@bot.message_handler(content_types=['text'])
def textButtons(message):
    if message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, я сейчас расскажу тебе про твой знак зодиака.")
        keyboard = types.InlineKeyboardMarkup()
        keyRam = types.InlineKeyboardButton(text = 'Овен', callback_data = 'ram')
        keyboard.add(keyRam)
        keyBull = types.InlineKeyboardButton(text = 'Телец', callback_data = 'bull')
        keyboard.add(keyBull)
        keyTwins = types.InlineKeyboardButton(text = 'Близнецы', callback_data = 'twins')
        keyboard.add(keyTwins)
        keyCrab = types.InlineKeyboardButton(text = 'Рак', callback_data = 'crab')
        keyboard.add(keyCrab)
        keyLion = types.InlineKeyboardButton(text = 'Лев', callback_data = 'lion')
        keyboard.add(keyLion)
        keyMaider = types.InlineKeyboardButton(text = 'Дева', callback_data = 'maider')
        keyboard.add(keyMaider)
        keyScales = types.InlineKeyboardButton(text = 'Весы', callback_data = 'scales')
        keyboard.add(keyScales)
        keyScorpion = types.InlineKeyboardButton(text = 'Скорпион', callback_data = 'scorpion')
        keyboard.add(keyScorpion)
        keyArcher = types.InlineKeyboardButton(text = 'Стрелец', callback_data = 'archer')
        keyboard.add(keyArcher)
        keyGoat = types.InlineKeyboardButton(text = 'Козерог', callback_data = 'goat')
        keyboard.add(keyGoat)
        keyWaterbearer = types.InlineKeyboardButton(text = 'Водолей', callback_data = 'waterbearer')
        keyboard.add(keyWaterbearer)
        keyFishes = types.InlineKeyboardButton(text = 'Рыбы', callback_data = 'fishes')
        keyboard.add(keyFishes)
        bot.send_message(message.from_user.id, text = 'Выбери свой знак зодиака', reply_markup = keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши: привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши: /help")

@bot.callback_query_handler(func=lambda call: True)
def eventButtons(call):
    if call.data == 'ram':
        bot.send_message(call.message.chat.id, dictToString('Овен'))
    if call.data == 'bull':
        bot.send_message(call.message.chat.id, dictToString('Телец'))
    if call.data == 'twins':
        bot.send_message(call.message.chat.id, dictToString('Близнецы'))
    if call.data == 'crab':
        bot.send_message(call.message.chat.id, dictToString('Рак'))
    if call.data == 'lion':
        bot.send_message(call.message.chat.id, dictToString('Лев'))
    if call.data == 'maider':
        bot.send_message(call.message.chat.id, dictToString('Дева'))
    if call.data == 'scales':
        bot.send_message(call.message.chat.id, dictToString('Весы'))
    if call.data == 'scorpion':
        bot.send_message(call.message.chat.id, dictToString('Скорпион'))
    if call.data == 'archer':
        bot.send_message(call.message.chat.id, dictToString('Стрелец'))
    if call.data == 'goat':
        bot.send_message(call.message.chat.id, dictToString('Козерог'))
    if call.data == 'waterbearer':
        bot.send_message(call.message.chat.id, dictToString('Водолей'))
    if call.data == 'fishes':
        bot.send_message(call.message.chat.id, dictToString('Рыбы'))
bot.polling(none_stop=True, interval=0)
