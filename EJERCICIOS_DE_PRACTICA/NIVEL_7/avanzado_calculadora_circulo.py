import math
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise ValueError("Error: El radio debe ser un número positivo mayor que cero.")
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_circunferencia(self):
        return 2 * math.pi * self.radio

    def calcular_diametro(self):
        return 2 * self.radio

    def obtener_resultados(self):
        return (f"Radio: {self.radio}\n"
                f"Área: {round(self.calcular_area(), 2)}\n"
                f"Circunferencia: {round(self.calcular_circunferencia(), 2)}\n"
                f"Diámetro: {round(self.calcular_diametro(), 2)}\n"
                "------------------------\n")

class AplicacionCirculo:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Círculos")
        self.root.geometry("400x400")
        self.circulos = []  # Lista para almacenar círculos

        # Entrada de radio
        self.lbl_radio = tk.Label(root, text="Ingrese el radio del círculo:")
        self.lbl_radio.pack()
        self.entry_radio = tk.Entry(root)
        self.entry_radio.pack()

        # Botón para agregar círculo
        self.btn_agregar = tk.Button(root, text="Agregar Círculo", command=self.agregar_circulo)
        self.btn_agregar.pack()

        # Botón para mostrar resultados
        self.btn_mostrar = tk.Button(root, text="Mostrar Cálculos", command=self.mostrar_resultados)
        self.btn_mostrar.pack()

        # Botón para guardar resultados
        self.btn_guardar = tk.Button(root, text="Guardar Resultados", command=self.guardar_resultados)
        self.btn_guardar.pack()

        # Área de texto para mostrar cálculos
        self.text_area = tk.Text(root, height=10, width=50)
        self.text_area.pack()

    def agregar_circulo(self):
        try:
            radio = float(self.entry_radio.get())
            circulo = Circulo(radio)
            self.circulos.append(circulo)
            messagebox.showinfo("Éxito", "Círculo agregado correctamente.")
            self.entry_radio.delete(0, tk.END)  # Limpia el campo de entrada
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resultados(self):
        self.text_area.delete("1.0", tk.END)  # Limpia el área de texto
        if not self.circulos:
            self.text_area.insert(tk.END, "⚠️ No hay círculos almacenados.\n")
        else:
            for circulo in self.circulos:
                self.text_area.insert(tk.END, circulo.obtener_resultados())

    def guardar_resultados(self):
        if not self.circulos:
            messagebox.showwarning("Advertencia", "No hay resultados para guardar.")
            return

        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "w") as file:
                for circulo in self.circulos:
                    file.write(circulo.obtener_resultados())
            messagebox.showinfo("Éxito", f"Resultados guardados en {archivo}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCirculo(root)
    root.mainloop()
