import telebot; bot = telebot.TeleBot('1184822377:AAFI7WcS2XEEj00lKOUXbC-tDHIuEY4Roz8')

from telebot import types


@bot.message_handler(content_types=['text'])
def sendText(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, я сейчас расскажу тебе про твой знак зодиака.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши ''/help'")


#zodiacSign = str(input("{blue}Введите свой знак зодиака: {endcolor}".format(blue="\033[96m", endcolor="\033[0m"))))

keyboard = types.InlineKeyboardMarkup()
keyTwins = types.InlineKeyboardButton(text = 'Близнецы ♊', callBack_data = 'zodiacSign')
keyboard.add(keyTwins)

keyboard = types.InlineKeyboardMarkup()
keyTaurus = types.InlineKeyboardButton(text = 'Телец ♉', callBack_data = 'zodiacSign')
keyboard.add(keyTaurus)

bot.send_message(message.from_user.id, text = 'Выбери свой знак зодиака', reply_murkup = keyboard)

bot.polling()
