from .Model import Person,Patient,Doctor,Appointment
Person
p1=Patient
d1=Doctor
apoint=Appointment
def PatientAppointment(patient_id, doctor_id, apoint):
    for apoint in apoint:
        if apoint.id == patient_id and apoint.id == doctor_id:
            return apoint
    return None
apoint = []
appointment = PatientAppointment(p1.id, d1.id, apoint)

# Print the result
if appointment:
    print(f"Patient {p1.name} has an appointment with DR {d1.name} on {appointment.appointment_date}.")
else:
    print(f"Patient {p1.name} doesn't have an appointment with DR {d1.name}.")


def doctorFinder(patient_id, appointments, doctors):
    for appointment in appointments:
        if appointment.patient_id == patient_id:
            for doctor in doctors:
                if doctor.id == appointment.doctor_id:
                    return doctor
    return None
appointments = [apoint]
doctors = [d1]

doctor = doctorFinder(p1.id, appointments, doctors)

# Print the result
if doctor:
    print(f"Patient {p1.name} has an appointment with Dr. {doctor.name} ({doctor.specialization}).")
else:
    print(f"Patient {p1.name} doesn't have any appointments.")



def appointments(patient_id,doctor_id,appointment_date):
    
    # print details of all appointments
 for appointment in appointments:
        patient_id = appointment.patient_id
        doctor_id = appointment.doctor_id
        appointment_date = appointment.appointment_date
        
 appointments = [apoint]
 print(f"Appointment: {appointment.id}")
 print(f"Patient: {patient_id}")
 print(f"Doctor: {doctor_id}")
 print(f"Date: {appointment_date}")