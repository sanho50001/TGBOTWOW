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


class DataBase:
    """Класс Базы Данных"""

    # def __init__(self):
    # Добавление юзера в базу данных для дальнейшей работы.
    def Create_User(self, id_account):
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT id_account FROM user_account WHERE id_account = {id_account}""")

            # Условие если в БД не нашлась запись, то создается.
            if cursor.fetchone() is None:
                cursor.execute(f"""INSERT INTO user_account SET id_account={id_account}""")
                con.commit()

    # Создание героя
    def Create_Hero(self, name_hero, classes):
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT name_hero FROM user_classes WHERE name_hero = {name_hero}""")

            # Условие если в БД не нашлась запись, то создается.
            if cursor.fetchone() is None:
                cursor.execute(f"""INSERT INTO user_classes SET name_hero={name_hero}, class={classes}""")
                con.commit()

    def Get_Hero(self, name_hero):
        hero = {}
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT name_hero FROM user_classes WHERE name_hero = {name_hero}""")
            return cursor.fetchall()

    def Hero(self):
        with con.cursor() as cursor:
            cursor.execute(f'SELECT * FROM zone')
            result = cursor.fetchall()
            for row in result:
                print(row)
            cursor.close()
        pass

    def Zone(self, coording_x, coording_y):
        with con.cursor() as cursor:
            cursor.execute(f"""SELECT coord_x and coord_y FROM zone WHERE coord_x = {coording_x} and coord_y = {coording_y}""")

            # Условие если в БД не нашлась запись, то создается.
            if cursor.fetchone() is None:
                return None
    def Spot(self):
        pass

    def SpotNPC(self):
        pass

    def NPC(self):
        pass

    pass


# Инициализация Базы Данных
database = DataBase()
