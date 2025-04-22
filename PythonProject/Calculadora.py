import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacion = combo_operacion.get()

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2

        lbl_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error", "¡Error! Ingrese números válidos.")

# Crear la ventana
window = tk.Tk()
window.title("Calculadora")

# Crear widgets
lbl_num1 = tk.Label(window, text="Número 1:")
entry_num1 = tk.Entry(window)

lbl_operacion = tk.Label(window, text="Operación:")
operaciones = ["+", "-", "*", "/"]
combo_operacion = tk.StringVar(window)
combo_operacion.set(operaciones[0])
combo = tk.OptionMenu(window, combo_operacion, *operaciones)

lbl_num2 = tk.Label(window, text="Número 2:")
entry_num2 = tk.Entry(window)

btn_calcular = tk.Button(window, text="Calcular", command=calcular)

lbl_resultado = tk.Label(window, text="Resultado:")

# Posicionar los widgets en la ventana
lbl_num1.pack()
entry_num1.pack()

lbl_operacion.pack()
combo.pack()

lbl_num2.pack()
entry_num2.pack()

btn_calcular.pack()

lbl_resultado.pack()

# Ejecutar la ventana
window.mainloop()
