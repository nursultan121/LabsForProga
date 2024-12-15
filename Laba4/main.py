import telebot
import requests
from tokenfile import TOKEN

APIusd = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VSJtGQfmp2yix6zqBsTCLa9Mrof040LKpJDsTEN8'
APIrub = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VSJtGQfmp2yix6zqBsTCLa9Mrof040LKpJDsTEN8&currencies=EUR%2CUSD%2CRUB&base_currency=RUB'
APIeur = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VSJtGQfmp2yix6zqBsTCLa9Mrof040LKpJDsTEN8&currencies=EUR%2CUSD%2CRUB&base_currency=EUR'
dollar = requests.get(APIusd)
ruble = requests.get(APIrub)
euro = requests.get(APIeur)

currdollar = dollar.json()
currruble = ruble.json()
curreuro = euro.json()

bot = telebot.TeleBot(TOKEN)

user_states = {}
user_states2 = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Всем дарова! Это бот для\
 конвертации валют!!!\n\
Выберите валюту (usd, rub, eur):")
    
@bot.message_handler(func = lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text.upper()
    if chat_id not in user_states:
        user_states[chat_id] = {'currency': None}
        user_states2[chat_id] = {'currency': None}

    user_state = user_states[chat_id]
    user_state2 = user_states2[chat_id]
    

    if (user_state['currency'] in ['USD', 'RUB', 'EUR']) and\
    (user_state2['currency'] in ['USD', 'RUB', 'EUR']) and\
    text.isdigit():
        number = float(text)
        if user_state['currency'] == 'USD':
            for key, value in currdollar.items():
                for key, valuev in value.items():
                    if key == user_state2['currency']:
                        result = number * valuev
                        bot.reply_to(message, f"Результат: {float('{:.3f}'.format(result))}")
                        user_states[chat_id] = {'currency': None}
                        user_states2[chat_id] = {'currency': None}
                    
        if user_state['currency'] == 'RUB':
            for key, value in currruble.items():
                for key, valuev in value.items():
                    if key == user_state2['currency']:
                        result = number * valuev
                        bot.reply_to(message, f"Результат: {float('{:.3f}'.format(result))}")
                        user_states[chat_id] = {'currency': None}
                        user_states2[chat_id] = {'currency': None}

        if user_state['currency'] == 'EUR':
            for key, value in curreuro.items():
                for key, valuev in value.items():
                    if key == user_state2['currency']:
                        result = number * valuev
                        bot.reply_to(message, f"Результат: {float('{:.3f}'.format(result))}")
                        user_states[chat_id] = {'currency': None}
                        user_states2[chat_id] = {'currency': None}

    if user_state2['currency'] is None and not (user_state['currency'] is None):
        if text in ['USD', 'RUB', 'EUR']:
            user_state2['currency'] = text
            bot.reply_to(message, f"Вы выбрали {text.upper()}. Теперь введите число.")
        else:
            bot.reply_to(message, "Неправильно. Попробуй ещё раз.")

    if user_state['currency'] is None:
        if text in ['USD', 'RUB', 'EUR']:
            user_state['currency'] = text
            bot.reply_to(message, f"Вы выбрали {text.upper()}. Теперь введите следующую валюту.")
        else:
            bot.reply_to(message, "Неправильно. Попробуй ещё раз.")


bot.infinity_polling()
