class Patient:
    def __init__(self, ID, name, dob):
        self.ID = ID
        self.name = name
        self.dob = dob

class Hospital:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.patients = []
        self.staff = []

    def occupancy(self):
        return len(self.patients)

    def admission(self, patient):
        self.patients.append(patient)

    def serialize(self):
        pass

    def __add__(self, other):
        if isinstance(other, Patient):
            self.patients.append(other)
        elif isinstance(other, Hospital):
            self.patients.extend(other.patients)
        else:
            print("Can't do what you want.")

    def __contains__(self, ID):
        for p in self.patients:
            if p.ID == ID:
                return True
        return False

    def isPatientInHospital(self, ID):
        for p in self.patients:
            if p.ID == ID:
                return True
        return False

class HealthMinistry:
    def __init__(self):
        # self.hospitals = []
        self.__hospitals = {}

    def getHospitals(self):
        return self.__hospitals

    def addHospital(self, hospital):
        # self.hospitals.append(hospital)
        self.__hospitals[hospital.ID] = hospital

    def getHospitalByID(self, ID):
        return self.__hospitals[ID]

        # for hospital in self.hospitals:
        #     if hospital.ID == ID:
        #         return hospital
        # return None

    def __len__(self):
        return len(self.__hospitals)

hm = HealthMinistry()
h1 = Hospital('H1', 'Hospital Krems')
h2 = Hospital('H2', 'Hospital Vienna')

hm.addHospital(h2)
hm.addHospital(h1)  # << I don't want people to do this!

print("HM has ", len(hm), "hospitals to maintain")

p1 = Patient('P1', 'Patient Stefan', None)
p2 = Patient('P2', 'Patient Lisa', None)
p3 = Patient('P3', 'Patient Mary', None)

h1.admission(p1)
h1.admission(p2)
# h1.admission(p3)
print("before", h1.occupancy())
h1 + p3
print("after", h1.occupancy())

print("P1" in h1)
print(h1.isPatientInHospital(p1))

print("Does not exist" in h1)


# class MyCoolList:
#     def __init__(self):
#         self.values = []
#
#     def __contains__(self, item):
#         for value in self.values:
#             if ....:
#                 return Ture
#
#     def __getitem__(self, item):

# A + B ==>
# A.__add__(B)

def len(obj):
    if hasattr(obj, "__len__"):
        return obj.__len__()
    else:
        "Crash and die"