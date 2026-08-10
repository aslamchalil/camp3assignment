# SINGLE INHERITANCE

# 1. Person -> Student

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, course, percentage):
        super().__init__(name, age)
        self.course = course
        self.percentage = percentage

    def display(self):
        super().display()
        print(f"Course: {self.course}")
        print(f"Percentage: {self.percentage}")


student = Student("Ameen", 20, "BCA", 82)
student.display()

print("----------------------------------------")


# 2. Employee -> Manager

class Employee:
    def __init__(self, employee_id, employee_name):
        self.employee_id = employee_id
        self.employee_name = employee_name

    def displayDetails(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")


class Manager(Employee):
    def __init__(self, employee_id, employee_name, team):
        super().__init__(employee_id, employee_name)
        self.team = team

    def displayDetails(self):
        super().displayDetails()
        print(f"Team: {self.team}")


manager = Manager(205, "Nithin", "Development")
manager.displayDetails()

print("----------------------------------------")


# 3. Vehicle -> Bike

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} has started")


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        print(f"{self.brand} {self.model} is being ridden")


bike = Bike("Yamaha", "R15")
bike.start()
bike.ride()

print("----------------------------------------")


# 4. Account -> SavingsAccount

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def displayDetails(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculateInterest(self, rate):
        interest = self.balance * rate / 100
        total = self.balance + interest

        self.displayDetails()
        print(f"Interest Rate: {rate}%")
        print(f"Interest: {interest}")
        print(f"Total Balance: {total}")


account = SavingsAccount(307, 25000)
account.calculateInterest(8)

print("----------------------------------------")


# 5. Member -> LibraryMember

class Member:
    def __init__(self, member_id, member_name):
        self.member_id = member_id
        self.member_name = member_name

    def display(self):
        print(f"Member ID: {self.member_id}")
        print(f"Member Name: {self.member_name}")


class LibraryMember(Member):
    def __init__(self, member_id, member_name, books):
        super().__init__(member_id, member_name)
        self.books = books

    def display(self):
        super().display()
        print(f"Books Borrowed: {self.books}")


member = LibraryMember(208, "Farhan", 6)
member.display()