class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.enrolled_courses = []
        self.quiz_marks = {}

    def enroll_course(self, course):
        self.enrolled_courses.append(course)

    def unenroll_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)

    def set_quiz_marks(self, quiz, marks):
        self.quiz_marks[quiz.name] = marks

    def __str__(self):
        enrolled_courses_str = ', '.join(course.title for course in self.enrolled_courses)
        quiz_marks_str = ', '.join(f"{quiz}: {marks}" for quiz, marks in self.quiz_marks.items())
        return f"User: {self.username}, Enrolled Courses: {enrolled_courses_str}, Quiz Marks: {quiz_marks_str}"


class Quiz:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Quiz: {self.name}"


class Course:
    def __init__(self, title, description, professor):
        self.title = title
        self.description = description
        self.objectives = []
        self.professor = professor
        self.students = []
        self.assignments = []
        self.quizzes = []

    def add_objective(self, objective):
        self.objectives.append(objective)

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)

    def grade_quiz(self, student, quiz, marks):
        if quiz in self.quizzes:
            student.set_quiz_marks(quiz, marks)
        else:
            print("Quiz not found.")

    def __str__(self):
        assignments_str = ', '.join(assignment.name for assignment in self.assignments)
        quizzes_str = ', '.join(quiz.name for quiz in self.quizzes)
        return f"Course: {self.title}, Professor: {self.professor}, Assignments: {assignments_str}, Quizzes: {quizzes_str}"


class GradingSystem:
    def __init__(self):
        self.assignments = []

    def create_assignment(self, assignment_name):
        assignment = Assignment(assignment_name)
        self.assignments.append(assignment)
        return assignment

    def grade_assignment(self, student, assignment, grade):
        if assignment in self.assignments:
            student.set_grade(assignment, grade)
        else:
            print("Assignment not found.")

    def __str__(self):
        return f"Grading System with Assignments: {', '.join(assignment.name for assignment in self.assignments)}"


class Assignment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Assignment: {self.name}"


class ElearningPlatform:
    def __init__(self):
        self.courses = []
        self.users = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def register_user(self, user):
        self.users.append(user)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user

    def __str__(self):
        return f"E-learning Platform with Courses: {', '.join(course.title for course in self.courses)}"


# Example Usage with Assignments and Quizzes:
platform = ElearningPlatform()

# Create a course
course = Course("Computer Science", "Introduction to programming", "Professor Z")
platform.add_course(course)

# Create assignments
assignment1 = Assignment("Homework 1")
assignment2 = Assignment("Project 1")
course.add_assignment(assignment1)
course.add_assignment(assignment2)

# Create quizzes
quiz1 = Quiz("Quiz 1")
quiz2 = Quiz("Midterm Quiz")
course.add_quiz(quiz1)
course.add_quiz(quiz2)

# Create a user
username = input("Enter username: ")
password = input("Enter password: ")
user = User(username, password)
platform.register_user(user)

# Enroll the user in the course
user.enroll_course(course)

# Grade assignments and quizzes
grading_system = GradingSystem()
grading_system.grade_assignment(user, assignment1, 90)
grading_system.grade_assignment(user, assignment2, 85)
course.grade_quiz(user, quiz1, 95)
course.grade_quiz(user, quiz2, 80)

# Display information
print(platform)
print(user)
print(course)




