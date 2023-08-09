import telebot
import datetime
from telebot import types

# Запуск бота по токену
bot = telebot.TeleBot('6442732736:AAEgEv-hxyaRxeHkDvMH4Ef_tj7ZC02WqTg')
print('Бот начал свою работу.')

# Класс команд телеграмма.
class CommandsTelegram:

    def __init__(self, bot):
        self.bot = bot

    def Help(self, message):
        # вызов метода создания кнопки
        markup_reply = types.ReplyKeyboardMarkup()
        markup_inline = types.InlineKeyboardMarkup()

        # кнопки
        reg_button = types.KeyboardButton('/reg')

        # создание кнопки и добавление туда кнопок.
        markup_reply.add(reg_button)
        markup_inline.add(
            types.InlineKeyboardButton(text='register', callback_data='register')
        )

        if message.text == "text":
            self.bot.send_message(message.from_user.id, 'text')
        elif message.text == "/help":
            self.bot.send_message(message.from_user.id, "Команды", reply_markup=markup_reply)
        else:
            self.bot.send_message(message.from_user.id, 'Извините, я вас не совсем понимаю.')

    # Обработчик сообщений. Срабатывает когда сообщение не прошло проверку на команду
    def getTextMessages(self, message):
        self.Help(message=message)

    def reg(self, message):
        pass


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




