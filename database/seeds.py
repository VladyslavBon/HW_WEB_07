from datetime import datetime
from random import randint, choice

from faker import Faker

from connect_db import session
from models import Group, Student, Teacher, Subject, Grade, TeacherStudent, TeacherSubject


NUMBER_STUDENTS = 30
NUMBER_TEACHERS = 3
GROUPS = ['First group', 'Second_group', 'Third group']
SUBJECTS = ['Math', 'Physics', 'Ukrainian', 'English', 'Сhemistry']


def generate_groups(groups):
    for i in groups:
        group = Group(
            group_name=i
        )
        session.add(group)

    session.commit()


def generate_students(number_students):
    fake = Faker('uk_UA')
    groups = session.query(Group).all()

    for _ in range(number_students):
        group = choice(groups)
        student = Student(
            fullname=fake.name(),
            group_id=group.id
        )
        session.add(student)

    session.commit()


def generate_teachers(number_teachers):
    fake = Faker('uk_UA')

    for _ in range(number_teachers):
        teacher = Teacher(
            fullname=fake.name()
        )
        session.add(teacher)

    session.commit()


def generate_subjects(subjects):
    for i in subjects:
        subject = Subject(
            subject_name=i
        )
        session.add(subject)

    session.commit()


def generate_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for month in range(1, 12 + 1):
        grade_date = datetime(2022, month, randint(20, 25)).date()
        for student in students:
            subject = choice(subjects)
            grade = Grade(
                student_id=student.id,
                subject_id=subject.id,
                grade=randint(1, 100),
                date_of=grade_date
            )
            session.add(grade)

    session.commit()


def create_rel():
    students = session.query(Student).all()
    teachers = session.query(Teacher).all()
    subjects = session.query(Subject).all()
    
    for student in students:
        teacher = choice(teachers)
        rel = TeacherStudent(teacher_id=teacher.id, student_id=student.id)
        session.add(rel)

    for subject in subjects:
        teacher = choice(teachers)
        rel = TeacherSubject(teacher_id=teacher.id, subject_id=subject.id)
        session.add(rel)

    session.commit()


if __name__ == '__main__':
    generate_groups(GROUPS)
    generate_students(NUMBER_STUDENTS)
    generate_teachers(NUMBER_TEACHERS)
    generate_subjects(SUBJECTS)
    create_rel()
    generate_grades()