import sqlite3

def set_user(user):
    try:
        sqlite_connection = sqlite3.connect('DataBase.db')
        sqlite_create_table_query = 'INSERT INTO OPROS VALUES ({}, "{}", date("now"), "{}")'.format(count_users(), user['id'],  user['choise'])
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

def get_users():
    try:
        sqlite_connection = sqlite3.connect('DataBase.db')
        sqlite_create_table_query = '''SELECT * FROM OPROS'''

        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        record = cursor.fetchall()
        print(record)

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    return record

def count_users():
    try:
        sqlite_connection = sqlite3.connect('DataBase.db')
        sqlite_create_table_query = '''SELECT ID FROM OPROS'''
        cursor = sqlite_connection.cursor()
        cursor.execute(sqlite_create_table_query)
        record = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
        
    finally:
        if (sqlite_connection):
            sqlite_connection.close()

    return len(record)