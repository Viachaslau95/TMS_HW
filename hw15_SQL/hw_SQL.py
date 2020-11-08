import sqlite3


class SQLliteCRUD:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = self.get_connection()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def creat_person(self, first_name, last_name):
        cursor = connection.cursor()
        INSERT_USER_DATA_QUERY = "INSERT INTO user(first_name, last_name) VALUES(?,?)"
        cursor.execute(INSERT_USER_DATA_QUERY, (first_name, last_name))
        connection.commit()


    def read(self):
        cursor = connection.cursor()
        cursor.execute("SELECT first_name, last_name FROM user")
        results = cursor.fetchall()
        print(results)


    def updete(self):
        pass

    def delete(self, id):
        delete = 'DELETE FROM user WHERE id='
        return delete

        pass


CREATE_TABLE_QUERY = """CREATE TABLE user (
                    id integer PRIMARY KEY AUTOINCREMENT,
                     first_name varchar,
                     last_name varchar
                     )
"""


if __name__ == '__main__':
    connection = sqlite3.connect('my.db')
    sql_lite_obj = SQLliteCRUD(db_name='my.db')
    sql_lite_obj.get_connection()
    sql_lite_obj.creat_person('K', 'B')
    sql_lite_obj.read()
    # sql_lite_obj.delete(1)

    cursor = connection.cursor()

    connection.commit()
    cursor.close()
    connection.close()
