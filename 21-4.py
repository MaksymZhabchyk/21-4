import telebot
API_TOKEN = '7805788253:AAHxuPqzdAldrUkExevo4neG0t5ZXkvg-1w'
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Це бот!")
@bot.message_handler(func=lambda _: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
