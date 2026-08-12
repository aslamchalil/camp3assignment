class ElectricityBill:
    def calculate_bill(self, units):
        return units * 5


class DomesticBill(ElectricityBill):
    def calculate_bill(self, units):
        if units <= 100:
            return units * 5
        else:
            return (100 * 5) + ((units - 100) * 3)


class CommercialBill(ElectricityBill):
    def calculate_bill(self, units):
        bill = units * 8
        tax = bill * 0.10
        return bill + tax


# Create objects
base_bill = ElectricityBill()
domestic_bill = DomesticBill()
commercial_bill = CommercialBill()

# Units consumed
units = int(input("Enter the unit consumed: "))

# Calculate and display bills
print("Base Electricity Bill:", base_bill.calculate_bill(units))
print("Domestic Bill:", domestic_bill.calculate_bill(units))
print("Commercial Bill:", commercial_bill.calculate_bill(units))