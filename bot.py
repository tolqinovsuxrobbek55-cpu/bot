# Oddiy Telegram bot namunasi
import telebot

TOKEN = "8948036879:AAFSVUCtCv3L58z-JGPCkA8yxEup-5qGPks"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men botman.")

bot.polling()
