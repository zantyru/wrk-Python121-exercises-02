import sqlite3
from pathlib import Path


WORK_DIR = Path(__file__).absolute().parent
DB_FILE_NAME = WORK_DIR / 'db.db'

# Подключение к БД
connection = sqlite3.connect(DB_FILE_NAME)
cursor = connection.cursor()

# Посылаем SQL-запрос
cursor.execute("""
CREATE TABLE IF NOT EXISTS Person (
    "person_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "first_name" TEXT(100),
    "last_name" TEXT(100),
    "birth_date" TEXT(10)
    );
""")

cursor.execute("""
INSERT OR REPLACE
    INTO Person(first_name, last_name, birth_date) VALUES
        ("Garry", "Hoodiny", "1945-02-02")
        , ("Om", "Redpocket", "1978-10-18")
        , ("Max", "Gorsky", "1989-11-06")
        , ("Emma", "Rwiststone", "1989-06-12");
""")

connection.commit()  # Подтвердить отсылку запросов в БД

# Можно передать данные из Python
people = [
    ("N1", "L1", "YYYY-XX-ZZ"),
    ("N2", "L2", "YYY9-X1-ZZ"),
    ("N1", "L3", "YYY9-XX-ZZ"),
    ("N4", "L2", "YYYY-1X-ZZ"),
    ("N4", "L6", "YYY9-XX-ZZ"),
    ("N6", "L9", "YYYY-X2-ZZ"),
    ("N7", '; DROP TABLE "Person";-- LTD', "YYYY-XX-ZZ"),
]
cursor.executemany(
    """
    INSERT OR REPLACE
        INTO Person(first_name, last_name, birth_date)
            VALUES(?, ?, ?); 
    """,
    people
)
connection.commit()

# Запросить данные из базы
cursor.execute("""SELECT * FROM Person""")
data = cursor.fetchall()
for row in data:
    print(row)
