import tkinter as tk
from tkinter import messagebox

class SandwichApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menu de Sandwiches")
        self.geometry("400x300")

        
class welcomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.label = tk.Label(self, text="Bienvenido a SubGuey", font=("Times New Roman", 16), fg="black")
        self.label.pack(pady=20)