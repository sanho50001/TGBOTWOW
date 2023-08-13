import telebot
import datetime
from game.settings.settingstelegram import CommandsTelegram

# Запуск бота по токену
bot = telebot.TeleBot('5824374073:AAEfAlM2tCZzknjkol1_NKyPnzfaMYI31BE')
print('Бот начал свою работу.')



# Отпределение команд бота
TGBOT = CommandsTelegram(bot)

# Хандлеры для вызова команд

# Хендлер для регистрации
@bot.message_handler(commands=["reg"])
def reg(message):
    bot.send_message(message.from_user.id, 'Начинаем процесс регистрации...')

# Хендлер старта
@bot.message_handler(commands=['start'])
def start(message):
    print(f'Чат ID: {message.chat.id} | {message.from_user.first_name} {message.from_user.last_name}: {message.text}')
    bot.send_message(message.from_user.id, 'Привет! Начнем?')

# хендлер принимающий любой вид текста которые не прошли проверку на команду
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    TGBOT.getTextMessages(message=message)

# Вечный пуллинг, чтобы бот принимал всегда сообщения
bot.polling(none_stop=True, interval=0)
print(f'Бот завершил работу в', datetime.datetime.now().strftime('Дата: %Y %m %d Время: %H:%M:%S'))




