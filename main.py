import telebot; bot = telebot.TeleBot('TOKEN')
from telebot import types

from zodiacSignsInfo import info_sign as sign
from zodiacSignsInfo import dict_to_string as ds

@bot.message_handler(content_types=['text'])
def text_buttons(message):
    if message.text.lower() == "Привет":
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
def event_buttons(call):
    if call.data == 'ram':
        bot.send_message(call.message.chat.id, ds('Овен'))
    if call.data == 'bull':
        bot.send_message(call.message.chat.id, ds('Телец'))
    if call.data == 'twins':
        bot.send_message(call.message.chat.id, ds('Близнецы'))
    if call.data == 'crab':
        bot.send_message(call.message.chat.id, ds('Рак'))
    if call.data == 'lion':
        bot.send_message(call.message.chat.id, ds('Лев'))
    if call.data == 'maider':
        bot.send_message(call.message.chat.id, ds('Дева'))
    if call.data == 'scales':
        bot.send_message(call.message.chat.id, ds('Весы'))
    if call.data == 'scorpion':
        bot.send_message(call.message.chat.id, ds('Скорпион'))
    if call.data == 'archer':
        bot.send_message(call.message.chat.id, ds('Стрелец'))
    if call.data == 'goat':
        bot.send_message(call.message.chat.id, ds('Козерог'))
    if call.data == 'waterbearer':
        bot.send_message(call.message.chat.id, ds('Водолей'))
    if call.data == 'fishes':
        bot.send_message(call.message.chat.id, ds('Рыбы'))
bot.polling(none_stop=True, interval=0)
