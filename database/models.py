from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Mapped

Base = declarative_base()


class Person():
    fullname = Column(String(250), nullable=False)

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(250), nullable=False)

class Student(Base, Person):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    group_id = Column('group_id', Integer, ForeignKey('groups.id', ondelete='CASCADE'))
    group = relationship(Group, backref='students')

class Teacher(Base, Person):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    students = relationship(Student, backref='teachers', secondary='teachers_to_students')

class TeacherStudent(Base):
    __tablename__ = 'teachers_to_students'
    id = Column(Integer, primary_key=True)
    teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    student_id = Column('student_id', Integer, ForeignKey('students.id', ondelete='CASCADE'))

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(250), nullable=False)
    teachers = relationship(Teacher, backref='subjects', secondary='teachers_to_subjects')

class TeacherSubject(Base):
    __tablename__ = 'teachers_to_subjects'
    id = Column(Integer, primary_key=True)
    teacher_id = Column('teacher_id', Integer, ForeignKey('teachers.id', ondelete='CASCADE'))
    subject_id = Column('subject_id', Integer, ForeignKey('subjects.id', ondelete='CASCADE'))

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Student, backref='grades')
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship(Subject, backref='grades')
    grade = Column(Integer, nullable=False)
    date_of = Column(DateTime, nullable=False)