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