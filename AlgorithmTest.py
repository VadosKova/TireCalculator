from Tire import Tire
from TireCalc import TireCalc

print("---Введите параметры шины---")

width = int(input("Ширина шины (мм): "))
tire_profile = int(input("Профиль шины (%): "))
diameter = int(input("Диаметр обода (дюймы): "))

tire = Tire(width, tire_profile, diameter)
tire_calc = TireCalc(tire)

res = tire.calc_result(tire_calc)
print("\nРезультаты расчетов:")
print(res)