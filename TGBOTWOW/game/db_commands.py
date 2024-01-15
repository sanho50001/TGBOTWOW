import mysql.connector
from mysql.connector import connect, Error
from dotenv import load_dotenv
import os

load_dotenv()
# with connect(
#         host="localhost",
#         user=os.getenv('db_user'),
#         password=os.getenv('db_password'),
# ) as connection:
#     print(connection)

config = {
    'user': os.getenv('db_user'),
    'password': os.getenv('db_password'),
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'tgwowgamedb',
    'raise_on_warnings': True,
}

con = mysql.connector.connect(**config)


class Settings_on_db:
    def __init__(self):
        self.settings = None

    def set_settings(self, settings):
        self.settings = settings

class DataBase:
    """Класс Базы Данных"""

    # def __init__(self):
    # Добавление юзера в базу данных для дальнейшей работы.
    def Create_User(self, id_account):
        """Добавление юзера в базу данных для дальнейшей работы"""
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT id_account FROM user_account WHERE id_account = {id_account}""")

            # Условие если в БД не нашлась запись, то создается.
            if cursor.fetchone() is None:
                cursor.execute(f"""INSERT INTO user_account SET id_account={id_account}""")
                con.commit()

    def get_id(self, id_account):
        """Получение id пользователя в таблице"""
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT id FROM user_account WHERE id_account={id_account}""")
            user_id = cursor.fetchone()
            value = user_id[0]
            return value

    # Создание героя
    def Create_Hero(self, name_hero, classes, id_account, lvl=1):
        """Создание героя"""
        with con.cursor() as cursor:
            user_id = self.get_id(id_account)
            try:
                cursor.execute(
                    "INSERT INTO user_classes (id, name_hero, class, id_account, lvl) VALUES (%s, %s, %s, %s, %s)",
                    (user_id, name_hero, classes, id_account, lvl))
            except Error as e:
                print(f"Ошибка: {e}")
            con.commit()

    def get_hero(self, name_hero):
        """Получение героя"""
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT name_hero, class,
             id_account, lvl FROM user_classes WHERE name_hero = '{name_hero}'""")
            result = cursor.fetchall()

            heroes = {}

            for row in result:
                heroes = {
                    'name hero': row[0],
                    'class': row[1],
                    'id account': row[2],
                    'lvl': row[3]
                }

            return heroes

    def get_hero_list(self):
        with con.cursor() as cursor:
            cursor.execute(f'SELECT name_hero, class, lvl FROM user_classes')
            result = cursor.fetchall()
            cursor.close()

            sorted_dict = {}
            for enum_row, row in enumerate(result):
                sorted_dict[enum_row] = {
                    settings_on_db.settings.text_on_db_name_hero(): 'None' if row[0] == '' else row[0],
                    settings_on_db.settings.text_on_db_classes_hero(): row[1],
                    settings_on_db.settings.text_on_db_lvl_hero():
                        str(row[2]) + ' ' + settings_on_db.settings.text_on_db_lvl_hero()}

            return (return_dict for return_dict in sorted_dict.items())

    def set_hero(self, number):
        with con.cursor() as cursor:
            cursor.execute(f'SELECT name_hero, class, lvl FROM user_classes')
            result = cursor.fetchall()
            cursor.close()

    def Zone(self, coording_x, coording_y):
        with con.cursor() as cursor:
            print('x=', coording_x, ' y=', coording_y)
            print('Zone', type(coording_y))
            t = cursor.execute(f"""SELECT NameLocation, NameZone FROM zone WHERE coord_x = {float(coording_x)} and coord_y = {float(coording_y)}""")
            print(t)
            result = cursor.fetchall()
            # Условие если в БД не нашлась запись, то создается.
            if result is None:
                return None
            else:
                return result
    def Spot(self):
        pass

    def SpotNPC(self):
        pass

    def NPC(self):
        pass





# Инициализация Базы Данных
database = DataBase()
settings_on_db = Settings_on_db()
