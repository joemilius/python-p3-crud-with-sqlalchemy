#!/usr/bin/env python3

from datetime import datetime

from sqlalchemy import (create_engine, desc, func,
    CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,
    Index, Column, DateTime, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String(55))
    grade = Column(Integer())
    birthday = Column(DateTime())
    enrolled_date = Column(DateTime(), default=datetime.now())

    def __repr__(self):
        return f"Student {self.id}: " \
            + f"{self.name}, " \
            + f"Grade {self.grade}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    albert_einstein = Student(
        name = "Albert Einstein",
        email = "albert.einstein@zurich.edu",
        grade = 6,
        birthday = datetime(
            year = 1879,
            month = 3,
            day = 14
        ),
    )

    # session.add(albert_einstein)
    # session.commit()

    # print(f"New student ID is {albert_einstein.id}")
    alan_turing = Student(
        name="Alan Turing",
        email="alan.turing@sherborne.edu",
        grade=11,
        birthday=datetime(
            year=1912,
            month=6,
            day=23
        ),
    )

    session.bulk_save_objects([albert_einstein, alan_turing])
    session.commit()

    # print(f"New student ID is {albert_einstein.id}")
    # print(f"New student ID is {alan_turing.id}")

    ## . .all
    # students = session.query(Student).all()

    # print(students)
    
    ## . attribute query
    # names = session.query(Student.name).all()

    # print(names)

    ## . .order_by
    # students_by_name = session.query(
    #         Student.name).order_by(
    #         Student.name).all()

    # print(students_by_name)

    ## . desc()
    # students_by_grade_desc = session.query(
    #         Student.name, Student.grade).order_by(
    #         desc(Student.grade)).all()

    # print(students_by_grade_desc)

    ## . .limit
    # oldest_student = session.query(
    #         Student.name, Student.birthday).order_by(
    #         desc(Student.grade)).limit(1)

    # print(oldest_student)

    ## . .first
    # oldest_student = session.query(
    #         Student.name, Student.birthday).order_by(
    #         desc(Student.grade)).first()

    # print(oldest_student)


    ## . .func
    # student_count = session.query(func.count(Student.id)).first()

    # print(student_count)


    ##Filtering queries
    # query = session.query(Student).filter(Student.name.like('%Alan%'),
    #     Student.grade == 11)

    # for record in query:
    #     print(record.name)


    ##Updating Database Queries

    # for student in session.query(Student):
    #     student.grade += 1

    # session.commit()

    # print([(student.name,
    #     student.grade) for student in session.query(Student)])


    ## with .update
    # session.query(Student).update({
    #     Student.grade: Student.grade + 1
    # })

    # print([(
    #     student.name,
    #     student.grade
    # ) for student in session.query(Student)])


    ## Deleting queries
    # query = session.query(
    #     Student).filter(
    #         Student.name == "Albert Einstein")        

    # # retrieve first matching record as object
    # albert_einstein = query.first()

    # # delete record
    # session.delete(albert_einstein)
    # session.commit()

    # # try to retrieve deleted record
    # albert_einstein = query.first()

    # print(albert_einstein)

    ##Delete all records from query
    # query = session.query(
    #     Student).filter(
    #         Student.name == "Albert Einstein")

    # query.delete()

    # albert_einstein = query.first()

    # print(albert_einstein)