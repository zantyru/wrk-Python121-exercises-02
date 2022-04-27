import sqlite3
from pathlib import Path


WORK_DIR = Path(__file__).absolute().parent
DB_FILE_NAME = WORK_DIR / 'db.db'


SQL_SCRIPT_CREATE_ALL = """
PRAGMA foreign_keys=on;
BEGIN TRANSACTION;
-- Создаём таблицы --
CREATE TABLE IF NOT EXISTS Player (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT(100) NOT NULL,
    last_name TEXT(100) NOT NULL,
    nick_name TEXT(100) NOT NULL
);
CREATE TABLE IF NOT EXISTS Score (
    player_id INTEGER NOT NULL,
    points INTEGER NOT NULL,
    FOREIGN KEY(player_id) REFERENCES Player(player_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
-- Наполняем таблицы данными --
INSERT OR REPLACE
    INTO Player(player_id, first_name, last_name, nick_name) VALUES
        (1, "Мрак", "Невт", "BoatMaster")
        , (2, "Сократ", "@Rose@")
        , (3, "Волк", "Серый", "PawPaw");
INSERT OR REPLACE
    INTO Score(player_id, points) VALUES
        (1, 345)
        , (3, 1200);
COMMIT;
"""


with sqlite3.connect(DB_FILE_NAME) as connection:
    print("Создание и наполнение БД, если это необходимо...")
    connection.executescript(SQL_SCRIPT_CREATE_ALL)
    cursor = connection.cursor()

