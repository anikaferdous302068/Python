class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelX = Vehicle(240, 18)
modelY = Vehicle(220, 16)
print("Model X Max Speed:", modelX.max_speed, "km/h")
print("Model Y Max Speed:", modelY.max_speed, "km/h")
print("Model X Mileage:", modelX.mileage, "km/l")
print("Model Y Mileage:", modelY.mileage, "km/l")