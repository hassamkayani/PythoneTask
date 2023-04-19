class Person:
    def __init__(self, id, name):
        def __str__(self):
         return f"Patient is:{self.id}-({self.name})-{self.age}-{self.gender}"
     
        self.id = id
        self.name = name

class Patient(Person):
    def __init__(self, id, name, age, gender):
        super().__init__(id, name)
        self.age = age
        self.gender = gender

class Doctor(Person):
    def __init__(self, id, name, specialization):
        super().__init__(id, name)
        self.specialization = specialization
       

class Appointment:
    def __init__(self, id, patient_id, doctor_id, appointment_date):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date

def main():
#create and Read 
    def __str__(self):
        return f"{self.id}-({self.name})-{self.age}-{self.gender}"
    
p1 = Patient(1, "Hassam",22,"Male")

print("Patient is-------",f"{p1.id}-{p1.name}-{p1.age}-{p1.gender}")

    
d1 = Doctor(1,"Ahmad","cardiology")

print("Doctor is-------",f"{d1.id}-{d1.name}-{d1.specialization}")

apoint=Appointment(1,1,1,2024-4-20)

print("Appointment is-------",f"{apoint.patient_id}--{apoint.doctor_id}--{apoint.appointment_date}")
def find_appointment(patient_id, doctor_id, apoint):
    for appointment in apoint:
        if apoint.id == patient_id and apoint.id == doctor_id:
            return apoint
    return None
apoint = []
appointment = find_appointment(p1.id, d1.id, apoint)

# Print the result
if appointment:
    print(f"Patient {p1.name} has an appointment with Dr. {d1.name} on {appointment.appointment_date}.")
else:
    print(f"Patient {p1.name} doesn't have an appointment with Dr. {d1.name}.")

# # Update data
# p1.name="Mavia"
# p1.age = 36
# p1.gender = "Male"
# d1.specialization = "Kidney"
# apoint.appointment_date = "2023-6-2"

# # Print updated data
# print("Updated Patients:")
# print(f"{p1.id}-{p1.name}-{p1.age}-{p1.gender}")

# print("Updated Doctors:")
# print(f"{d1.id}-{d1.name}-{d1.specialization}")

# print("Updated Appointments:")
# print(f"{apoint.id}-{apoint.patient_id}-{apoint.doctor_id}-{apoint.appointment_date}")

#now delete Pitient/Doctor/appointment

# if p1.name=="Mavia":
#     del p1.id,p1.name,p1.age,p1.gender
#     print("deleted Successfully")
# else:
#     print("Not Found")

#seacrh Person
# print("\n Search Patient-----")
# if p1.name=="Mavia":
#   print("found")
# else:
#     print("Not Found")





     


      