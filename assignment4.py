# MULTILEVEL INHERITANCE

# 1. Person -> Student -> Result

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, roll_number, course):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.course = course

    def display(self):
        super().display()
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")


class Result(Student):
    def __init__(self, name, age, roll_number, course, percentage):
        super().__init__(name, age, roll_number, course)
        self.percentage = percentage

    def display(self):
        super().display()
        print(f"Percentage: {self.percentage}")


student = Result("Zayan", 19, 31, "BSc", 88)
student.display()

print("----------------------------------------")


# 2. Animal -> Dog -> Puppy

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking")


class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age

    def play(self):
        print(f"{self.name} is playing")


puppy = Puppy("Bruno", "Beagle", 5)

puppy.play()
puppy.bark()
puppy.eat()

print("----------------------------------------")


# 3. Company -> Employee -> Salary

class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def display(self):
        print(f"Company Name: {self.company_name}")


class Employee(Company):
    def __init__(self, company_name, employee_id, name):
        super().__init__(company_name)
        self.employee_id = employee_id
        self.name = name

    def display(self):
        super().display()
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.name}")


class Salary(Employee):
    def __init__(self, company_name, employee_id, name, salary):
        super().__init__(company_name, employee_id, name)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Employee Salary: {self.salary}")


employee = Salary("TechNova", 3145, "Adil", 42000)
employee.display()