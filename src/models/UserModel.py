from database.db import get_connection
from .entities.User import User
import math


class UserModel():

    @classmethod
    def get_users(self):
        try:
            connection = get_connection()
            users = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, apellido, edad FROM users ORDER BY id ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    user = User(row[0], row[1], row[2], row[3])
                    users.append(user.to_JSON())

            connection.close()
            return users
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, apellido, edad FROM users WHERE id = %s", (id,))
                row = cursor.fetchone()

                user = None
                if row != None:
                    user = User(row[0], row[1], row[2], row[3])
                    user = user.to_JSON()

            connection.close()
            return user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users (id, nombre, apellido, edad)
                                VALUES (%s, %s, %s, %s)""", (user.id, user.nombre, user.apellido, user.edad))
                affected_rows=cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", (user.id))
                affected_rows=cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE users SET nombre = %s, apellido = %s, edad = %s
                                WHERE id = %s""", (user.nombre, user.apellido, user.edad, user.id))
                affected_rows=cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def prom_users(self):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT AVG(edad) AS promedio FROM users")
                row = cursor.fetchone()
                p = row[0]
                promedio = round(p,1)

            connection.close()
            return promedio
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def status_users(self):
        try:
            connection = get_connection()
            nameSystem = "api-usuarios"
            version = "0.0.1"
            developer = "Alfredo"
            email = "Alfredoxd00@hotmail.com"
            status = [nameSystem, version, developer, email]

            connection.close()
            return status
        except Exception as ex:
            raise Exception(ex)
