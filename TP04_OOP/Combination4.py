"""Practical OOP """

"""Student Management System"""

class Student:
    """ENCAPSULATION"""
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # Private attribute

    def get_score(self):
        return self.__score

class ScholarshipStudent(Student):
    """INHERITANCE"""
    def show_scholarship(self):
        print(self.name, "is a scholarship student.")


class Teacher:
    """POLYMORPHISM"""
    def show_role(self):
        print("I am a teacher.")

class StudentRole:
    def show_role(self):
        print("I am a student.")

from abc import ABC, abstractmethod

class SchoolSystem(ABC):
    """ABSTRACTION"""
    @abstractmethod
    def display(self):
        pass

class SchoolInfo(SchoolSystem):
    def display(self):
        print("Welcome to the Student Management System!")

student1 = ScholarshipStudent("Alex", 90)

# Encapsulation
print("Student:", student1.name)
print("Score:", student1.get_score())

# Inheritance
student1.show_scholarship()

# Polymorphism
teacher = Teacher()
student = StudentRole()

teacher.show_role()
student.show_role()

# Abstraction
school = SchoolInfo()
school.display()
