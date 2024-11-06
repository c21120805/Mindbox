import tkinter as tk
from tkinter import messagebox
 
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        messagebox.showinfo("Resultado", f"La suma es: {suma}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def restar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resta = num1 - num2
        messagebox.showinfo("Resultado", f"La resta es: {resta}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def multiplicar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        producto = num1 * num2
        messagebox.showinfo("Resultado", f"La resta es: {producto}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def dividir():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        division = num1 / num2
        messagebox.showinfo("Resultado", f"La resta es: {division}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
 
 
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("423x300")
 
label_num1 = tk.Label(ventana, text="Número 1:", bg="lightblue", fg="black", font=("Calibri", 12, "bold"), relief="sunken", padx=10, pady=10)
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=1, column=0)
 
label_num2 = tk.Label(ventana, text="Número 2:", bg="lightblue", fg="black", font=("Calibri", 12, "bold"), relief="sunken", padx=10, pady=10)
label_num2.grid(row=0, column=6)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=6)
 
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar, bg="lightgreen", font=("Arial", 11, "bold"))
boton_sumar.grid(row=4, column=0)

boton_restar = tk.Button(ventana, text="Restar", command=restar, bg="lightgreen", font=("Arial", 11, "bold"))
boton_restar.grid(row=4, column=2)

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar, bg="lightgreen", font=("Arial", 11, "bold"))
boton_multiplicar.grid(row=4, column=4)

boton_division = tk.Button(ventana, text="Dividir", command=dividir, bg="lightgreen", font=("Arial", 11, "bold"))
boton_division.grid(row=4, column=6)

label_num3 = tk.Label(ventana, text="",padx=10, pady=10)
label_num3.grid(row=0, column=3)

label_num4= tk.Label(ventana, text="",padx=10, pady=10)
label_num4.grid(row=3, column=3)
 
ventana.mainloop()
 