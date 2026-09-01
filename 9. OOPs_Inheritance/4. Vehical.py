### Vehicle

# * brand

# ### Car

# * brand

# ### ElectricCar

# * model

# Requirements

# * Use `super()` in every constructor.
# * Create a method `showDetails()`.
# * Each class should call its parent method using `super()`.

# **Expected Output**

# ```
# Brand : Tesla
# Model : Model 3
# Battery : 75 kWh


class Vehical:
    def __init__(self, brand):
        self.brand = brand
        
class Car(Vehical):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    def showDetails(self):
        print(f"Name: {self.brand}")
        print(f"Roll : {self.model}")
        print(f"Marks : {self.battery_capacity}")
        
        
# Main()
car = ElectricCar('Tesla', 'Model 3', 75)
car.showDetails()