from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, basic_salary):
        self._basic_salary = basic_salary

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_basic_salary(self):
        print("Basic Salary:", self._basic_salary)



class FullTimeEmployee(Employee):

    def calculate_salary(self):
        hra = self._basic_salary * 0.20
        da = self._basic_salary * 0.10

        total_salary = self._basic_salary + hra + da

        return total_salary



salary = float(input("Enter the basic salary of the employee: "))
employee = FullTimeEmployee(salary)

employee.display_basic_salary()


print("Total Salary:", employee.calculate_salary())