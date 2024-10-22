import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Gráficas")
        self.root.geometry("800x600")

        # Crear el marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el área de botones y el área de gráficos
        self.create_widgets()

    def create_widgets(self):
        # Frame para los botones
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Botones para los diferentes tipos de gráficos
        self.hist_button = ttk.Button(self.button_frame, text="Histograma", command=self.show_histogram)
        self.hist_button.pack(pady=10)

        self.bar_button = ttk.Button(self.button_frame, text="Gráfico de Barras", command=self.show_bar_chart)
        self.bar_button.pack(pady=10)

        self.pie_button = ttk.Button(self.button_frame, text="Gráfico de Pastel", command=self.show_pie_chart)
        self.pie_button.pack(pady=10)

        # Botón para el diagrama de dispersión
        self.scatter_button = ttk.Button(self.button_frame, text="Diagrama de Dispersión", command=self.show_scatter_plot)
        self.scatter_button.pack(pady=10)

        # Botón para el diagrama de Pareto
        self.pareto_button = ttk.Button(self.button_frame, text="Diagrama de Pareto", command=self.show_pareto_chart)
        self.pareto_button.pack(pady=10)

        # Botón para el gráfico de control
        self.control_button = ttk.Button(self.button_frame, text="Gráfico de Control", command=self.show_control_chart)
        self.control_button.pack(pady=10)

        # Botones sin funcionalidad por ahora
        self.verificacion_button = ttk.Button(self.button_frame, text="Hoja de Verificación")
        self.verificacion_button.pack(pady=10)

        self.ishikawa_button = ttk.Button(self.button_frame, text="Diagrama de Ishikawa")
        self.ishikawa_button.pack(pady=10)

        # Frame para el gráfico
        self.plot_frame = ttk.Frame(self.main_frame)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Inicializar la figura y el lienzo como None
        self.fig = None
        self.canvas = None

    def clear_canvas(self):
        # Si ya existe un lienzo, eliminarlo
        if self.canvas is not None:
            self.canvas.get_tk_widget().pack_forget()
            self.canvas = None
            self.fig = None

    def show_histogram(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura y ejes
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        data = np.random.randn(1000)

        # Crear el histograma
        ax.hist(data, bins=20, edgecolor='black')
        ax.set_title("Histograma")
        ax.set_xlabel("Valores")
        ax.set_ylabel("Frecuencia")

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def show_bar_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura y ejes
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        categories = ['A', 'B', 'C', 'D']
        values = np.random.randint(10, 100, size=4)

        # Crear el gráfico de barras
        ax.bar(categories, values, color='skyblue')
        ax.set_title("Gráfico de Barras")
        ax.set_xlabel("Categorías")
        ax.set_ylabel("Valores")

        # Añadir etiquetas encima de cada barra
        for i, v in enumerate(values):
            ax.text(i, v + 1, str(v), ha='center')

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def show_pie_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura y ejes
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        labels = ['A', 'B', 'C', 'D']
        sizes = np.random.randint(10, 100, size=4)

        # Crear el gráfico de pastel
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Para asegurar que el gráfico sea circular
        ax.set_title("Gráfico de Pastel")

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def show_scatter_plot(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura y ejes
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        x = np.random.rand(100)
        y = np.random.rand(100)

        # Crear el diagrama de dispersión
        ax.scatter(x, y, color='green', alpha=0.5)

        # Calcular la línea de tendencia
        m, b = np.polyfit(x, y, 1)  # Ajuste lineal

        # Dibujar la línea de tendencia
        ax.plot(x, m*x + b, color='red', label="Línea de tendencia")

        ax.set_title("Diagrama de Dispersión")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")
        ax.legend()

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def show_pareto_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        categories = ['A', 'B', 'C', 'D', 'E', 'F']
        values = np.random.randint(20, 100, size=6)

        # Ordenar los valores de mayor a menor
        sorted_indices = np.argsort(values)[::-1]
        sorted_values = values[sorted_indices]
        sorted_categories = [categories[i] for i in sorted_indices]

        # Calcular la frecuencia acumulativa
        cumulative = np.cumsum(sorted_values)
        cumulative_percentage = cumulative / cumulative[-1] * 100

        # Crear el gráfico de barras (diagrama de Pareto)
        ax.bar(sorted_categories, sorted_values, color='skyblue')

        # Crear el eje secundario para la línea acumulativa
        ax2 = ax.twinx()
        ax2.plot(sorted_categories, cumulative_percentage, color='red', marker="D", label="Cumulativo")
        ax2.yaxis.set_ticks_position('right')
        ax2.yaxis.set_label_position('right')
        ax2.set_ylim(0, 110)

        # Configuración del gráfico
        ax.set_title("Diagrama de Pareto")
        ax.set_xlabel("Categorías")
        ax.set_ylabel("Frecuencia")
        ax2.set_ylabel("Porcentaje Acumulativo")

        # Añadir leyendas
        ax.legend(['Frecuencia'], loc='upper left')
        ax2.legend(['Cumulativo'], loc='upper right')

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

    def show_control_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Crear una nueva figura
        self.fig = plt.Figure(figsize=(5, 4))
        ax = self.fig.add_subplot(111)

        # Generar datos aleatorios
        data = np.random.randn(30) * 10 + 50  # Datos aleatorios alrededor de 50

        # Calcular estadísticas
        mean = np.mean(data)
        std = np.std(data)
        ucl = mean + 3 * std  # Límite de control superior
        lcl = mean - 3 * std  # Límite de control inferior

        # Crear el gráfico de control
        ax.plot(data, marker='o', linestyle='-', color='blue', label='Datos')
        ax.axhline(mean, color='green', linestyle='--', label='Media')  # Línea central
        ax.axhline(ucl, color='red', linestyle='--', label='Límite superior (UCL)')  # Límite superior
        ax.axhline(lcl, color='red', linestyle='--', label='Límite inferior (LCL)')  # Límite inferior

        # Configuración del gráfico
        ax.set_title("Gráfico de Control")
        ax.set_xlabel("Índice")
        ax.set_ylabel("Valor")
        ax.legend()

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
