import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Gráficas")
        self.root.geometry("900x600")  # Ajustar el tamaño si es necesario

        # Crear el marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Variables para almacenar el estado del frame de entrada
        self.input_frame_visible = False

        # Crear el área de botones y el área de gráficos
        self.create_widgets()

    def create_widgets(self):
        # Frame para los botones y entradas
        self.left_frame = ttk.Frame(self.main_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Frame para los botones
        self.button_frame = ttk.Frame(self.left_frame)
        self.button_frame.pack(fill=tk.Y, padx=10, pady=10)

        # Botones para los diferentes tipos de gráficos
        self.hist_button = ttk.Button(self.button_frame, text="Histograma", command=self.show_histogram_inputs)
        self.hist_button.pack(pady=5)

        self.bar_button = ttk.Button(self.button_frame, text="Gráfico de Barras", command=self.show_bar_chart)
        self.bar_button.pack(pady=5)

        self.pie_button = ttk.Button(self.button_frame, text="Gráfico de Pastel", command=self.show_pie_chart)
        self.pie_button.pack(pady=5)

        # Botón para el diagrama de dispersión
        self.scatter_button = ttk.Button(self.button_frame, text="Diagrama de Dispersión", command=self.show_scatter_plot)
        self.scatter_button.pack(pady=5)

        # Botón para el diagrama de Pareto
        self.pareto_button = ttk.Button(self.button_frame, text="Diagrama de Pareto", command=self.show_pareto_chart)
        self.pareto_button.pack(pady=5)

        # Botón para el gráfico de control
        self.control_button = ttk.Button(self.button_frame, text="Gráfico de Control", command=self.show_control_chart)
        self.control_button.pack(pady=5)

        # Botones sin funcionalidad por ahora
        self.verificacion_button = ttk.Button(self.button_frame, text="Hoja de Verificación")
        self.verificacion_button.pack(pady=5)

        self.ishikawa_button = ttk.Button(self.button_frame, text="Diagrama de Ishikawa")
        self.ishikawa_button.pack(pady=5)

        # Frame para las entradas del histograma (inicialmente oculto)
        self.input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Histograma")
        # No lo empaquetamos aquí para que esté oculto al inicio

        # Campos de entrada para el histograma
        self.data_entry = ttk.Entry(self.input_frame, width=30)
        self.title_entry = ttk.Entry(self.input_frame, width=30)
        self.x_label_entry = ttk.Entry(self.input_frame, width=30)
        self.y_label_entry = ttk.Entry(self.input_frame, width=30)
        self.bins_entry = ttk.Entry(self.input_frame, width=30)

        # Botón para generar el histograma
        self.generate_hist_button = ttk.Button(self.input_frame, text="Generar Histograma", command=self.show_histogram)

        # Colocar los widgets en el input_frame
        self.setup_histogram_inputs()

        # Frame para el gráfico
        self.plot_frame = ttk.Frame(self.main_frame)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Inicializar la figura y el lienzo como None
        self.fig = None
        self.canvas = None

    def setup_histogram_inputs(self):
        # Etiquetas y campos de entrada
        ttk.Label(self.input_frame, text="Datos (separados por comas):").pack(anchor='w', pady=2)
        self.data_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Título del Histograma:").pack(anchor='w', pady=2)
        self.title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.y_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Número de Bins:").pack(anchor='w', pady=2)
        self.bins_entry.pack(fill=tk.X, pady=2)

        self.generate_hist_button.pack(pady=10)

    def clear_canvas(self):
        # Si ya existe un lienzo, eliminarlo
        if self.canvas is not None:
            self.canvas.get_tk_widget().pack_forget()
            self.canvas = None
            self.fig = None

    def show_histogram_inputs(self):
        # Mostrar u ocultar el frame de entrada del histograma
        if not self.input_frame_visible:
            self.input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.input_frame_visible = True
        else:
            self.input_frame.pack_forget()
            self.input_frame_visible = False

    def show_histogram(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        data_str = self.data_entry.get()
        title = self.title_entry.get() or "Histograma"
        x_label = self.x_label_entry.get() or "Valores"
        y_label = self.y_label_entry.get() or "Frecuencia"
        bins_str = self.bins_entry.get()

        if not data_str:
            messagebox.showinfo("Información", "Por favor, ingrese los datos para el histograma.")
            return

        # Procesar el número de bins
        if bins_str:
            try:
                bins = int(bins_str)
                if bins <= 0:
                    messagebox.showwarning("Advertencia", "El número de bins debe ser un entero positivo. Se usará el valor por defecto (10).")
                    bins = 10
            except ValueError:
                messagebox.showwarning("Advertencia", "Entrada no válida para el número de bins. Se usará el valor por defecto (10).")
                bins = 10
        else:
            bins = 10  # Valor por defecto

        try:
            # Convertir la cadena de entrada en una lista de números
            data = [float(x.strip()) for x in data_str.split(',')]

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el histograma
            ax.hist(data, bins=bins, edgecolor='black')
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)

            # Ajustar el layout
            self.fig.tight_layout()

            # Crear el nuevo lienzo y mostrarlo
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una lista válida de números separados por comas.")

    def show_bar_chart(self):
        if self.input_frame_visible:
            self.input_frame.pack_forget()
            self.input_frame_visible = False
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
        if self.input_frame_visible:
            self.input_frame.pack_forget()
            self.input_frame_visible = False
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
        if self.input_frame_visible:
            self.input_frame.pack_forget()
            self.input_frame_visible = False
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
        if self.input_frame_visible:
            self.input_frame.pack_forget()
            self.input_frame_visible = False
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
        if self.input_frame_visible:
            self.input_frame.pack_forget()
            self.input_frame_visible = False
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
