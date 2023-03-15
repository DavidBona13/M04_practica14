
#School class to manage the schools of Georgia
class School:
    def __init__(self, Faculty, Name, Location, Curriculum):
        self.Faculty    = Faculty
        self.Name       = Name
        self.Location   = Location
        self.Curriculum = Curriculum

    def toJsonFormat(self):
        return {"faculty":self.Faculty,
            "name":self.Name,
            "location":self.Location,
            "curriculum":self.Curriculum}

    #Print school embed data
    def Info(self):
        print("\nVehicle embed data")
        print(f"Faculty : {self.Faculty}")
        print(f"Name : {self.Name}")
        print(f"Location : {self.Location}")
        print(f"Curriculum : {self.Curriculum}\n")


    #The Getters start here

    def getFaculty(self):
        return self.Faculty

    def getName(self):
        return self.Name

    def getLocation(self):
        return self.Location

    def getCurriculum(self):
        return self.Curriculum


    #The Setters start here

    def setFaculty(self, NewFaculty):
        self.Faculty = NewFaculty

    def setName(self, NewName):
        self.Name = NewName

    def setLocation(self, NewLocation):
        self.Location = NewLocation

    def setCurriculum(self, NewCurriculum):
        self.Curriculum = NewCurriculum




