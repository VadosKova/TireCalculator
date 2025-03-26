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