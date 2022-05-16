from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey, UniqueConstraint


meta = MetaData()

students = Table(
    "students", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("lastname", String)
)

class_rooms = Table(
    'class_rooms', meta,
    Column('id', Integer, primary_key=True),
    Column('number', String),
    Column('capacity', Integer)
)

subjects = Table(
    'subjects', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

students_subjects = Table(
    'students_subjects', meta,
    Column('student_id', Integer, ForeignKey('students.id', onupdate="CASCADE", ondelete="CASCADE")),
    Column('subject_id', Integer, ForeignKey('subjects.id', onupdate="CASCADE", ondelete="CASCADE")),
    UniqueConstraint('student_id', 'subject_id')
)
