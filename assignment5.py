# MULTIPLE INHERITANCE

# 1. Printer + Scanner -> OfficeMachine

class Printer:
    def print_document(self, document):
        print(f"Printing document: {document}")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class OfficeMachine(Printer, Scanner):
    def __init__(self, machine_name):
        self.machine_name = machine_name

    def display_info(self):
        print(f"Office Machine: {self.machine_name}")


machine = OfficeMachine("Canon ImageClass")
machine.display_info()
machine.print_document("Assignment.pdf")
machine.scan_document()

print("----------------------------------------")


# 2. OnlinePayment + CashPayment -> BillingModule

class OnlinePayment:
    def pay_online(self, amount):
        print(f"Online payment of Rs.{amount} completed successfully")


class CashPayment:
    def pay_cash(self, amount):
        print(f"Cash payment of Rs.{amount} received successfully")


class BillingModule(OnlinePayment, CashPayment):
    def __init__(self, bill_no, customer_name):
        self.bill_no = bill_no
        self.customer_name = customer_name

    def display_bill_info(self):
        print(f"Bill Number: {self.bill_no}")
        print(f"Customer Name: {self.customer_name}")


bill = BillingModule("B205", "Rahul")
bill.display_bill_info()
bill.pay_online(2200)
bill.pay_cash(500)

print("----------------------------------------")


# 3. Calling + Camera -> SmartPhone

class Calling:
    def make_call(self, number):
        print(f"Calling {number}...")


class Camera:
    def take_photo(self):
        print("Photo captured successfully")


class SmartPhone(Calling, Camera):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_phone_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


phone = SmartPhone("OnePlus", "12R")
phone.display_phone_info()
phone.make_call("9123456789")
phone.take_photo()

print("----------------------------------------")


# 4. PersonalInfo + JobInfo -> Employee

class PersonalInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")


class JobInfo:
    def __init__(self, emp_id, designation):
        self.emp_id = emp_id
        self.designation = designation

    def display_job_info(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Designation: {self.designation}")


class Employee(PersonalInfo, JobInfo):
    def __init__(self, name, age, emp_id, designation):
        PersonalInfo.__init__(self, name, age)
        JobInfo.__init__(self, emp_id, designation)

    def display_employee_info(self):
        self.display_personal_info()
        self.display_job_info()


employee = Employee("Fathima", 24, "E205", "Data Analyst")
employee.display_employee_info()

print("----------------------------------------")


# 5. Logger + Database -> Application

class Logger:
    def log_message(self, message):
        print(f"Log: {message}")


class Database:
    def connect_database(self):
        print("Database connected successfully")


class Application(Logger, Database):
    def __init__(self, app_name):
        self.app_name = app_name

    def display_app_info(self):
        print(f"Application Name: {self.app_name}")


app = Application("Online Shopping System")
app.display_app_info()
app.connect_database()
app.log_message("User logged into the application")

print("----------------------------------------")


# 6. PersonalDetails + AcademicDetails -> StudentProfile

class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_personal_details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")


class AcademicDetails:
    def __init__(self, roll_no, course, cgpa):
        self.roll_no = roll_no
        self.course = course
        self.cgpa = cgpa

    def display_academic_details(self):
        print(f"Roll Number: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"CGPA: {self.cgpa}")


class StudentProfile(PersonalDetails, AcademicDetails):
    def __init__(self, name, age, roll_no, course, cgpa):
        PersonalDetails.__init__(self, name, age)
        AcademicDetails.__init__(self, roll_no, course, cgpa)

    def display_student_profile(self):
        self.display_personal_details()
        self.display_academic_details()


student = StudentProfile(
    "Aisha",
    21,
    "S205",
    "BCA",
    8.9
)

student.display_student_profile()

print("----------------------------------------")


# 7. Engine + Safety -> Car

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine_info(self):
        print(f"Engine Type: {self.engine_type}")


class Safety:
    def __init__(self, airbags):
        self.airbags = airbags

    def display_safety_info(self):
        print(f"Number of Airbags: {self.airbags}")


class Car(Engine, Safety):
    def __init__(self, brand, model, engine_type, airbags):
        self.brand = brand
        self.model = model

        Engine.__init__(self, engine_type)
        Safety.__init__(self, airbags)

    def display_car_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        self.display_engine_info()
        self.display_safety_info()


car = Car("Hyundai", "Creta", "Petrol", 6)
car.display_car_info()

print("----------------------------------------")