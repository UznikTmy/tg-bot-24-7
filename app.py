import telebot
import datetime
import schedule

bot = telebot.TeleBot("8287514660:AAGmIWrcoydKFDWl65tb_zRrkpsFKiMEFjw")

msg = "";

@bot.message_handler(func=lambda _: True)
def reply(message):
  msg = message;
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  bot.reply_to(message, "Привет! Я доступен. Сейчас "+date_time)

def job(message):
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  bot.reply_to(message, "Привет! Я работаю... ("+date_time+")")

# Schedule the job to run every 10 seconds
schedule.every(10).seconds.do(job, message=msg)

bot.polling(none_stop=True)
