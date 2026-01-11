import telebot
import datetime

bot = telebot.TeleBot("8287514660:AAGmIWrcoydKFDWl65tb_zRrkpsFKiMEFjw")

@bot.message_handler(func=lambda _: True)
def reply(message):
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  bot.reply_to(message, "Привет! Я доступен. Сейчас "+date_time)

bot.polling(none_stop=True)
