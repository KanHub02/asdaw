import telebot
bot = telebot.TeleBot('5141874602:AAGto-MRzsi_os1RTRUkEfMGTJ9oHXN9xpU')
@bot.message.handler(commands = [start])
def start(m, res = False):
    bot.send_message(m.chat.id, ('Привет, я здесь!'))
@bor.message.handler(commands = [text])
def handle_text(message):
    bot.send_message (message.chat.id, ('Вы написали:'))
bot.polling(none_stop=True, interval=0)