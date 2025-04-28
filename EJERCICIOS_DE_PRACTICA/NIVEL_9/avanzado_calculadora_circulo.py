import sys
import math
import sqlite3
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
from PyQt6.QtGui import QFont
import matplotlib.pyplot as plt
import numpy as np

# Configuración de la base de datos SQLite
DB_FILE = "circulos.db"

def inicializar_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS circulos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        radio REAL,
                        area REAL,
                        circunferencia REAL,
                        diametro REAL)''')
    conn.commit()
    conn.close()

class CalculadoraCirculo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculadora de Círculos - Nivel 9")
        self.setGeometry(100, 100, 500, 500)
        
        layout = QVBoxLayout()

        # Etiqueta y entrada para el radio
        self.label = QLabel("Ingrese el radio del círculo:")
        self.label.setFont(QFont("Arial", 12))
        layout.addWidget(self.label)

        self.input_radio = QLineEdit()
        layout.addWidget(self.input_radio)

        # Botón para calcular
        self.btn_calcular = QPushButton("Calcular")
        self.btn_calcular.clicked.connect(self.calcular)
        layout.addWidget(self.btn_calcular)

        # Botón para mostrar historial
        self.btn_historial = QPushButton("Mostrar Historial")
        self.btn_historial.clicked.connect(self.mostrar_historial)
        layout.addWidget(self.btn_historial)

        # Botón para graficar
        self.btn_graficar = QPushButton("Graficar Círculo")
        self.btn_graficar.clicked.connect(self.graficar_circulo)
        layout.addWidget(self.btn_graficar)

        # Área de resultados
        self.resultados = QTextEdit()
        self.resultados.setReadOnly(True)
        layout.addWidget(self.resultados)

        self.setLayout(layout)

    def calcular(self):
        try:
            radio = float(self.input_radio.text())
            if radio <= 0:
                raise ValueError("El radio debe ser mayor que cero.")

            # Cálculos
            area = math.pi * radio**2
            circunferencia = 2 * math.pi * radio
            diametro = 2 * radio

            resultado_texto = (f"Radio: {radio}\n"
                                f"Área: {round(area, 2)}\n"
                                f"Circunferencia: {round(circunferencia, 2)}\n"
                                f"Diámetro: {round(diametro, 2)}\n")
            self.resultados.setText(resultado_texto)

            # Guardar en la base de datos
            conn = sqlite3.connect(DB_FILE)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO circulos (radio, area, circunferencia, diametro) VALUES (?, ?, ?, ?)",
                            (radio, area, circunferencia, diametro))
            conn.commit()
            conn.close()

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese un número válido y mayor que cero.")

    def mostrar_historial(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT radio, area, circunferencia, diametro FROM circulos ORDER BY id DESC LIMIT 5")
        datos = cursor.fetchall()
        conn.close()

        if not datos:
            self.resultados.setText("No hay registros en el historial.")
        else:
            historial_texto = "Últimos cálculos:\n"
            for radio, area, circunferencia, diametro in datos:
                historial_texto += (f"Radio: {radio}, Área: {round(area, 2)}, "
                                    f"Circunferencia: {round(circunferencia, 2)}, "
                                    f"Diámetro: {round(diametro, 2)}\n")
            self.resultados.setText(historial_texto)

    def graficar_circulo(self):
        try:
            radio = float(self.input_radio.text())
            if radio <= 0:
                raise ValueError("El radio debe ser mayor que cero.")

            # Crear figura con Matplotlib
            fig, ax = plt.subplots()
            theta = np.linspace(0, 2 * np.pi, 300)
            x = radio * np.cos(theta)
            y = radio * np.sin(theta)

            ax.plot(x, y, label=f"Círculo de radio {radio}")
            ax.set_aspect(1)
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.legend()
            plt.title("Representación Gráfica del Círculo")
            plt.grid()
            plt.show()

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese un número válido y mayor que cero.")

if __name__ == "__main__":
    inicializar_db()
    app = QApplication(sys.argv)
    ventana = CalculadoraCirculo()
    ventana.show()
    sys.exit(app.exec())
