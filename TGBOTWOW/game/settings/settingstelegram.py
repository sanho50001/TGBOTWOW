from telebot import types


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
