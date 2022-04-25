def print_authors(cursor):
    cursor.execute("""
        SELECT author_id, first_name, last_name
        FROM Author;
    """)
    data = cursor.fetchall()
    print("Author")
    for author_id, first_name, last_name in data:
        print(author_id, first_name, last_name)


def print_books(cursor):
    cursor.execute("""
            SELECT book_id, title, author_id
            FROM Book;
        """)
    data = cursor.fetchall()
    print("Book")
    for book_id, title, author_id in data:
        print(book_id, title, author_id)


def add_author(cursor, first_name, last_name):
    sql = """
    INSERT
        INTO Author(first_name, last_name)
            VALUES (?, ?); 
    """
    cursor.execute(sql, (first_name, last_name))
    cursor.connection.commit()


def add_book(cursor, title, author_id):
    sql = """
    INSERT
        INTO Book(title, author_id)
            VALUES (?, ?); 
    """
    cursor.execute(sql, (title, author_id))
    cursor.connection.commit()


def get_number(prompt, number_type, default=None):
    while True:
        try:
            n = number_type(input(str(prompt)))
            break
        except (ValueError, TypeError) as _:
            print(f"Введено не число. Ожидается тип {number_type}.")
            if default is not None:
                n = default
                print(f"Использовано значение по умолчанию: {n}")
                break
            else:
                print("Повторите ввод.")
    return n


def start_menu_add_book(cursor):
    print("Добавление книги")
    title = input("Вв название книги: ")
    author_id = get_number("Вв ID автора: ", int)
    print("\n\n")
    add_book(cursor, title, author_id)


def start_menu(cursor):
    while True:
        print("0 - выход")
        print("1 - показать авторов")
        print("2 - показать книги")
        print("3 - добавить автора")
        print("4 - добавить книгу")
        n = get_number(">>> ", int)
        print("\n\n")

        if n == 0:
            break
        elif n == 1:
            print_authors(cursor)
            print("\n\n")
        elif n == 2:
            print_books(cursor)
            print("\n\n")
        elif n == 3:
            pass
        elif n == 4:
            start_menu_add_book(cursor)
