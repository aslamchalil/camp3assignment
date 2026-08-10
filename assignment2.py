class Verify:

    def __init__(self, pin):
        correct_pin = 5678

        if correct_pin == pin:
            print("Login successful")
        else:
            print("Invalid PIN")


pin = int(input("Enter your PIN: "))
password = Verify(pin)


class Box:

    def get_volume(self):
        volume = self.width * self.height * self.depth
        print("Volume:", volume)


box1 = Box()

box1.width = 4
box1.height = 5
box1.depth = 2

box1.get_volume()


box2 = Box()

box2.width = 6
box2.height = 3
box2.depth = 4

box2.get_volume()


class Box:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def get_volume(self):
        volume = self.width * self.height * self.depth
        print("Volume:", volume)


box1 = Box(4, 5, 2)
box1.get_volume()

box2 = Box(6, 3, 4)
box2.get_volume()


class BillingSystem:

    def __init__(self, country_name, language, customer_id,
                 billing_date, amount_outstanding):

        self.country_name = country_name
        self.language = language
        self.customer_id = customer_id
        self.billing_date = billing_date
        self.amount_outstanding = float(amount_outstanding)

    def display_details(self):
        print(f"Country: {self.country_name}")
        print(f"Language: {self.language}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Billing Date: {self.billing_date}")
        print(f"Amount Outstanding: {self.amount_outstanding}")


customer1 = BillingSystem(
    'India',
    'Malayalam',
    201,
    '2026-07-10',
    45000
)

customer1.display_details()

print("------------------------------")

customer2 = BillingSystem(
    'Germany',
    'German',
    202,
    '2026-08-05',
    78000
)

customer2.display_details()

print("------------------------------")



class Patient:

    hospital_name = 'GreenLife Hospital'

    def __init__(self, patient_id, name, age, admitted_days, daily_charge):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.admitted_days = admitted_days
        self.daily_charge = daily_charge

    def calculate_bill(self):
        return self.admitted_days * self.daily_charge

    @classmethod
    def change_hospital_name(cls, new_name):
        cls.hospital_name = new_name
        print(f"New hospital name: {cls.hospital_name}")

    @staticmethod
    def is_senior(age):
        return age >= 60

    def __str__(self):
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Admitted Days: {self.admitted_days}\n"
            f"Daily Charge: {self.daily_charge}\n"
            f"Hospital: {Patient.hospital_name}"
        )


patient1 = Patient(205, 'Arjun', 35, 7, 1500)

print('Total Bill:', patient1.calculate_bill())

patient1.change_hospital_name('Sunrise Medical Centre')

print('Senior:', patient1.is_senior(65))

print(patient1.__str__())



