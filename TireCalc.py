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