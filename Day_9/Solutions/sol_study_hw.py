"""
Задача №2: Система учета учебных курсов.

При необходимости можно добавить свои классы или функции для реализации.

Дан примерный список классов с атрибутами и методами.
Напишите реализацию учета учебных курсов.

Класс Person:
Атрибуты: name, surname age, birthday, sex, full_name

Класс Student(Person)
Атрибуты: background, experience, total_points, attendance_type('webinar', 'full-time')
Методы: make_practice, make_homework, do_final_test

Класс Teacher(Person)
Методы: create_task, check_task, create_final_test, check_final_test

Класс Course()
Атрибуты: course_name, amount_of_days, students, teacher, lessons, attendance_journal
Методы: add_student, add_teacher, check_all(all_homework + final_test), count_success, count_failure, responses

Класс Lesson()
Атрибуты: lesson_name, date, attendance_of_students

Класс Task()
Атрибуты: description, level('light', 'medium', 'hard') или points(количество баллов), type('practice', 'homework'), solution_as_link
"""
import random

NAMES = "Matvey", "Alexey", "Sasha", "Artem"
SURNAMES = "Maslov", "Ivanov", "Sidorov", "Petrov"
BACKGROUNDS = "Builder", "Programmer", "Office worker", "Sales manager"



class Task:
    def __init__(self, description: str, points: int, type):
        self.description = f"{random.randint(1,100)}+{random.randint(1,100)}"
        self.points = points
        if type not in ('practice', 'homework'):
            raise TypeError("Wrong type")
        self.type = type
        self.soulution = None
        self.student = None


class Person:
    def __init__(self):
        self.full_name = f"{random.choice(NAMES)} {random.choice(SURNAMES)}"
        self.age = random.randint(18, 40)
        self.birthday = f"{random.randint(1, 30)}-{random.randint(1, 12)}-{2022 - self.age}"
        self.sex = random.choice(("male", "female"))

    def __repr__(self):
        return f"name:{self.full_name}, Age:{self.age}, Birthday:{self.birthday}, Sex:{self.sex}"


class Student(Person):
    def __init__(self):
        super().__init__()
        self.background = random.choice(BACKGROUNDS)
        self.experience = "Drawing in Paint"
        self.total_points = 0
        self.attendance_type = random.choice(("webinar", "full-time"))

    def __repr__(self):
        return f"Student({super().__repr__()}, Background:{self.background}, Experience:{self.experience}, Total points:{self.total_points}, Attendance:{self.attendance_type})\n"

    def make_task(self, task: Task):
        task.soulution = random.randint(0, 1)
        task.student = self


class Teacher(Person):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f"Teacher {super().__repr__()}\n"

    @staticmethod
    def create_task(type):
        return Task("do smth", 10, type)

    @staticmethod
    def check_task(task: Task):
        if task.soulution:
            task.student.total_points += task.points
            print(f"{task.student.full_name} complete {task.description} and earn {task.points} points!")
            return True
        else:
            print(f"{task.student.full_name} fail {task.description}!")
            return False

    def create_test(self):
        return [self.create_task("practice") for _ in range(10)]


class Course:
    def __init__(self, course_name, amount_of_days):
        self.course_name = course_name
        self.count_success = 0
        self.count_fail = 0
        self.amount_of_days = amount_of_days
        self.students = []
        self.teacher = None
        self.lessons = []

    def add_lesson(self, name):
        self.lessons.append(Lesson(name,self.teacher, self.students))

    def __repr__(self):
        return f"Name:{self.course_name}, Marks stat:{self.show_marks_stat()}, Amount of days:{self.amount_of_days}\nTeacher:{self.teacher}Students:{''.join(f'{student}' for student in self.students)}\nLessons:{''.join(f'{lesson}' for lesson in self.lessons)}"

    def add_student(self):
        self.students.append(Student())

    def set_teacher(self):
        self.teacher = Teacher()

    def show_marks_stat(self):
        for lesson in self.lessons:
            self.count_fail += lesson.count_fail
            self.count_success += lesson.count_success
        return f"(Success tasks:{self.count_success}, Failed tasks:{self.count_fail})"


class Lesson:
    def __init__(self, name, teacher, students):
        self.lesson_name = name
        self.teacher = teacher
        self.count_success = 0
        self.count_fail = 0
        self.students = students
        self.date = f"{random.randint(1, 30)}-{random.randint(1, 12)}-{2022}"
        self.attendance_of_students = 0

    def __repr__(self):
        return f"Name:{self.lesson_name}, Date:{self.date}, Teacher:{self.teacher}Students:{''.join(f'{student}' for student in self.students)}\n"

    def test(self):
        print(f"{'='*20}{self.lesson_name} TEST{'='*20}\n")
        test = self.teacher.create_test()
        for student in self.students:
            for task in test:
                student.make_task(task)
                if self.teacher.check_task(task):
                    self.count_success += 1
                else:
                    self.count_fail += 1


course = Course("Math", 14)
course.set_teacher()
for i in range(5):
    course.add_student()
course.add_lesson("Lesson 1")
course.add_lesson("Lesson 2")
for lesson in course.lessons:
    lesson.test()
print(f"\n{course}")