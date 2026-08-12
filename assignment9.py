from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,id):
        self._id=id

    @abstractmethod
    def get_role_details(self):
        pass

    def display_id(self):
        print("ID:",self._id)

class Teacher(Person):

    def __init__(self,id,subject):
        super().__init__(id)
        self._subject=subject
    #Implementing abstract method
    def get_role_details(self):
        print("Id:",self._id)
        print("Subject:",self._subject)

#create Teacher object
teacher_id = input("Enter the ID of the teacher: ")
teacher_subject = input("Enter the subject of the teacher: ")
teacher = Teacher(teacher_id, teacher_subject)

#use object to call methods
teacher.get_role_details()