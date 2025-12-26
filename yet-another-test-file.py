from abc import ABC, abstractmethod

# ---------------- ABSTRACTION ----------------
class Person(ABC):
    def __init__(self, name, age):
        self.name = name        # Encapsulation
        self.age = age

    @abstractmethod
    def role(self):
        pass


# ---------------- INHERITANCE ----------------
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.__marks = marks    # Private data (Encapsulation)

    # Getter method (Encapsulation)
    def get_marks(self):
        return self.__marks

    # Polymorphism (method overriding)
    def role(self):
        return "I am a Student"

    def result(self):
        return "Pass" if self.__marks >= 40 else "Fail"


class Teacher(Person):
    def role(self):
        return "I am a Teacher"


# ---------------- POLYMORPHISM ----------------
def show_role(person):
    print(person.role())


# ---------------- OBJECT CREATION ----------------
s1 = Student("Rahul", 20, 75)
t1 = Teacher("Mr. Sharma", 45)

print("Student Name:", s1.name)
print("Student Age:", s1.age)
print("Student Marks:", s1.get_marks())
print("Student Result:", s1.result())

show_role(s1)
show_role(t1)


# ---------------- DESTRUCTOR ----------------
class Demo:
    def __del__(self):
        print("Destructor called, object deleted")

obj = Demo()
del obj