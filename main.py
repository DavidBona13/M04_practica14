#integrant_A imports
import json

from Integrante_A.car import Car
from Integrante_A.school import School

cars = [Car("Toyota Camry", "Gasoline", "120", "Red"),
        Car("Tesla Model S", "Electric", "130", "Black"),
        Car("BMW i8", "Hybrid", "155", "White"),
        Car("Mercedes-Benz S-Class", "Diesel", "140", "Gray")]

schools = [School("Engineering", "Ivy University", "New York City", "Aerospace, Biomedical, Chemical, Civil, Electrical"),
           School("Arts", "Liberty University", "Lynchburg", "Music, Theater, Creative, Writing, Visual Arts"),
           School("Bussiness", "Grove University", "Philadelphia", "Accounting, Finance, Management, Marketing"),
           School("Education","Horizon University", "Seattle", "Early Childhood Education, Speacial Education, Counseling")]

cars_list = [c.toJsonFormat() for c in cars]
school_list = [s.toJsonFormat() for s in schools]

gen_data = {"cars":cars_list, "school":school_list}

with open("jsonAPI_A/data.json", 'w') as file:
    json.dump(gen_data,file)
