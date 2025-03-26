class Tire:
    def __init__(self, width, tire_profile, diameter):
        self.width = width
        self.tire_profile = tire_profile
        self.diameter = diameter

    def calc_result(self, tire_calc):
        sidewall_height = tire_calc.calculate_sidewall_height()
        diameter = tire_calc.calculate_diameter()
        circumference = tire_calc.calculate_circumference()
        revolutions = tire_calc.calculate_revolutions_per_km()

        return (f"Шина {self.width}/{self.tire_profile} R{self.diameter}:\n"
                f"  Высота боковины: {sidewall_height:.2f} мм\n"
                f"  Диаметр обода: {self.diameter * 25.4:.2f} мм\n"
                f"  Общий диаметр: {diameter:.2f} мм\n"
                f"  Длина окружности: {circumference:.2f} мм\n"
                f"  Число оборотов на 1 км: {revolutions:.2f} оборотов")