import telebot

token="8621176392:AAGlZgsmJvrfEoIqDw3o8zz7G5VH4XW_Lig"
bot=telebot.TeleBot(token)
@bit.message_hendler(content_type=['text'])
def start(message):
    bot.send_message(message.chat.id, message.text)
bot.infinity_polling()
