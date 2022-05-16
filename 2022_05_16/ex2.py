from sqlalchemy import create_engine, MetaData
from sqlalchemy import and_
import dbtables


engine = create_engine("sqlite:///college.sqlite3", echo=True)

connection = engine.connect()

select = dbtables.students.select()
result = connection.execute(select)

print("Все записи таблицы students:")
for row in result:
    print(row)


select = dbtables.students.select().where(
    dbtables.students.c.name.like("%и%")
)
result = connection.execute(select)

print("Все студенты, имя которых содержит 'и':")
for row in result:
    print(row, type(row), f"Имя студента: {row.name}")


select = dbtables.students.select().where(
    and_(
        dbtables.students.c.lastname == 'Петров',
        dbtables.students.c.name.like("%и%")
    )
)
result = connection.execute(select)

print("Все студенты, имя которых содержит 'и', а фамилия 'Петров':")
for row in result:
    print(row)
