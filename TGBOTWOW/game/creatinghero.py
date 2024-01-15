class CreatingHero:
    def __init__(self):
        self.bot = None
        self.settings = None
        self.hero = None
        self.types = None
        self.user = None
        self.database = None
        self.time = None
        self.startgame = None

    def set_bot(self, bot):
        self.bot = bot

    def set_settings(self, settings):
        self.settings = settings

    def set_hero(self, hero):
        self.hero = hero

    def set_types(self, types):
        self.types = types

    def set_user(self, user):
        self.user = user

    def set_database(self, database):
        self.database = database

    def set_time(self, time):
        self.time = time

    def set_startgame(self, startgame):
        self.startgame = startgame

    def step_one_creating_hero(self, message):
        """Этап создания персонажа. 1/2 этап."""
        # print(message)
        self.hero.hero.set_name_hero(message.text)  #Установка имени персонажа

        # вызов метода создания кнопки
        markup_inline = self.types.InlineKeyboardMarkup()

        # Кнопки инлайн(под сообщением выпадающие) классов
        markup_inline.add(
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_warrior(), callback_data='warrior'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_hunter(), callback_data='hunter'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_paladin(), callback_data='paladin'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_rogue(), callback_data='rogue'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_priest(), callback_data='priest'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_shaman(), callback_data='shaman'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_mage(), callback_data='mage'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_warlock(), callback_data='warlock'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_druid(), callback_data='druid'),
            self.types.InlineKeyboardButton(text=self.settings.text_on_class_death_knight(), callback_data='dk'),
        )
        # Отправка сообщения и кнопок инлайн
        messages = self.bot.send_message(self.user.get_id_account(),
                                    self.settings.text_menu_button_choice_class_hero(),
                                    reply_markup=markup_inline)
        self.settings.set_last_message_id(messages.message_id)
        # Функция необходимая для сообщений в чате (если пользователь захотел сам ввести)
        self.bot.register_next_step_handler(message, self.two_step_creating_hero)

    def two_step_creating_hero(self):
        """Второй этап создания персонажа. 2/2 этап."""
        messages = self.bot.send_message(self.user.get_id_account(),
                         self.settings.text_on_welcom_step_two_creating_hero())
        self.settings.set_last_message_id(messages.message_id)
        # создание героя в базе данных
        self.database.Create_Hero(
            name_hero=self.hero.hero.get_name_hero(),
            classes=self.hero.hero.get_classes_hero(),
            id_account=self.user.get_id_account()
        )
        self.time.sleep(1)
        self.startgame.welcom()

    #     bot.register_next_step_handler(message, self.three_step_creating_hero)
    # def three_step_creating_hero(self, message):
    #     bot.send_message(user.get_id_account(), settings.)


creating_hero = CreatingHero()