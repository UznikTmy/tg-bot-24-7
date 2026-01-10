import telebot

bot = telebot.TeleBot("8287514660:AAGmIWrcoydKFDWl65tb_zRrkpsFKiMEFjw")

@bot.message_handler(func=lambda _: True)
def reply(message):
  bot.reply_to(message, "Hello! I'm alive 24/7.")

bot.

bot.polling(none_stop=True)
