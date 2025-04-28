import math
import json
import os
import tkinter as tk
from tkinter import messagebox, filedialog

ARCHIVO_JSON = "circulos.json"

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
        return {
            "radio": self.radio,
            "area": round(self.calcular_area(), 2),
            "circunferencia": round(self.calcular_circunferencia(), 2),
            "diametro": round(self.calcular_diametro(), 2)
        }

class AplicacionCirculo:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Círculos - Nivel 8")
        self.root.geometry("500x450")
        self.root.configure(bg="#f0f0f0")

        self.circulos = self.cargar_datos()

        # Entrada de radio
        self.lbl_radio = tk.Label(root, text="Ingrese el radio del círculo:", bg="#f0f0f0")
        self.lbl_radio.pack(pady=5)
        self.entry_radio = tk.Entry(root)
        self.entry_radio.pack(pady=5)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar Círculo", command=self.agregar_circulo, bg="#4CAF50", fg="white")
        self.btn_agregar.pack(pady=5)
        self.btn_mostrar = tk.Button(root, text="Mostrar Cálculos", command=self.mostrar_resultados, bg="#2196F3", fg="white")
        self.btn_mostrar.pack(pady=5)
        self.btn_guardar = tk.Button(root, text="Guardar Resultados", command=self.guardar_resultados, bg="#FF9800", fg="white")
        self.btn_guardar.pack(pady=5)
        self.btn_eliminar = tk.Button(root, text="Eliminar Último Círculo", command=self.eliminar_ultimo, bg="#f44336", fg="white")
        self.btn_eliminar.pack(pady=5)

        # Área de texto para mostrar cálculos
        self.text_area = tk.Text(root, height=10, width=60)
        self.text_area.pack(pady=10)

    def agregar_circulo(self):
        try:
            radio = float(self.entry_radio.get())
            circulo = Circulo(radio)
            self.circulos.append(circulo.obtener_resultados())
            self.guardar_datos()
            messagebox.showinfo("Éxito", "Círculo agregado correctamente.")
            self.entry_radio.delete(0, tk.END)  
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_resultados(self):
        self.text_area.delete("1.0", tk.END)  
        if not self.circulos:
            self.text_area.insert(tk.END, "⚠️ No hay círculos almacenados.\n")
        else:
            for c in self.circulos:
                self.text_area.insert(tk.END, f"Radio: {c['radio']}\nÁrea: {c['area']}\nCircunferencia: {c['circunferencia']}\nDiámetro: {c['diametro']}\n-----------------\n")

    def guardar_resultados(self):
        if not self.circulos:
            messagebox.showwarning("Advertencia", "No hay resultados para guardar.")
            return

        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, "w") as file:
                for c in self.circulos:
                    file.write(f"Radio: {c['radio']}\nÁrea: {c['area']}\nCircunferencia: {c['circunferencia']}\nDiámetro: {c['diametro']}\n-----------------\n")
            messagebox.showinfo("Éxito", f"Resultados guardados en {archivo}")

    def eliminar_ultimo(self):
        if not self.circulos:
            messagebox.showwarning("Advertencia", "No hay círculos para eliminar.")
            return
        self.circulos.pop()
        self.guardar_datos()
        messagebox.showinfo("Éxito", "Último círculo eliminado.")
        self.mostrar_resultados()

    def guardar_datos(self):
        with open(ARCHIVO_JSON, "w") as file:
            json.dump(self.circulos, file)

    def cargar_datos(self):
        if os.path.exists(ARCHIVO_JSON):
            with open(ARCHIVO_JSON, "r") as file:
                return json.load(file)
        return []

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionCirculo(root)
    root.mainloop()
