# polymorphism in different class with same methods name

class Bank_Account:
    def display(self):
        print("This is Bank_Account Class")

class Saving_Account:
    def display(self):
        print("This is Saving_Account Class")

class Current_Account:
    def display(self):
        print("This is Current_Account Class")


account=[Bank_Account(),Saving_Account(),Current_Account()]

# for acc in account:
#     #acc.display()


#polymorphism in parent-child class with same name parameter

class Vechile:
    def __init__(self,brand_name,model_number):
        self.brand_name=brand_name
        self.model_num=model_number

    def Move(self):
        return "Moving"

class Car(Vechile):
    def __init__(self, brand_name, model_number,car_name):
        super().__init__(brand_name, model_number)
        self.car_name=car_name

    def Move(self):
        return "Drive"
    
class Boat(Vechile):
    def __init__(self, brand_name, model_number,boat_name):
        super().__init__(brand_name, model_number)
        self.boat_name=boat_name


class Airplan(Vechile):
    def __init__(self, brand_name, model_number,airplane_name):
        super().__init__(brand_name, model_number)
        self.airplane_name=airplane_name

    def Move(self):
        return "flyy!"
    

ferrari=Car("ford","339djbd93","ferrari")
Titanic=Boat("Titan","kknd3kn","titanic")
flouto=Airplan("tata","jhas8jd","fluto")

print(ferrari.Move())
print(Titanic.Move())
print(flouto.Move())