import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

messagebox.showerror("Error","Something went wrong")

messagebox.showerror("Info","Show")

messagebox.showerror("Warning","Show")

messagebox.showerror("Critical","Show")