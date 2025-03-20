class Patient:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob

class Hospital:
    def __init__(self, ID, name, country):
        self.ID = ID
        self.name = name
        self.__patients = []
        self.country = ""
        self.max_occupancy = 100

    def occupancy(self) -> int:
        return len(self.__patients)

    def add_patient(self, patient):
        if self.occupancy() < self.max_occupancy:
            self.__patients.append(patient)

    def __len__(self):
        return len(self.__patients)

    def has_patient(self, patient_ID):
        for patient in self.__patients:
            if patient.ID == patient_ID:
                return True
        return False

    def __contains__(self, patient_ID):
        for patient in self.__patients:
            if patient.ID == patient_ID:
                return True
        return False


class HealthMinistry:
    def __init__(self):
        self.hospitals = []

    def add_hospital(self, hospital):
        if hospital.country != "Austria":
            print("Can only add Austrian hospitals")
            return

        self.hospitals.append(hospital)

    def getHospitalByID(self, ID):
        for hospital in self.hospitals:
            if hospital.ID == ID:
                return hospital
        print("Hospital not found")

    def deleteHospital(self, hospital):
        pass


# hm = HealthMinistry()
h1 = Hospital(1, "H1", "Austria")
# h2 = Hospital(2, "H2")

# hm.hospitals.append(h1)
# hm.add_hospital(h2)

h1.add_patient(Patient(1, "P1", None))
p2 = Patient(2, "P2", None)
h1.add_patient(p2)
h1._Hospital__patients.append(Patient(1, "P3", None))

print(h1.occupancy())

print("Occupancy of h1:", len(h1))

print(2 in h1)