class Vehicle:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km


class Bus(Vehicle):
    def total_fare(self, km):
        fare = km * self.rate_per_km
        maintenance = fare * 0.10   # 10% extra charge
        return fare + maintenance

bus = Bus(5)   
distance = int(input("Enter distance in km: "))

print("Total Fare:", bus.total_fare(distance))
