from tkinter import *
from tkinter import messagebox
from Tire import Tire
from TireCalc import TireCalc
from InputValid import InputValid


class CalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tire Calculator")
        self.root.geometry("400x400")

        self.width_label = Label(self.root, text="Ширина шины (мм):")
        self.width_label.grid(row=0, column=0)
        self.width_entry = Entry(self.root)
        self.width_entry.grid(row=0, column=1)

        self.tire_profile_label = Label(self.root, text="Профиль шины (%) :")
        self.tire_profile_label.grid(row=1, column=0)
        self.tire_profile_entry = Entry(self.root)
        self.tire_profile_entry.grid(row=1, column=1)

        self.diameter_label = Label(self.root, text="Диаметр обода (дюймы):")
        self.diameter_label.grid(row=2, column=0)
        self.diameter_entry = Entry(self.root)
        self.diameter_entry.grid(row=2, column=1)

        self.calc_btn = Button(self.root, text="Рассчитать", command=self.calculate_tire)
        self.calc_btn.grid(row=3, column=0, columnspan=2)

        self.result_text = Text(self.root, width=40, height=10)
        self.result_text.grid(row=4, column=0, columnspan=2)

    def calculate_tire(self):
        width = self.width_entry.get()
        tire_profile = self.tire_profile_entry.get()
        diameter = self.diameter_entry.get()

        input_validator = InputValid()

        if not (input_validator.validate_input(width, 'int') and input_validator.validate_input(tire_profile,'float') and input_validator.validate_input(diameter, 'int')):
            messagebox.showerror("Error", "Введите корректные данные")
            return

        width = int(width)
        tire_profile = int(tire_profile)
        diameter = int(diameter)

        tire = Tire(width, tire_profile, diameter)
        tire_calc = TireCalc(tire)
        res = tire.calc_result(tire_calc)

        self.result_text.delete(1.0, END)
        self.result_text.insert(END, res)

root = Tk()
gui = CalcGUI(root)

root.mainloop()