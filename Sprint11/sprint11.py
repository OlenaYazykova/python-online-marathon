import sqlite3
import os


class SQLite():
    def __init__(self, file):
        self.file=file

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.file)
            self.cursor = self.connection.cursor()
            print("Connected to SQLite")
            return self.cursor
        except sqlite3.Error as error:
            return f"Error establishing a database connection, {error}"

    def __exit__(self, type, value, traceback):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("The SQLite connection is closed")


def get_data(file):
    try:
        with SQLite(file) as cursor:
            cursor.execute("SELECT * FROM customers WHERE grade > 200 ORDER BY id")
            rows = cursor.fetchall()
            print(f"Total rows are:   {len(rows)}")
            print('Printing each row')
            for row in rows:
                print(f"Id:  {row[0]}")
                print(f"Name:  {row[1]}")
                print(f"City:  {row[2]}")
                print(f"Grade:  {row[3]}")
                print(f"Seller:  {row[4]}\n\n")
    except AttributeError:
        print(SQLite(file).__enter__())
    except sqlite3.Error as error:
        print(f"An error occurred accessing the database {file}, {error}")


file1=os.path.dirname(__file__) + "\\files\\q1.db"
get_data(file1)
