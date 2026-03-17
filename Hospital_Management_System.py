
#! project feature:

# 1. Hospital details
# 2. Doctor registration
# 3. Patient registration
# 4. Doctor specialization search
# 5. Appointment booking
# 6. Show all doctors
# 7. Show all patients

#! This will use important OOPs concept:

# 1. Classes
# 2. Objects
# 3. Constructors
# 4. Methods
# 5. Composition
# 6. Lists


#! Hospital Class

class Hospital:
    
    def __init__(self, hosp_name, location):
        self.hosp_name = hosp_name
        self.location = location
        
        self.doctors = []
        self.patients = []
    
    def show_hospital_details(self):
        
        print("Hospital name : ", self.hosp_name)
        print("Location : ", self.location)
    
    #!Add doctor
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print("Doctor added successfully..")
    
    #!Add patient 
    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully..")
        
    def show_all_doctors(self):
        print("Doctor List")
        
        for doctor in self.doctor:
            doctor.show_details()
            print()    
    
    def show_all_patient(self):
        print("Patients List")
        
        for patient in self.patients:
            patient.show_details()
            print()
            
    def book_appointment(self, doctor, patient):
        print(patient.name, "is Appointment with", doctor.name)

#! Doctor Class
       
class Doctor:
    
    def __init__(self, name, specialization, experience):
        self.name = name
        self.specialization = specialization
        self.experience = experience
        
    def show_doctor_details(self):
        print("Docotor name : ", self.name)
        print("Specialization : ", self.specialization)
        print("Experience : ", self.experience)
        print()
        
#! Patient Class

class Patient:
    
    def __init__(self, name, age ,disease):
        self.name = name
        self.age = age
        self.disease = disease
        
    def show_patient_details(self):
        print("Patient name : ", self.name)
        print("Age : ", self.age)
        print("disease : ", self.disease)
        print()
        
#! Create hospital
hospital = Hospital("Mangla Hospital", "Gowaliar")

#!Create doctors
doctor1 = Doctor("Dr Karan", "cardiologist", "10 years")
doctor1 = Doctor("Dr Niraj", "neurologist", "12 years")

#!Create patients
patient1 = Patient("Arun singh tomar", 20, "Fever")
patient2 = Patient("Gopi yadav", 22, "cold")

#!Add patients
hospital.add_patient(patient1)
hospital.add_patient(patient2)

hospital.show_hospital_details()
hospital.book_appointment(patient2, doctor1)