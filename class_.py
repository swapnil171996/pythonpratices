"""
Classs
Mathod
object
Variable
"""
class ABC:
    def greetnig (self):
        print("good morning")

obj_var=ABC()
obj_var.greetnig() #good morning

class add:
    def __init__(self):
        print("Initiate object Memory")
    def addition(self):
        num1=50
        num2=100
        print("addition of two number",num1+num2)
obj_var2=add()
obj_var2.addition() #Initiate object Memory
#addition of two number 150


class Car:
    def __init__(self,car_name,car_price,car_model):
        self.Car_name=car_name
        self.Car_price=car_price
        self.Car_model=car_model
        self.Car_milage="20km/l"
        self.show_greetings()
    def show_greetings(self):
        print(f"welocome to {self.Car_name}")

    def carname(self):
        print("carname:",self.Car_name)
    def carprice(self):
        print("carprice:",self.Car_price)
    def carmodel(self):
        print("carmodel:",self.Car_model)
    def cardetails(self):
        print("car  details")
        print("Name:",self.Car_name)
        print("Price:",self.Car_price)
        print("model:",self.Car_model)
        print("milage:", self.Car_milage)
obj=Car("TATA",1200000,car_model="Nexon")

obj.carname()
obj.carmodel()
obj.carprice()
obj.cardetails()






