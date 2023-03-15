
class Car:
    def __init__(self, Model, Fuel, Speed, Color):
        self.Model = Model
        self.Fuel  = Fuel
        self.Speed = Speed
        self.Color = Color


    def toJsonFormat(self):
        return {"model":self.Model,
            "fuel":self.Fuel,
            "speed":self.Speed,
            "color":self.Color}

    #Print vehicle embed data

    def toString(self):
        print("\nVehicle embed data")
        print(f"Model : {self.Model}")
        print(f"Fuel : {self.Fuel}")
        print(f"Speed : {self.Speed}")
        print(f"Color : {self.Color}\n")

    #The Getters start here

    def getModel(self):
        return self.Model

    def getFuel(self):
        return self.Fuel

    def getSpeed(self):
        return self.Speed

    def getColor(self):
        return self.Color

    #The Setters start here

    def setModel(self, NewModel):
        self.Model = NewModel

    def setFuel(self, NewFuel):
        self.Fuel = NewFuel

    def setSpeed(self, NewSpeed):
        self.Speed = NewSpeed

    def setReproduction(self, NewColor):
        self.Color = NewColor



