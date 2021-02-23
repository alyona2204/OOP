class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def revie_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress and grade <= 10:
            if course in lector.grades_lector:
                lector.grades_lector[course] += [grade]
            else:
                lector.grades_lector[course] = [grade]
        else:
            print ('Ошибка')

    def get_ball(self, course):
        if course in self.courses_in_progress:
            for key, value in list(self.grades.items()):
                if key == course:
                    return value
        else:
            print('Ошибка')

    def average_rating(self, course):
        if course in self.courses_in_progress:
            x = sum(self.get_ball(course)) / len(self.get_ball(course))
            return f'Средний балл студента {self.name} {self.surname} за курс {course}: {x}'
        else:
            return f'Студент {self.name} {self.surname} не обучается по курсу {course}'

    def average(self):
        for key, value in list(self.grades.items()):
            x = sum(value) / len(value)
            return x

    def __lt__(self, other):
        if isinstance(other, Student):
            print('Сравнение студентов')
        return self.average() < other.average()

    def __str__(self):
        nl = '\n'
        return f'Имя: {self.name} {nl}Фамилия: {self.surname}{nl}' \
               f'Средняя оценка за домашние задания: {self.average()}{nl}' \
               f'Курсы в процессе изучения: {self.courses_in_progress}{nl}' \
               f'Завершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades_lector = {}

    def __str__(self):
        nl = '\n'
        return f'Имя: {self.name} {nl}Фамилия: {self.surname}{nl}' \
               f'Средняя оценка за лекции: {self.average_lector()}'

    def get_ball_lector(self, course):
        if course in self.courses_attached:
            for key, value in list(self.grades_lector.items()):
                if key == course:
                    return value
        else:
            print('Ошибка')

    def average_rating_lector(self, course):
        if course in self.courses_attached:
            x = sum(self.get_ball_lector(course)) / len(self.get_ball_lector(course))
            return f'Средний балл лектора {self.name} {self.surname} за курс {course}: {x}'
        else:
            return f'Лектор {self.name} {self.surname} не обучает курсу {course}'

    def average_lector(self):
        for key, value in list(self.grades_lector.items()):
            x = sum(value) / len(value)
            return x

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            print('Сравнение лекторов')
        return self.average_lector() < other.average_lector()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
    def revie_students (self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')



    def __str__(self):
        nl = '\n'
        return f'Имя: {self.name} {nl}Фамилия: {self.surname}'





student_1 = Student('Ruoy', 'Eman', 'gender')
student_2 = Student('Noi', 'Peters', 'gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses+= ['Введение в программирование']
student_2.finished_courses+= ['Введение в программирование']
student_2.courses_in_progress += ['Python']


reviewer_1 = Reviewer('Reviewer', 'toPython')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Reviewer', 'toGit')
reviewer_2.courses_attached += ['Git']

reviewer_1.revie_students(student_1, 'Python', 10)
reviewer_1.revie_students(student_1, 'Python', 9)
reviewer_1.revie_students(student_1, 'Python', 10)
reviewer_1.revie_students(student_1, 'Python', 10)

reviewer_2.revie_students(student_1, 'Git', 10)
reviewer_2.revie_students(student_1, 'Git', 9)
reviewer_2.revie_students(student_1, 'Git', 9)
reviewer_2.revie_students(student_1, 'Git', 9)

reviewer_1.revie_students(student_2, 'Python', 10)
reviewer_1.revie_students(student_2, 'Python', 9)
reviewer_1.revie_students(student_2, 'Python', 9)
reviewer_1.revie_students(student_2, 'Python', 10)

lector_1 = Lecturer('Lector', 'toPython')
lector_1.courses_attached += ['Python']
lector_2 = Lecturer('Lector', 'toGit')
lector_2.courses_attached += ['Git']


student_1.revie_lecturer(lector_1, 'Python', 9)
student_1.revie_lecturer(lector_1, 'Python', 10)
student_1.revie_lecturer(lector_1, 'Python', 9)
student_1.revie_lecturer(lector_1, 'Python', 10)

student_1.revie_lecturer(lector_2, 'Git', 10)
student_1.revie_lecturer(lector_2, 'Git', 10)
student_1.revie_lecturer(lector_2, 'Git', 10)
student_1.revie_lecturer(lector_2, 'Git', 10)


print(student_1)
print(student_2)
print(lector_1)
print(lector_2)
print(reviewer_1)
print(reviewer_2)
print(student_1.average_rating('Git'))
print(student_1.average_rating('Python'))
print(student_2.average_rating('Python'))
print(student_2.average_rating('Git'))

print(lector_2.average_rating_lector('Git'))
print(lector_1.average_rating_lector('Python'))
print(lector_2.average_rating_lector('Python'))
print(student_2<student_1)
print(lector_2<lector_1)
