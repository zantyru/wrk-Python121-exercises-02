import sqlite3
from pathlib import Path
import ex1_console


WORK_DIR = Path(__file__).absolute().parent
DB_FILE_NAME = WORK_DIR / 'db.db'


SQL_SCRIPT_CREATE_ALL = """
PRAGMA foreign_keys=on;
BEGIN TRANSACTION;
-- Создаём таблицы --
CREATE TABLE IF NOT EXISTS Author (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT(100) NOT NULL,
    last_name TEXT(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS Book (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title TEXT(200) NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY(author_id) REFERENCES Author(author_id)
        -- При удалении автора, удаляются все его книги (по цепочке)
        ON DELETE CASCADE
        -- При обновлении автора, обновляются все его упоминания
        ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS Publisher (
    publisher_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT(100)
);
CREATE TABLE IF NOT EXISTS BookPublisher (
    book_id INTEGER NOT NULL,
    publisher_id INTEGER NOT NULL,
    FOREIGN KEY(book_id) REFERENCES Book(book_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(publisher_id) REFERENCES Publisher(publisher_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE    
); 
-- Наполняем таблицы данными --
INSERT OR REPLACE
    INTO Author(author_id, first_name, last_name) VALUES
        (1, "Мрак", "Невт")
        , (2, "Сократ", "")
        , (3, "Волк", "Серый");
INSERT OR REPLACE
    INTO Book(book_id, title, author_id) VALUES
        (1, "Как ловит мух", 2);
COMMIT;
"""


with sqlite3.connect(DB_FILE_NAME) as connection:
    print("Создание и наполнение БД, если это необходимо...")
    connection.executescript(SQL_SCRIPT_CREATE_ALL)
    cursor = connection.cursor()
    ex1_console.start_menu(cursor)
