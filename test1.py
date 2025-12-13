class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting.")

    def stop(self):
        print("Vehicle is stopping.")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    # Below, we "override" the start and stop methods, inherited from Vehicle, to provide car-specific behaviour

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")
class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    # Below, we "override" the start and stop methods, inherited from Vehicle, to provide bike-specific behaviour

    def start(self):
        print("Motorcycle is starting.")

    def stop(self):
        print("Motorcycle is stopping.")
# Create list of vehicles to inspect
vehicles = [Car("Ford", "Focus", 2008, 5), Motorcycle("Honda", "Scoopy", 2018), "Plane"]

# Loop through list of vehicles and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")
