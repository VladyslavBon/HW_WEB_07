from sqlalchemy import func, desc, and_
from connect_db import session
from models import Group, Student, Teacher, Subject, Grade, TeacherSubject

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    print(session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all())
    
def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.
    print(session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all())

def select_3():
    # Знайти середній бал у групах з певного предмета.
    print(session.query(Group.group_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).filter(Grade.subject_id == 1).group_by(Group.group_name).order_by(desc('avg_grade')).all())

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    print(session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).order_by(desc('avg_grade')).all())

def select_5():
    # Знайти, які курси читає певний викладач.
    print(session.query(Teacher.fullname, Subject.subject_name)\
        .select_from(Subject).join(TeacherSubject).join(Teacher).filter(TeacherSubject.teacher_id == 1).all())

def select_6():
    # Знайти список студентів у певній групі.
    print(session.query(Student.fullname)\
        .select_from(Student).filter(Student.group_id == 1).all())

def select_7():
    # Знайти оцінки студентів в окремій групі з певного предмета.
    print(session.query(Student.fullname, Grade.grade)\
        .select_from(Grade).join(Student).filter(and_(Grade.subject_id == 1, Student.group_id == 1)).order_by(desc(Grade.grade)).all())

def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    print(session.query(Teacher.fullname, Subject.subject_name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Subject).join(TeacherSubject).join(Teacher).join(Grade).filter(TeacherSubject.teacher_id == 1)\
        .group_by(Teacher.id, Teacher.fullname, Subject.subject_name).order_by(desc('avg_grade')).all())

def select_9():
    # Знайти список курсів, які відвідує певний студент.
    print(session.query(Student.fullname, Subject.subject_name)\
        .select_from(Grade).join(Student).join(Subject).filter(Grade.student_id == 1).group_by(Student.id, Subject.id).all())

def select_10():
    # Список курсів, які певному студенту читає певний викладач.
    print(session.query(Subject.subject_name)\
        .select_from(Subject).join(TeacherSubject).join(Teacher).join(Grade).filter(and_(TeacherSubject.teacher_id == 1, Grade.student_id == 1))\
        .group_by(Teacher.id, Teacher.fullname, Subject.subject_name).all())
    
if __name__ == '__main__':
    select_10()