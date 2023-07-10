import os
import telebot

BOT_TOKEN = '5858548516:AAE9S7mGEeS8hC1MtV3HTkFQfAZZ8oXD4Bk'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello', 'hi', 'hola', 'tanya'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
    response = "I'm a bot that can perform various tasks. Here are some available commands:\n"
    response += "/start, /hello, /hi, /hola, /tanya - Greet the bot\n"
    response += "/help - Get information about available commands\n"
    response += "/info - Get information about the bot\n"
    response += "/weather <city> - Get the current weather of a city\n"
    response += "/news - Get the latest news\n"
    bot.reply_to(message, response)

@bot.message_handler(commands=['info'])
def send_info(message):
    response = "I'm a Telegram bot created using Telebot library.\n"
    response += "I can perform various tasks based on the commands you send.\n"
    response += "Feel free to explore the available commands.\n"
    bot.reply_to(message, response)

@bot.message_handler(commands=['weather'])
def get_weather(message):
    # Extract the city from the command
    command_parts = message.text.split()
    if len(command_parts) < 2:
        bot.reply_to(message, "Please provide a city name.")
        return

    city = command_parts[1]

    # Retrieve weather information using an external weather API
    # Replace this code with your weather API integration
    weather_info = f"The current weather in {city} is sunny."
    bot.reply_to(message, weather_info)

@bot.message_handler(commands=['news'])
def get_news(message):
    # Retrieve the latest news using an external news API
    # Replace this code with your news API integration
    news_info = "Here are the latest news headlines:\n"
    news_info += "- News headline 1\n"
    news_info += "- News headline 2\n"
    news_info += "- News headline 3\n"
    bot.reply_to(message, news_info)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
