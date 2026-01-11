import telebot
import datetime
import threading

bot = telebot.TeleBot("8287514660:AAGmIWrcoydKFDWl65tb_zRrkpsFKiMEFjw")

@bot.message_handler(func=lambda _: True)
def reply(message):
  now = datetime.datetime.now()
  date_time = now.strftime("%Y-%m-%d %H:%M:%S")
  bot.reply_to(message, "Привет! Я доступен. Сейчас "+date_time)

def delayed():
  th_name = threading.current_thread().name
  print(f'Th:{th_name} Worker запущен')
  bot.reply_to(message, "Привет! Я доступен by timer. ")

# Создание и запуск потоков таймеров
t1 = threading.Timer(1, delayed)
t1.start()
# t1.cancel()

bot.polling(none_stop=True)
