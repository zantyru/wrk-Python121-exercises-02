from sqlalchemy import create_engine, MetaData
import dbtables


engine = create_engine("sqlite:///college.sqlite3", echo=True)
# meta = MetaData()
dbtables.meta.create_all(engine)

# Чтобы обмениваться даннными с таблицами
connection = engine.connect()

insert = dbtables.students.insert().values(
    name="John", lastname="First"
)
connection.execute(insert)

insert = dbtables.students.insert().values([
    {"name": "Marta", "lastname": "Goods"},
    {"name": "Николай", "lastname": "Петров"},
    {"name": "Василий", "lastname": "Тёркин"}
])
connection.execute(insert)

