import telebot

bot = telebot.TeleBot(7986165513:AAEyv-BitpL9YeDWzLZsoXsb_9s8PGUXbMQ)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Йо, я живий 🔥 Напиши назву треку і я знайду музику 🎧")

@bot.message_handler(func=lambda m: True)
def send_music(message):
    bot.send_message(message.chat.id, f"Ти написав: {message.text}\n(тут скоро буде музика)")

bot.polling()
