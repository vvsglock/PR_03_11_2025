import pandas as pd


class Student:
    def __init__(self, student_id, name, group):
        self.student_id = student_id
        self.name = name
        self.group = group
        self.exams = []

    def add_exam(self, exam):
        self.exams.append(exam)

    def get_info(self):
        return f"Студент: {self.name} (ID: {self.student_id}), Группа: {self.group.name}"


class Group:
    def __init__(self, group_id, name):
        self.group_id = group_id
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students_count(self):
        return len(self.students)

    def get_info(self):
        return f"Группа: {self.name} (ID: {self.group_id}), Студентов: {self.get_students_count()}"


class Teacher:
    def __init__(self, teacher_id, name, department):
        self.teacher_id = teacher_id
        self.name = name
        self.department = department
        self.disciplines = []

    def add_discipline(self, discipline):
        self.disciplines.append(discipline)

    def get_info(self):
        return f"Преподаватель: {self.name} (ID: {self.teacher_id}), Предмент: {self.department}"


class Discipline:
    def __init__(self, discipline_id, name, hours):
        self.discipline_id = discipline_id
        self.name = name
        self.hours = hours
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_info(self):
        return f"Дисциплина: {self.name} (ID: {self.discipline_id}), Часов: {self.hours}"


class Exam:
    def __init__(self, exam_id, discipline, teacher, group, date):
        self.exam_id = exam_id
        self.discipline = discipline
        self.teacher = teacher
        self.group = group
        self.date = date
        self.grades = {}

    def add_grade(self, student, grade):
        if student in self.group.students:
            self.grades[student] = grade
            student.add_exam(self)
        else:
            print(f"Ошибка: студент {student.name} не в группе {self.group.name}")

    def get_info(self):
        return f"Экзамен: {self.discipline.name} (ID: {self.exam_id})\n" \
               f"Группа: {self.group.name}, Преподаватель: {self.teacher.name}\n" \
               f"Дата: {self.date}"

    def get_avg_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)


group1 = Group(1, "403ИС-22")
group2 = Group(2, "407ИС-22")

student1 = Student(1, "Вартанян Вячеслав", group1)
student2 = Student(2, "Поляков Ярослав", group1)
student3 = Student(3, "Сидоров Владимир", group2)

group1.add_student(student1)
group1.add_student(student2)
group2.add_student(student3)

teacher1 = Teacher(1, "Николаев Николай", "Физкультура")
teacher2 = Teacher(2, "Букина Анастасия", "Литература")

discipline1 = Discipline(1, "Физкультура", 90)
discipline2 = Discipline(2, "Литература", 120)

discipline1.add_teacher(teacher1)
discipline2.add_teacher(teacher2)

teacher1.add_discipline(discipline1)
teacher2.add_discipline(discipline2)

exam1 = Exam(1, discipline1, teacher1, group1, "2025-01-20")
exam2 = Exam(2, discipline2, teacher2, group2, "2025-01-25")

exam1.add_grade(student1, 4)
exam1.add_grade(student2, 5)
exam2.add_grade(student3, 3)

all_exams = [exam1, exam2]

data = []
for exam in all_exams:
    data.append({
        'Дисциплина':exam.discipline.name,
        'Группа':exam.group.name,
        'Преподаватель':exam.teacher.name,
        'Дата':exam.date,
        'Средний балл':exam.get_avg_grade(),
        'Количество студентов':len(exam.group.students)
    })

df = pd.DataFrame(data)
df.to_excel('exam_report.xlsx', index=False)
