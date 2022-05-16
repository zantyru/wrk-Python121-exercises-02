from sqlalchemy import create_engine, select
from sqlalchemy import and_, or_
import dbtables


engine = create_engine("sqlite:///college.sqlite3", echo=True)
dbtables.meta.create_all(engine)

connection = engine.connect()

# Без join. Простая выборка из нескольких таблиц
query = select(
    [dbtables.students, dbtables.students_subjects]
).where(
    dbtables.students.c.id == dbtables.students_subjects.c.student_id
)
result = connection.execute(query)

rows = result.fetchall()
for row in rows:
    print(row.id, row.name, row.lastname, row.subject_id)

print("----------------")

# Join
join_query = dbtables.students.join(
    dbtables.students_subjects,
    dbtables.students.c.id == dbtables.students_subjects.c.student_id
).join(
    dbtables.subjects,
    dbtables.students_subjects.c.subject_id == dbtables.subjects.c.id
)

query = select(
    [
        dbtables.students.c.name,
        dbtables.students.c.lastname,
        dbtables.subjects.c.name
    ]
).select_from(join_query)

result = connection.execute(query)
for row in result:
    print(row)
