import math
from Tire import Tire

class TireCalc:
    def __init__(self, tire):
        self.tire = tire

    def calculate_sidewall_height(self):
        return self.tire.width * (self.tire.tire_profile / 100)