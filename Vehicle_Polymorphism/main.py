class BMW():
    def mileage(self):
        print("BMW mileage is 10km/l")
    def price(self):
        print("BMW price is 50 lakhs")
    def color(self):
        print("BMW color is black")
    def model(self):
        print("BMW model is 2020")
class Ferrari():
    def mileage(self):
        print("Ferrari mileage is 8km/l")
    def price(self):
        print("Ferrari price is 1 crore")
    def color(self):
        print("Ferrari color is red")
    def model(self):
        print("Ferrari model is 2021")
obj_bmw = BMW()
obj_ferrari = Ferrari()
for car in (obj_bmw, obj_ferrari):
    car.mileage()
    car.price()
    car.color()
    car.model()