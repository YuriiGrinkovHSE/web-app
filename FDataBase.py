import math
import sqlite3
import time

class FDataBase:
    def __init__(self, db):
        self.__db__ = db
        self.__cur = db.cursor()

    def getFeedback(self, name, surname, feedback):
        try:
            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO usrs VALUES(NULL, ?, ?, ?, ?)", (name, surname, feedback, tm))
            self.__db__.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления отзыва в Базу Данных " + str(e))
            return False
        return True


