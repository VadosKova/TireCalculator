from InputValid import InputValid

valid = InputValid()

width = valid.get_valid_input("Enter width (мм): ", "int")
tire_profile = valid.get_valid_input("Enter tire profile (%): ", "float")
diameter = valid.get_valid_input("Enter diameter (дюймы): ", "int")

print(f"Result:\nШирина шины: {width} мм\nВысота боковины: {tire_profile}%\nДиаметр обода: {diameter} дюймов")