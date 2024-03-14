"""

Name:Shanie Portal
Date: 09/09/2023
Assignment:Assignment #2: Hospital Patient Class
Due Date:09/09/2023
About this project:This is a simple program creating and displaying three instances of the class Patient.
Assumptions:No assumptions are made in this program as it doesn't take user input.
All work below was performed by Shanie Portal

"""

#Declaration of Patient Class.
class Patient:
    def __init__(self, PatientId, Name, Age, PhoneNumber,PositiveForCOVID):
        self.PatientId = PatientId
        self.Name = Name
        self.Age = Age
        self.PhoneNumber = PhoneNumber
        self.PositiveForCOVID = PositiveForCOVID


#Creating instance of Patient class: Patient1.
Patient1 = Patient(7, "James Bond", 78, "123-456-9876", "True")
#Displaying intance of Patient class: Patient1.
print("Patient 1:")
print("Patient ID: ", Patient1.PatientId)
print("Patient Name: ", Patient1.Name)
print("Patient Age: ", Patient1.Age)
print("Patient Phone Number: ", Patient1.PhoneNumber)
print("Positive For COVID: ", Patient1.PositiveForCOVID)

#Creating instance of Patient class: Patient2.
Patient2 = Patient(100, "Kim Smith", 34, "765-231-6745", "False")
#Displaying intance of Patient class: Patient2.
print("\nPatient 2:")
print("Patient ID: ", Patient2.PatientId)
print("Patient Name: ", Patient2.Name)
print("Patient Age: ", Patient2.Age)
print("Patient Phone Number: ", Patient2.PhoneNumber)
print("Positive For COVID: ", Patient2.PositiveForCOVID)

#Creating instance of Patient class: Patient3.
Patient3 = Patient(9, "Tom Hatfield", 51, "231-967-4476", "True")
#Displaying intance of Patient class: Patient3.
print("\nPatient 3:")
print("Patient ID: ", Patient3.PatientId)
print("Patient Name: ", Patient3.Name)
print("Patient Age: ", Patient3.Age)
print("Patient Phone Number: ", Patient3.PhoneNumber)
print("Positive For COVID: ", Patient3.PositiveForCOVID)