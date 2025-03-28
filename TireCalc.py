import math
from Tire import Tire

class TireCalc:
    def __init__(self, tire):
        self.tire = tire

    def calculate_sidewall_height(self):
        return self.tire.width * (self.tire.tire_profile / 100)

    def calculate_diameter(self):
        sidewall_height = self.calculate_sidewall_height()
        return (sidewall_height * 2) + (self.tire.diameter * 25.4)

    def calculate_circumference(self):
        diameter = self.calculate_diameter()
        return math.pi * diameter

    def calculate_revolutions_per_km(self):
        circumference = self.calculate_circumference()
        return 1000 / circumference