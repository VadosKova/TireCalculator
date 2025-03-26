from Tire import Tire
from TireCalc import TireCalc

print("---Введите параметры шины---")

width = int(input("Ширина шины (мм): "))
aspect_ratio = int(input("Высота боковины (%): "))
diameter = int(input("Диаметр обода (дюймы): "))

tire = Tire(width, aspect_ratio, diameter)
tire_calc = TireCalc(tire)

res = tire.calc_result(tire_calc)
print("\nРезультаты расчетов:")
print(res)