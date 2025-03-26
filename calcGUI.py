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