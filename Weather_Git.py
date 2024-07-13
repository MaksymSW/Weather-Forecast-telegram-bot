import telebot
import requests

TELEGRAM_TOKEN = 'Your bot token'


bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Write /weather <City> to know the weather.")


def get_weather(city):
    url = f'http://wttr.in/{city}?format=3&lang=en'
    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip()
    else:
        return "The City not found. Try again, please."
    
@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        city = message.text.split()[1]
        weather_info = get_weather(city)
        bot.reply_to(message, weather_info)
    except:
        bot.reply_to(message, "Enter a City, please") 

bot.polling()