import os
import telebot
import openai

BOT_TOKEN = '5858548516:AAEkbS0LHi5Y7YmHpDBSo8RsnZwFyQZBej0'
OPENAI_API_KEY = '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'

bot = telebot.TeleBot(BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

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
def generate_reply(message):
    user_input = message.text

    # Use the ChatGPT API to generate a reply
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_input,
        max_tokens=4001,
        temperature=0,
        n=1,
        stop=None
    )

    if len(response.choices) > 0:
        reply = response.choices[0].text.strip()
        bot.reply_to(message, reply)

bot.infinity_polling()
