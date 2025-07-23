class vehicle:
    def __init__(self,brand,fuel_type):
        self.brand=brand
        self.fuel_type=fuel_type
    def display_info(self):
        print(f"Brand       :{self.brand}")
        print(f"Fuel type   :{self.fuel_type}")
class Car(vehicle):
    def __init__(self,brand,fuel_type,model):
        super().__init__(brand,fuel_type)
        self.model=model
    def display_details(self):
        self.display_info()
        print(f"model       :{self.model}")
c=Car("toyota","petrol","sedan" )
c.display_details()

