

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! To get the weather for a city, use the command /weather city_name.")

@bot.message_handler(commands=['weather'])
def send_weather(message):
    global city
    city = message.text.split(' ', 1)[1]
    chat_id = message.chat.id
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=<api_key>'
    try:
        response = requests.get(url).json()
        temp = response['main']['temp']
        description = response['weather'][0]['description']
        weather_message = f'The temperature in {city} is {temp}°C with {description}'
        bot.send_message(chat_id, weather_message)
    except:
        error_message = "Sorry, I couldn't retrieve the weather data for that city. Please try again."
        bot.send_message(chat_id, error_message)

bot.polling()
