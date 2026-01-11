import telebot
from datetime import date

bot = telebot.TeleBot("8287514660:AAGmIWrcoydKFDWl65tb_zRrkpsFKiMEFjw")

@bot.message_handler(func=lambda _: True)
def reply(message):
  today = date.today()
  formatted_date = today.strftime("%Y-%m-%d")
  bot.reply_to(message, "Привет! Я доступен. Сейчас "+formatted_date)

bot.polling(none_stop=True)
