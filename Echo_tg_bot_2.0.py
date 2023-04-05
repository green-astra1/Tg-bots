import telebot

#вставляем токен бота полученный из @BotFather
bot = telebot.TeleBot ("TOKEN")

#функция, обрабатывающая команду /start
@bot.message_handler (commands = ["start"])
def start_message (message):
    first_name = message.chat.first_name
    #бот отправляет (пользователю, "Привет, " его ник тг)
    bot.send_message (message.chat.id, f"Привет, {first_name}")

#отслеживаем текстовые сообщение
@bot.message_handler (content_types = ['text'])
def repeat_all_messages (message):
    #бот отправляет (пользователю, "Вы написали: " его же сообщение)
    bot.send_message (message.chat.id, "Вы написали: " + message.text)

#запускаем бота
bot.polling (none_stop = True)
