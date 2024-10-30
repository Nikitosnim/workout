import telebot

token="7102444695:AAFOT1y5AoBbLTVFWBnefPc1vfRvB3sxPPs"

bot = telebot.TeleBot(token)

@bot.message_handler(content_tyeps=["text"])
def ech(message):
      bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
