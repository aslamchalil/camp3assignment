#1. Product Stock

class Product:
    def add_stock(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(f"Added {quantity} items. Current stock = {self.quantity}")
        else:
            print("Enter valid quantity")

    def sell(self, quantity):
        if 0 < quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Sold {quantity} items. Current stock = {self.quantity}")
        else:
            print("Insufficient stock")

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Current stock = {self.quantity}")


product = Product()
product.name = "Nike Shoes"
product.price = 7500
product.quantity = 15

product.add_stock(8)
product.sell(4)
product.display()

#2. Employee Bonus

class Employee:
    def calculate_bonus(self):
        self.bonus = self.base_salary * 0.05 * self.years_of_service
        print(f"Bonus = {self.bonus}")

    def total_salary(self):
        total = self.base_salary + self.bonus
        print(f"Total Salary = {total}")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Experience: {self.years_of_service}")
        print(f"Bonus: {self.bonus}")


emp = Employee()
emp.name = "Rahul"
emp.base_salary = 28000
emp.years_of_service = 3

emp.calculate_bonus()
emp.total_salary()
emp.display()

#3. Bank Account

class BankAccount:
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current Balance = {self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Current Balance = {self.balance}")
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")


account = BankAccount()
account.account_holder = "Akhil"
account.account_number = 205
account.balance = 15000

account.deposit(4000)
account.withdraw(2500)
account.display()

#4. Student Result

class StudentResult:
    def calculate_result(self):
        if self.marks >= 40:
            print("Pass")
        else:
            print("Fail")

    def calculate_grade(self):
        if 90 <= self.marks <= 100:
            self.grade = "A"
        elif 75 <= self.marks <= 89:
            self.grade = "B"
        elif 60 <= self.marks <= 74:
            self.grade = "C"
        else:
            self.grade = "D"

        print(f"Grade: {self.grade}")

    def display(self):
        print(f"Student Name: {self.student_name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")


student = StudentResult()
student.student_name = "Neha"
student.roll_number = 27
student.marks = 86

student.calculate_result()
student.calculate_grade()
student.display()

#5 5. Library Book

class LibraryBook:
    def issue_book(self, quantity):
        available = self.total_copies - self.issued_copies

        if 0 < quantity <= available:
            self.issued_copies += quantity
            print(f"Issued {quantity} books")
        else:
            print("Books are not available")

    def return_book(self, quantity):
        if 0 < quantity <= self.issued_copies:
            self.issued_copies -= quantity
            print(f"Returned {quantity} books")
        else:
            print("Invalid return quantity")

    def display(self):
        available = self.total_copies - self.issued_copies
        print(f"Book Title: {self.book_title}")
        print(f"Author: {self.author}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Issued Copies: {self.issued_copies}")
        print(f"Available Copies: {available}")


book = LibraryBook()
book.book_title = "The Alchemist"
book.author = "Paulo Coelho"
book.total_copies = 25
book.issued_copies = 7

book.issue_book(4)
book.return_book(2)
book.display()

#6. Hotel Room

class HotelRoom:
    def book_room(self, rooms):
        available = self.total_rooms - self.booked_rooms

        if 0 < rooms <= available:
            self.booked_rooms += rooms
            print(f"{rooms} room(s) booked")
        else:
            print("Rooms are not available")

    def cancel_room(self, rooms):
        if 0 < rooms <= self.booked_rooms:
            self.booked_rooms -= rooms
            print(f"{rooms} room(s) cancelled")
        else:
            print("Invalid cancellation")

    def display(self):
        available = self.total_rooms - self.booked_rooms
        print(f"Room Number: {self.room_number}")
        print(f"Room Type: {self.room_type}")
        print(f"Total Rooms: {self.total_rooms}")
        print(f"Booked Rooms: {self.booked_rooms}")
        print(f"Available Rooms: {available}")


room = HotelRoom()
room.room_number = 205
room.room_type = "Deluxe"
room.total_rooms = 12
room.booked_rooms = 4

room.book_room(3)
room.cancel_room(1)
room.display()

#7 

class MovieTicket:
    def book_seats(self, seats):
        available = self.total_seats - self.booked_seats

        if 0 < seats <= available:
            self.booked_seats += seats
            print(f"{seats} seat(s) booked")
        else:
            print("Seats are not available")

    def cancel_seats(self, seats):
        if 0 < seats <= self.booked_seats:
            self.booked_seats -= seats
            print(f"{seats} seat(s) cancelled")
        else:
            print("Invalid cancellation")

    def display(self):
        print(f"Movie: {self.movie_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Booked Seats: {self.booked_seats}")


ticket = MovieTicket()
ticket.movie_name = "Avengers"
ticket.total_seats = 120
ticket.booked_seats = 45

ticket.book_seats(10)
ticket.cancel_seats(5)
ticket.display()

#8. Mobile Recharge

class MobileRecharge:
    def recharge(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Recharge added: {amount}")

    def use_balance(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Used balance: {amount}")
        else:
            print("Insufficient balance")

    def display(self):
        print(f"Mobile Number: {self.mobile_number}")
        print(f"Balance: {self.balance}")


mobile = MobileRecharge()
mobile.mobile_number = 9876543210
mobile.balance = 300

mobile.recharge(700)
mobile.use_balance(150)
mobile.display()

#9. Car Fuel

class Car:
    def refill_fuel(self, litres):
        if litres > 0 and self.current_fuel + litres <= self.fuel_capacity:
            self.current_fuel += litres
            print(f"Added {litres} litres of fuel")
        else:
            print("Invalid fuel quantity")

    def drive(self, litres):
        if 0 < litres <= self.current_fuel:
            self.current_fuel -= litres
            print(f"Used {litres} litres of fuel")
        else:
            print("Not enough fuel")

    def display(self):
        print(f"Car: {self.car_name}")
        print(f"Fuel Capacity: {self.fuel_capacity}")
        print(f"Current Fuel: {self.current_fuel}")


car = Car()
car.car_name = "Toyota Supra"
car.fuel_capacity = 70
car.current_fuel = 20

car.refill_fuel(25)
car.display()
car.drive(15)
car.display()

# 10. Shopping Cart

class ShoppingCart:
    def add_item(self, quantity):
        if quantity > 0:
            self.quantity += quantity
            print(f"Added {quantity} items")

    def remove_item(self, quantity):
        if 0 < quantity <= self.quantity:
            self.quantity -= quantity
            print(f"Removed {quantity} items")
        else:
            print("Invalid quantity")

    def display(self):
        print(f"Item Name: {self.item_name}")
        print(f"Item Price: {self.item_price}")
        print(f"Item Quantity: {self.quantity}")


item = ShoppingCart()
item.item_name = "Notebook"
item.item_price = 60
item.quantity = 12

item.add_item(5)
item.display()

item.remove_item(4)
item.display()

#