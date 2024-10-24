import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Gráficas")
        self.root.geometry("900x900")  # Ajustar el tamaño si es necesario

        # Crear el marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Variables para almacenar el estado de los frames de entrada
        self.hist_input_frame_visible = False
        self.bar_input_frame_visible = False
        self.pie_input_frame_visible = False
        self.scatter_input_frame_visible = False
        self.pareto_input_frame_visible = False
        self.control_input_frame_visible = False
        self.ishikawa_frame_visible = False
        self.verification_frame_visible = False
        self.bar_csv_categories = None
        self.bar_csv_values = None
        self.pie_csv_labels = None
        self.pie_csv_values = None
        self.scatter_csv_x_values = None
        self.scatter_csv_y_values = None
        self.pareto_csv_categories = None
        self.pareto_csv_values = None
        self.control_csv_data = None

        # Crear el área de botones y el área de gráficos
        self.create_widgets()


#Crear los widgets y botones
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

        self.bar_button = ttk.Button(self.button_frame, text="Gráfico de Barras", command=self.show_bar_chart_inputs)
        self.bar_button.pack(pady=5)

        self.pie_button = ttk.Button(self.button_frame, text="Gráfico de Pastel", command=self.show_pie_chart_inputs)

        self.pie_button.pack(pady=5)

        # Botón para el diagrama de dispersión
        self.scatter_button = ttk.Button(self.button_frame, text="Diagrama de Dispersión", command=self.show_scatter_plot_inputs)
        self.scatter_button.pack(pady=5)

        # Botón para el diagrama de Pareto
        self.pareto_button = ttk.Button(self.button_frame, text="Diagrama de Pareto", command=self.show_pareto_chart_inputs)
        self.pareto_button.pack(pady=5)


        # Botón para el gráfico de control
        self.control_button = ttk.Button(self.button_frame, text="Gráfico de Control", command=self.show_control_chart_inputs)
        self.control_button.pack(pady=5)


        # Botones sin funcionalidad por ahora
        self.verificacion_button = ttk.Button(self.button_frame, text="Hoja de Verificación", command=self.show_verification_sheet_inputs)
        self.verificacion_button.pack(pady=5)

        # Botón para el Diagrama de Ishikawa
        self.ishikawa_button = ttk.Button(self.button_frame, text="Diagrama de Ishikawa", command=self.show_ishikawa_inputs)

        self.ishikawa_button.pack(pady=5)

        # Frame para las entradas del histograma (inicialmente oculto)
        self.input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Histograma")
        self.pie_input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Gráfico de Pastel")

        # Frame para las entradas del diagrama de dispersión (inicialmente oculto)
        self.scatter_input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Diagrama de Dispersión")

        # Frame para las entradas del diagrama de Pareto (inicialmente oculto)
        self.pareto_input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Diagrama de Pareto")

        # Frame para las entradas del gráfico de control (inicialmente oculto)
        self.control_input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Gráfico de Control")


        # Frame para las entradas del diagrama de Ishikawa (inicialmente oculto)
        self.ishikawa_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Diagrama de Ishikawa")

        # Añadir en create_widgets
        self.verification_frame = ttk.LabelFrame(self.left_frame, text="Parámetros de la Hoja de Verificación")
        # Añadir al final de create_widgets
        self.setup_verification_sheet_inputs()

        # Frame para el gráfico
        self.plot_frame = ttk.Frame(self.main_frame)
        self.plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Inicializar la figura y el lienzo como None
        self.fig = None
        self.canvas = None

        # Frame para las entradas del gráfico de barras (inicialmente oculto)
        self.bar_input_frame = ttk.LabelFrame(self.left_frame, text="Parámetros del Gráfico de Barras")

        # Configurar los campos de entrada
        self.setup_histogram_inputs()
        self.setup_ishikawa_inputs()
        self.setup_bar_chart_inputs()
        self.setup_pie_chart_inputs()
        self.setup_scatter_plot_inputs()
        self.setup_pareto_chart_inputs()
        self.setup_control_chart_inputs()


# Esconder los inputs
    def hide_all_input_frames(self):
        if self.hist_input_frame_visible:
            self.input_frame.pack_forget()
            self.hist_input_frame_visible = False
        if self.bar_input_frame_visible:
            self.bar_input_frame.pack_forget()
            self.bar_input_frame_visible = False
        if self.pie_input_frame_visible:
            self.pie_input_frame.pack_forget()
            self.pie_input_frame_visible = False
        if self.scatter_input_frame_visible:
            self.scatter_input_frame.pack_forget()
            self.scatter_input_frame_visible = False
        if self.pareto_input_frame_visible:
            self.pareto_input_frame.pack_forget()
            self.pareto_input_frame_visible = False
        if self.control_input_frame_visible:
            self.control_input_frame.pack_forget()
            self.control_input_frame_visible = False
        if self.ishikawa_frame_visible:
            self.ishikawa_frame.pack_forget()
            self.ishikawa_frame_visible = False
        if self.verification_frame_visible:
            self.verification_frame.pack_forget()
            self.verification_frame_visible = False


# Limpiar los inputs
    def clear_canvas(self):
        # Si ya existe un lienzo, eliminarlo
        if self.canvas is not None:
            self.canvas.get_tk_widget().pack_forget()
            self.canvas = None
            self.fig = None


# El setup de los inputs
    def setup_histogram_inputs(self):
        # Campos de entrada para el histograma

        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.hist_data_source = ttk.Combobox(self.input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.hist_data_source.current(0)  # Seleccionar "Entrada Manual" por defecto
        self.hist_data_source.pack(fill=tk.X, pady=2)
        self.hist_data_source.bind("<<ComboboxSelected>>", self.toggle_hist_data_entry)  # Vincular evento de selección

        # Campo de entrada de datos (solo si se selecciona "Entrada Manual")
        ttk.Label(self.input_frame, text="Datos (separados por comas):").pack(anchor='w', pady=2)
        self.data_entry = ttk.Entry(self.input_frame, width=30)
        self.data_entry.pack(fill=tk.X, pady=2)

        # Botón para cargar archivo CSV (solo si se selecciona "Archivo CSV")
        self.load_csv_button = ttk.Button(self.input_frame, text="Cargar Archivo CSV", command=self.load_hist_csv)
        # No lo empaquetamos aún; lo haremos en la función toggle_hist_data_entry

        # Etiquetas y campos de entrada para el título y etiquetas de los ejes
        ttk.Label(self.input_frame, text="Título del Histograma:").pack(anchor='w', pady=2)
        self.title_entry = ttk.Entry(self.input_frame, width=30)
        self.title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.x_label_entry = ttk.Entry(self.input_frame, width=30)
        self.x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.y_label_entry = ttk.Entry(self.input_frame, width=30)
        self.y_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.input_frame, text="Número de Bins:").pack(anchor='w', pady=2)
        self.bins_entry = ttk.Entry(self.input_frame, width=30)
        self.bins_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el histograma
        self.generate_hist_button = ttk.Button(self.input_frame, text="Generar Histograma", command=self.show_histogram)
        self.generate_hist_button.pack(pady=10)


    def setup_bar_chart_inputs(self):
        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.bar_input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.bar_data_source = ttk.Combobox(self.bar_input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.bar_data_source.current(0)  # Seleccionar "Entrada Manual" por defecto
        self.bar_data_source.pack(fill=tk.X, pady=2)
        self.bar_data_source.bind("<<ComboboxSelected>>", self.toggle_bar_data_entry)  # Vincular evento de selección

        # Campos de entrada para el gráfico de barras
        self.bar_categories_entry = ttk.Entry(self.bar_input_frame, width=30)
        self.bar_values_entry = ttk.Entry(self.bar_input_frame, width=30)

        # Botón para cargar archivo CSV
        self.bar_load_csv_button = ttk.Button(self.bar_input_frame, text="Cargar Archivo CSV", command=self.load_bar_csv)

        # Resto de los campos
        ttk.Label(self.bar_input_frame, text="Título del Gráfico de Barras:").pack(anchor='w', pady=2)
        self.bar_title_entry = ttk.Entry(self.bar_input_frame, width=30)
        self.bar_title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.bar_input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.bar_x_label_entry = ttk.Entry(self.bar_input_frame, width=30)
        self.bar_x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.bar_input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.bar_y_label_entry = ttk.Entry(self.bar_input_frame, width=30)
        self.bar_y_label_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el gráfico de barras
        self.generate_bar_chart_button = ttk.Button(self.bar_input_frame, text="Generar Gráfico de Barras", command=self.show_bar_chart)
        self.generate_bar_chart_button.pack(pady=10)

        # Inicialmente mostramos los campos de entrada manual
        ttk.Label(self.bar_input_frame, text="Categorías (separadas por comas):").pack(anchor='w', pady=2)
        self.bar_categories_entry.pack(fill=tk.X, pady=2)
        ttk.Label(self.bar_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
        self.bar_values_entry.pack(fill=tk.X, pady=2)


    def setup_pie_chart_inputs(self):
        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.pie_input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.pie_data_source = ttk.Combobox(self.pie_input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.pie_data_source.current(0)
        self.pie_data_source.pack(fill=tk.X, pady=2)
        self.pie_data_source.bind("<<ComboboxSelected>>", self.toggle_pie_data_entry)

        # Campos de entrada para el gráfico de pastel
        self.pie_labels_entry = ttk.Entry(self.pie_input_frame, width=30)
        self.pie_values_entry = ttk.Entry(self.pie_input_frame, width=30)

        # Botón para cargar archivo CSV
        self.pie_load_csv_button = ttk.Button(self.pie_input_frame, text="Cargar Archivo CSV", command=self.load_pie_csv)

        # Resto de los campos
        ttk.Label(self.pie_input_frame, text="Título del Gráfico de Pastel:").pack(anchor='w', pady=2)
        self.pie_title_entry = ttk.Entry(self.pie_input_frame, width=30)
        self.pie_title_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el gráfico de pastel
        self.generate_pie_chart_button = ttk.Button(self.pie_input_frame, text="Generar Gráfico de Pastel", command=self.show_pie_chart)
        self.generate_pie_chart_button.pack(pady=10)

        # Inicialmente mostramos los campos de entrada manual
        ttk.Label(self.pie_input_frame, text="Etiquetas (separadas por comas):").pack(anchor='w', pady=2)
        self.pie_labels_entry.pack(fill=tk.X, pady=2)
        ttk.Label(self.pie_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
        self.pie_values_entry.pack(fill=tk.X, pady=2)


    def setup_scatter_plot_inputs(self):
        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.scatter_input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.scatter_data_source = ttk.Combobox(self.scatter_input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.scatter_data_source.current(0)
        self.scatter_data_source.pack(fill=tk.X, pady=2)
        self.scatter_data_source.bind("<<ComboboxSelected>>", self.toggle_scatter_data_entry)

        # Campos de entrada para el diagrama de dispersión
        self.scatter_x_values_entry = ttk.Entry(self.scatter_input_frame, width=30)
        self.scatter_y_values_entry = ttk.Entry(self.scatter_input_frame, width=30)

        # Botón para cargar archivo CSV
        self.scatter_load_csv_button = ttk.Button(self.scatter_input_frame, text="Cargar Archivo CSV", command=self.load_scatter_csv)

        # Resto de los campos
        ttk.Label(self.scatter_input_frame, text="Título del Diagrama de Dispersión:").pack(anchor='w', pady=2)
        self.scatter_title_entry = ttk.Entry(self.scatter_input_frame, width=30)
        self.scatter_title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.scatter_input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.scatter_x_label_entry = ttk.Entry(self.scatter_input_frame, width=30)
        self.scatter_x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.scatter_input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.scatter_y_label_entry = ttk.Entry(self.scatter_input_frame, width=30)
        self.scatter_y_label_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el diagrama de dispersión
        self.generate_scatter_plot_button = ttk.Button(self.scatter_input_frame, text="Generar Diagrama de Dispersión", command=self.show_scatter_plot)
        self.generate_scatter_plot_button.pack(pady=10)

        # Inicialmente mostramos los campos de entrada manual
        ttk.Label(self.scatter_input_frame, text="Valores de X (separados por comas):").pack(anchor='w', pady=2)
        self.scatter_x_values_entry.pack(fill=tk.X, pady=2)
        ttk.Label(self.scatter_input_frame, text="Valores de Y (separados por comas):").pack(anchor='w', pady=2)
        self.scatter_y_values_entry.pack(fill=tk.X, pady=2)


    def setup_pareto_chart_inputs(self):
        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.pareto_input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.pareto_data_source = ttk.Combobox(self.pareto_input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.pareto_data_source.current(0)
        self.pareto_data_source.pack(fill=tk.X, pady=2)
        self.pareto_data_source.bind("<<ComboboxSelected>>", self.toggle_pareto_data_entry)

        # Campos de entrada para el diagrama de Pareto
        self.pareto_categories_entry = ttk.Entry(self.pareto_input_frame, width=30)
        self.pareto_values_entry = ttk.Entry(self.pareto_input_frame, width=30)

        # Botón para cargar archivo CSV
        self.pareto_load_csv_button = ttk.Button(self.pareto_input_frame, text="Cargar Archivo CSV", command=self.load_pareto_csv)

        # Resto de los campos
        ttk.Label(self.pareto_input_frame, text="Título del Diagrama de Pareto:").pack(anchor='w', pady=2)
        self.pareto_title_entry = ttk.Entry(self.pareto_input_frame, width=30)
        self.pareto_title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.pareto_input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.pareto_x_label_entry = ttk.Entry(self.pareto_input_frame, width=30)
        self.pareto_x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.pareto_input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.pareto_y_label_entry = ttk.Entry(self.pareto_input_frame, width=30)
        self.pareto_y_label_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el diagrama de Pareto
        self.generate_pareto_chart_button = ttk.Button(self.pareto_input_frame, text="Generar Diagrama de Pareto", command=self.show_pareto_chart)
        self.generate_pareto_chart_button.pack(pady=10)

        # Inicialmente mostramos los campos de entrada manual
        ttk.Label(self.pareto_input_frame, text="Categorías (separadas por comas):").pack(anchor='w', pady=2)
        self.pareto_categories_entry.pack(fill=tk.X, pady=2)
        ttk.Label(self.pareto_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
        self.pareto_values_entry.pack(fill=tk.X, pady=2)


    def setup_control_chart_inputs(self):
        # Añadir opción para seleccionar la fuente de datos
        ttk.Label(self.control_input_frame, text="Fuente de Datos:").pack(anchor='w', pady=2)
        self.control_data_source = ttk.Combobox(self.control_input_frame, values=["Entrada Manual", "Archivo CSV"], state="readonly")
        self.control_data_source.current(0)
        self.control_data_source.pack(fill=tk.X, pady=2)
        self.control_data_source.bind("<<ComboboxSelected>>", self.toggle_control_data_entry)

        # Campo de entrada para los datos
        self.control_data_entry = ttk.Entry(self.control_input_frame, width=30)

        # Botón para cargar archivo CSV
        self.control_load_csv_button = ttk.Button(self.control_input_frame, text="Cargar Archivo CSV", command=self.load_control_csv)

        # Resto de los campos
        ttk.Label(self.control_input_frame, text="Título del Gráfico de Control:").pack(anchor='w', pady=2)
        self.control_title_entry = ttk.Entry(self.control_input_frame, width=30)
        self.control_title_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.control_input_frame, text="Etiqueta del Eje X:").pack(anchor='w', pady=2)
        self.control_x_label_entry = ttk.Entry(self.control_input_frame, width=30)
        self.control_x_label_entry.pack(fill=tk.X, pady=2)

        ttk.Label(self.control_input_frame, text="Etiqueta del Eje Y:").pack(anchor='w', pady=2)
        self.control_y_label_entry = ttk.Entry(self.control_input_frame, width=30)
        self.control_y_label_entry.pack(fill=tk.X, pady=2)

        # Botón para generar el gráfico de control
        self.generate_control_chart_button = ttk.Button(self.control_input_frame, text="Generar Gráfico de Control", command=self.show_control_chart)
        self.generate_control_chart_button.pack(pady=10)

        # Inicialmente mostramos el campo de entrada manual
        ttk.Label(self.control_input_frame, text="Datos (separados por comas):").pack(anchor='w', pady=2)
        self.control_data_entry.pack(fill=tk.X, pady=2)


    def setup_verification_sheet_inputs(self):
        # Inicializar lista para almacenar los ítems
        self.verification_data = []

        # Botón para añadir nuevas columnas
        self.add_column_button = ttk.Button(self.verification_frame, text="Añadir Columna", command=self.add_check_column)
        self.add_column_button.pack(pady=5)
        
        # Etiqueta y campo para el título de la hoja
        ttk.Label(self.verification_frame, text="Título de la Hoja de Verificación:").pack(anchor='w', pady=2)
        self.verification_title_entry = ttk.Entry(self.verification_frame, width=30)
        self.verification_title_entry.pack(fill=tk.X, pady=2)

        # Botón para añadir nuevos ítems
        self.add_check_item_button = ttk.Button(self.verification_frame, text="Añadir Ítem", command=self.add_check_item)
        self.add_check_item_button.pack(pady=5)

        # Frame para los ítems
        self.check_items_frame = ttk.Frame(self.verification_frame)
        self.check_items_frame.pack(fill=tk.BOTH, expand=True)

        # Botón para generar la hoja de verificación
        self.generate_verification_button = ttk.Button(self.verification_frame, text="Generar Hoja de Verificación", command=self.show_verification_sheet)
        self.generate_verification_button.pack(pady=10)


    def setup_ishikawa_inputs(self):
        # Campos de entrada para el diagrama de Ishikawa
        self.problem_entry = ttk.Entry(self.ishikawa_frame, width=30)
        self.subcauses_entries = {}  # Diccionario para almacenar las entradas de subcausas por causa

        # Etiqueta y campo para el problema central
        ttk.Label(self.ishikawa_frame, text="Problema Central:").pack(anchor='w', pady=2)
        self.problem_entry.pack(fill=tk.X, pady=2)

        # Nombres de las causas principales predefinidas
        cause_names = ["Hombre", "Máquina", "Método", "Material", "Medida", "Entorno"]

        # Frame para las causas y subcausas
        self.causes_frame = ttk.Frame(self.ishikawa_frame)
        self.causes_frame.pack(fill=tk.BOTH, expand=True)

        for cause_name in cause_names:
            # Crear un frame para la causa y sus subcausas
            cause_frame = ttk.LabelFrame(self.causes_frame, text=cause_name)
            cause_frame.pack(fill=tk.X, pady=5)

            # Añadir el nombre de la causa principal (no editable)
            ttk.Label(cause_frame, text=cause_name).pack(side=tk.LEFT, padx=5, pady=5)

            # Botón para añadir subcausas
            add_subcause_button = ttk.Button(cause_frame, text="Añadir Subcausa", command=lambda cf=cause_frame, cn=cause_name: self.add_subcause_entry(cf, cn))
            add_subcause_button.pack(side=tk.LEFT, padx=5)

            # Frame para las subcausas de esta causa
            subcauses_frame = ttk.Frame(cause_frame)
            subcauses_frame.pack(fill=tk.X, padx=20)
            self.subcauses_entries[cause_name] = []

        # Botón para limpiar las entradas
        self.clear_ishikawa_button = ttk.Button(self.ishikawa_frame, text="Limpiar Todo", command=self.clear_ishikawa_inputs)
        self.clear_ishikawa_button.pack(pady=5)

        # Botón para generar el diagrama de Ishikawa
        self.generate_ishikawa_button = ttk.Button(self.ishikawa_frame, text="Generar Diagrama de Ishikawa", command=self.show_ishikawa)
        self.generate_ishikawa_button.pack(pady=10)


# Mostrar los inputs
    def show_histogram_inputs(self):
        self.hide_all_input_frames()
        if not self.hist_input_frame_visible:
            self.input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.hist_input_frame_visible = True
        else:
            self.input_frame.pack_forget()
            self.hist_input_frame_visible = False


    def show_bar_chart_inputs(self):
        self.hide_all_input_frames()
        if not self.bar_input_frame_visible:
            self.bar_input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.bar_input_frame_visible = True
        else:
            self.bar_input_frame.pack_forget()
            self.bar_input_frame_visible = False


    def show_pie_chart_inputs(self):
        self.hide_all_input_frames()
        if not self.pie_input_frame_visible:
            self.pie_input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.pie_input_frame_visible = True
        else:
            self.pie_input_frame.pack_forget()
            self.pie_input_frame_visible = False


    def show_scatter_plot_inputs(self):
        self.hide_all_input_frames()
        if not self.scatter_input_frame_visible:
            self.scatter_input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.scatter_input_frame_visible = True
        else:
            self.scatter_input_frame.pack_forget()
            self.scatter_input_frame_visible = False


    def show_pareto_chart_inputs(self):
        self.hide_all_input_frames()
        if not self.pareto_input_frame_visible:
            self.pareto_input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.pareto_input_frame_visible = True
        else:
            self.pareto_input_frame.pack_forget()
            self.pareto_input_frame_visible = False


    def show_control_chart_inputs(self):
        self.hide_all_input_frames()
        if not self.control_input_frame_visible:
            self.control_input_frame.pack(fill=tk.X, padx=10, pady=10)
            self.control_input_frame_visible = True
        else:
            self.control_input_frame.pack_forget()
            self.control_input_frame_visible = False


    def show_ishikawa_inputs(self):
        # Mostrar u ocultar el frame de entrada del diagrama de Ishikawa
        self.hide_all_input_frames()
        if not self.ishikawa_frame_visible:
            self.ishikawa_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
            self.ishikawa_frame_visible = True
        else:
            self.ishikawa_frame.pack_forget()
            self.ishikawa_frame_visible = False


    def show_verification_sheet_inputs(self):
        # Ocultar otros frames de entrada
        self.hide_all_input_frames()
        if not self.verification_frame_visible:
            self.verification_frame.pack(fill=tk.BOTH, padx=10, pady=10, expand=True)
            self.verification_frame_visible = True
        else:
            self.verification_frame.pack_forget()
            self.verification_frame_visible = False


# Mostrar las gráficas
    def show_histogram(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.title_entry.get() or "Histograma"
        x_label = self.x_label_entry.get() or "Valores"
        y_label = self.y_label_entry.get() or "Frecuencia"
        bins_str = self.bins_entry.get()

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

        # Obtener la fuente de datos seleccionada
        data_source = self.hist_data_source.get()

        try:
            if data_source == "Entrada Manual":
                data_str = self.data_entry.get()
                if not data_str:
                    messagebox.showinfo("Información", "Por favor, ingrese los datos para el histograma.")
                    return
                # Convertir la cadena de entrada en una lista de números
                data = [float(x.strip()) for x in data_str.split(',')]
            elif data_source == "Archivo CSV":
                if hasattr(self, 'hist_csv_data') and self.hist_csv_data:
                    data = self.hist_csv_data
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

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
            messagebox.showerror("Error", "Por favor, asegúrese de que los datos sean números válidos.")


    def show_bar_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.bar_title_entry.get() or "Gráfico de Barras"
        x_label = self.bar_x_label_entry.get() or "Categorías"
        y_label = self.bar_y_label_entry.get() or "Valores"

        data_source = self.bar_data_source.get()

        try:
            if data_source == "Entrada Manual":
                categories_str = self.bar_categories_entry.get()
                values_str = self.bar_values_entry.get()

                if not categories_str or not values_str:
                    messagebox.showinfo("Información", "Por favor, ingrese las categorías y los valores.")
                    return

                categories = [x.strip() for x in categories_str.split(',')]
                values = [float(x.strip()) for x in values_str.split(',')]

                if len(categories) != len(values):
                    raise ValueError("El número de categorías y valores no coincide.")

            elif data_source == "Archivo CSV":
                if hasattr(self, 'bar_csv_categories') and self.bar_csv_categories:
                    categories = self.bar_csv_categories
                    values = self.bar_csv_values
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el gráfico de barras
            ax.bar(categories, values, color='skyblue')
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)

            # Añadir etiquetas encima de cada barra
            for i, v in enumerate(values):
                ax.text(i, v + 0.5, str(v), ha='center')

            # Ajustar el layout
            self.fig.tight_layout()

            # Crear el nuevo lienzo y mostrarlo
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.canvas.draw()

        except ValueError as e:
            messagebox.showerror("Error", f"Error en los datos ingresados: {e}")


    def show_pie_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.pie_title_entry.get() or "Gráfico de Pastel"

        data_source = self.pie_data_source.get()

        try:
            if data_source == "Entrada Manual":
                labels_str = self.pie_labels_entry.get()
                values_str = self.pie_values_entry.get()

                if not labels_str or not values_str:
                    messagebox.showinfo("Información", "Por favor, ingrese las etiquetas y los valores.")
                    return

                labels = [x.strip() for x in labels_str.split(',')]
                values = [float(x.strip()) for x in values_str.split(',')]

                if len(labels) != len(values):
                    raise ValueError("El número de etiquetas y valores no coincide.")

            elif data_source == "Archivo CSV":
                if hasattr(self, 'pie_csv_labels') and self.pie_csv_labels:
                    labels = self.pie_csv_labels
                    values = self.pie_csv_values
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el gráfico de pastel
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Para asegurar que el gráfico sea circular
            ax.set_title(title)

            # Ajustar el layout
            self.fig.tight_layout()

            # Crear el nuevo lienzo y mostrarlo
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.canvas.draw()

        except ValueError as e:
            messagebox.showerror("Error", f"Error en los datos ingresados: {e}")


    def show_scatter_plot(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.scatter_title_entry.get() or "Diagrama de Dispersión"
        x_label = self.scatter_x_label_entry.get() or "Eje X"
        y_label = self.scatter_y_label_entry.get() or "Eje Y"

        data_source = self.scatter_data_source.get()

        try:
            if data_source == "Entrada Manual":
                x_values_str = self.scatter_x_values_entry.get()
                y_values_str = self.scatter_y_values_entry.get()

                if not x_values_str or not y_values_str:
                    messagebox.showinfo("Información", "Por favor, ingrese los valores de X y Y.")
                    return

                x_values = [float(x.strip()) for x in x_values_str.split(',')]
                y_values = [float(y.strip()) for y in y_values_str.split(',')]

                if len(x_values) != len(y_values):
                    raise ValueError("El número de valores de X y Y no coincide.")

            elif data_source == "Archivo CSV":
                if hasattr(self, 'scatter_csv_x_values') and self.scatter_csv_x_values:
                    x_values = self.scatter_csv_x_values
                    y_values = self.scatter_csv_y_values
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el diagrama de dispersión
            ax.scatter(x_values, y_values, color='green', alpha=0.5)

            # Calcular la línea de tendencia si hay suficientes datos
            if len(x_values) > 1:
                m, b = np.polyfit(x_values, y_values, 1)  # Ajuste lineal
                ax.plot(x_values, m*np.array(x_values) + b, color='red', label="Línea de tendencia")

            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.legend()

            # Ajustar el layout
            self.fig.tight_layout()

            # Crear el nuevo lienzo y mostrarlo
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.canvas.draw()

        except ValueError as e:
            messagebox.showerror("Error", f"Error en los datos ingresados: {e}")


    def show_pareto_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.pareto_title_entry.get() or "Diagrama de Pareto"
        x_label = self.pareto_x_label_entry.get() or "Categorías"
        y_label = self.pareto_y_label_entry.get() or "Frecuencia"

        data_source = self.pareto_data_source.get()

        try:
            if data_source == "Entrada Manual":
                categories_str = self.pareto_categories_entry.get()
                values_str = self.pareto_values_entry.get()

                if not categories_str or not values_str:
                    messagebox.showinfo("Información", "Por favor, ingrese las categorías y los valores.")
                    return

                categories = [x.strip() for x in categories_str.split(',')]
                values = [float(x.strip()) for x in values_str.split(',')]

                if len(categories) != len(values):
                    raise ValueError("El número de categorías y valores no coincide.")

            elif data_source == "Archivo CSV":
                if hasattr(self, 'pareto_csv_categories') and self.pareto_csv_categories:
                    categories = self.pareto_csv_categories
                    values = self.pareto_csv_values
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

            # Ordenar los valores de mayor a menor
            sorted_indices = np.argsort(values)[::-1]
            sorted_values = np.array(values)[sorted_indices]
            sorted_categories = [categories[i] for i in sorted_indices]

            # Calcular la frecuencia acumulativa
            cumulative = np.cumsum(sorted_values)
            cumulative_percentage = cumulative / cumulative[-1] * 100

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el gráfico de barras (diagrama de Pareto)
            ax.bar(sorted_categories, sorted_values, color='skyblue')

            # Crear el eje secundario para la línea acumulativa
            ax2 = ax.twinx()
            ax2.plot(sorted_categories, cumulative_percentage, color='red', marker="D", label="Cumulativo")
            ax2.yaxis.set_ticks_position('right')
            ax2.yaxis.set_label_position('right')
            ax2.set_ylim(0, 110)

            # Configuración del gráfico
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
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

        except ValueError as e:
            messagebox.showerror("Error", f"Error en los datos ingresados: {e}")


    def show_control_chart(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener los valores de los campos de entrada
        title = self.control_title_entry.get() or "Gráfico de Control"
        x_label = self.control_x_label_entry.get() or "Índice"
        y_label = self.control_y_label_entry.get() or "Valor"

        data_source = self.control_data_source.get()

        try:
            if data_source == "Entrada Manual":
                data_str = self.control_data_entry.get()
                if not data_str:
                    messagebox.showinfo("Información", "Por favor, ingrese los datos para el gráfico de control.")
                    return
                data = [float(x.strip()) for x in data_str.split(',')]
            elif data_source == "Archivo CSV":
                if hasattr(self, 'control_csv_data') and self.control_csv_data:
                    data = self.control_csv_data
                else:
                    messagebox.showinfo("Información", "No se han cargado datos desde el archivo CSV.")
                    return
            else:
                messagebox.showerror("Error", "Fuente de datos no reconocida.")
                return

            # Calcular estadísticas
            mean = np.mean(data)
            std = np.std(data)
            ucl = mean + 3 * std  # Límite de control superior
            lcl = mean - 3 * std  # Límite de control inferior

            # Crear una nueva figura y ejes
            self.fig = plt.Figure(figsize=(5, 4))
            ax = self.fig.add_subplot(111)

            # Crear el gráfico de control
            ax.plot(data, marker='o', linestyle='-', color='blue', label='Datos')
            ax.axhline(mean, color='green', linestyle='--', label='Media')  # Línea central
            ax.axhline(ucl, color='red', linestyle='--', label='Límite superior (UCL)')  # Límite superior
            ax.axhline(lcl, color='red', linestyle='--', label='Límite inferior (LCL)')  # Límite inferior

            # Configuración del gráfico
            ax.set_title(title)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.legend()

            # Ajustar el layout
            self.fig.tight_layout()

            # Crear el nuevo lienzo y mostrarlo
            self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            self.canvas.draw()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese una lista válida de números separados por comas.")


    def show_ishikawa(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener el problema central
        problem = self.problem_entry.get()
        if not problem:
            messagebox.showinfo("Información", "Por favor, ingrese el problema central.")
            return

        # Obtener las causas y subcausas
        causes = []
        for cause_name in self.subcauses_entries:
            subcauses_entries = self.subcauses_entries[cause_name]
            subcauses = [sc.get() for sc in subcauses_entries if sc.get()]
            causes.append({'cause': cause_name, 'subcauses': subcauses})

        # Crear una nueva figura
        self.fig = plt.Figure(figsize=(8, 6))
        ax = self.fig.add_subplot(111)

        # Dibujar el diagrama de Ishikawa
        self.draw_ishikawa(ax, problem, causes)

        # Ajustar el layout
        self.fig.tight_layout()

        # Crear el nuevo lienzo y mostrarlo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()


    def show_verification_sheet(self):
        # Limpiar el lienzo anterior
        self.clear_canvas()

        # Obtener el título
        title = self.verification_title_entry.get() or "Hoja de Verificación"

        # Recopilar los datos de los ítems
        items = []
        all_columns_data = []

        for item_frame, item_entry, count_entry, column_entries in self.verification_data:
            item = item_entry.get()

            # Obtener el valor del conteo inicial
            try:
                count = int(count_entry.get())
            except ValueError:
                count = 0

            if item:
                items.append(item)

                # Obtener los valores de las columnas adicionales
                row_data = [count]
                for col_entry in column_entries:
                    try:
                        col_value = int(col_entry.get())
                    except ValueError:
                        col_value = 0
                    row_data.append(col_value)
                all_columns_data.append(row_data)

        if not items:
            messagebox.showinfo("Información", "Por favor, añada al menos un ítem a la hoja de verificación.")
            return

        # Crear una nueva figura
        self.fig = plt.Figure(figsize=(6, 4))
        ax = self.fig.add_subplot(111)

        # Preparar los datos para la tabla
        table_data = []
        for i in range(len(items)):
            # Combinar ítem y valores de las columnas
            row = [items[i]] + all_columns_data[i]
            table_data.append(row)

        # Generar las etiquetas de las columnas dinámicamente
        num_columns = len(all_columns_data[0])  # Número de columnas (sin contar el ítem)
        col_labels = ["Ítem"] + [f"Columna {j+1}" for j in range(num_columns)]

        # Crear la tabla
        table = ax.table(cellText=table_data, colLabels=col_labels, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 2)

        # Ocultar los ejes
        ax.axis('off')
        ax.set_title(title, fontsize=12)

        # Ajustar el layout
        self.fig.tight_layout()

        # Mostrar la figura en el lienzo
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.draw()


    # Entradas adicionales
    def toggle_hist_data_entry(self, event):
        if self.hist_data_source.get() == "Entrada Manual":
            # Mostrar campo de entrada de datos y ocultar botón de cargar CSV
            self.data_entry.pack(fill=tk.X, pady=2)
            self.load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campo de entrada de datos
            self.data_entry.pack_forget()
            self.load_csv_button.pack(fill=tk.X, pady=2)


    def toggle_bar_data_entry(self, event):
        if self.bar_data_source.get() == "Entrada Manual":
            # Mostrar campos de entrada manual y ocultar botón de cargar CSV
            ttk.Label(self.bar_input_frame, text="Categorías (separadas por comas):").pack(anchor='w', pady=2)
            self.bar_categories_entry.pack(fill=tk.X, pady=2)
            ttk.Label(self.bar_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
            self.bar_values_entry.pack(fill=tk.X, pady=2)
            self.bar_load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campos de entrada manual
            self.bar_categories_entry.pack_forget()
            self.bar_values_entry.pack_forget()
            self.bar_load_csv_button.pack(fill=tk.X, pady=2)


    def toggle_pie_data_entry(self, event):
        if self.pie_data_source.get() == "Entrada Manual":
            # Mostrar campos de entrada manual y ocultar botón de cargar CSV
            ttk.Label(self.pie_input_frame, text="Etiquetas (separadas por comas):").pack(anchor='w', pady=2)
            self.pie_labels_entry.pack(fill=tk.X, pady=2)
            ttk.Label(self.pie_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
            self.pie_values_entry.pack(fill=tk.X, pady=2)
            self.pie_load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campos de entrada manual
            self.pie_labels_entry.pack_forget()
            self.pie_values_entry.pack_forget()
            self.pie_load_csv_button.pack(fill=tk.X, pady=2)


    def toggle_scatter_data_entry(self, event):
        if self.scatter_data_source.get() == "Entrada Manual":
            # Mostrar campos de entrada manual y ocultar botón de cargar CSV
            ttk.Label(self.scatter_input_frame, text="Valores de X (separados por comas):").pack(anchor='w', pady=2)
            self.scatter_x_values_entry.pack(fill=tk.X, pady=2)
            ttk.Label(self.scatter_input_frame, text="Valores de Y (separados por comas):").pack(anchor='w', pady=2)
            self.scatter_y_values_entry.pack(fill=tk.X, pady=2)
            self.scatter_load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campos de entrada manual
            self.scatter_x_values_entry.pack_forget()
            self.scatter_y_values_entry.pack_forget()
            self.scatter_load_csv_button.pack(fill=tk.X, pady=2)


    def toggle_pareto_data_entry(self, event):
        if self.pareto_data_source.get() == "Entrada Manual":
            # Mostrar campos de entrada manual y ocultar botón de cargar CSV
            ttk.Label(self.pareto_input_frame, text="Categorías (separadas por comas):").pack(anchor='w', pady=2)
            self.pareto_categories_entry.pack(fill=tk.X, pady=2)
            ttk.Label(self.pareto_input_frame, text="Valores (separados por comas):").pack(anchor='w', pady=2)
            self.pareto_values_entry.pack(fill=tk.X, pady=2)
            self.pareto_load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campos de entrada manual
            self.pareto_categories_entry.pack_forget()
            self.pareto_values_entry.pack_forget()
            self.pareto_load_csv_button.pack(fill=tk.X, pady=2)


    def toggle_control_data_entry(self, event):
        if self.control_data_source.get() == "Entrada Manual":
            # Mostrar campo de entrada manual y ocultar botón de cargar CSV
            ttk.Label(self.control_input_frame, text="Datos (separados por comas):").pack(anchor='w', pady=2)
            self.control_data_entry.pack(fill=tk.X, pady=2)
            self.control_load_csv_button.pack_forget()
        else:
            # Mostrar botón de cargar CSV y ocultar campo de entrada manual
            self.control_data_entry.pack_forget()
            self.control_load_csv_button.pack(fill=tk.X, pady=2)


    # Poner el csv
    def load_hist_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    data = []
                    for row in reader:
                        for value in row:
                            try:
                                data.append(float(value.strip()))
                            except ValueError:
                                continue  # Ignorar valores no numéricos

                if data:
                    self.hist_csv_data = data  # Guardar los datos para usarlos al generar el histograma
                    messagebox.showinfo("Información", f"Se cargaron {len(data)} datos desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos numéricos en el archivo CSV.")
                    self.hist_csv_data = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.hist_csv_data = None
        else:
            self.hist_csv_data = None


    def load_bar_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    categories = []
                    values = []
                    for row in reader:
                        if len(row) >= 2:
                            category = row[0].strip()
                            try:
                                value = float(row[1].strip())
                                categories.append(category)
                                values.append(value)
                            except ValueError:
                                continue  # Ignorar filas con valores no numéricos
                if categories and values:
                    self.bar_csv_categories = categories
                    self.bar_csv_values = values
                    messagebox.showinfo("Información", f"Se cargaron {len(categories)} categorías desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos válidos en el archivo CSV.")
                    self.bar_csv_categories = None
                    self.bar_csv_values = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.bar_csv_categories = None
                self.bar_csv_values = None
        else:
            self.bar_csv_categories = None
            self.bar_csv_values = None


    def load_pie_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    labels = []
                    values = []
                    for row in reader:
                        if len(row) >= 2:
                            label = row[0].strip()
                            try:
                                value = float(row[1].strip())
                                labels.append(label)
                                values.append(value)
                            except ValueError:
                                continue  # Ignorar filas con valores no numéricos
                if labels and values:
                    self.pie_csv_labels = labels
                    self.pie_csv_values = values
                    messagebox.showinfo("Información", f"Se cargaron {len(labels)} etiquetas desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos válidos en el archivo CSV.")
                    self.pie_csv_labels = None
                    self.pie_csv_values = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.pie_csv_labels = None
                self.pie_csv_values = None
        else:
            self.pie_csv_labels = None
            self.pie_csv_values = None


    def load_scatter_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                x_values = []
                y_values = []
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if len(row) >= 2:
                            try:
                                x = float(row[0].strip())
                                y = float(row[1].strip())
                                x_values.append(x)
                                y_values.append(y)
                            except ValueError:
                                continue  # Ignorar filas con valores no numéricos
                if x_values and y_values:
                    self.scatter_csv_x_values = x_values
                    self.scatter_csv_y_values = y_values
                    messagebox.showinfo("Información", f"Se cargaron {len(x_values)} puntos desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos válidos en el archivo CSV.")
                    self.scatter_csv_x_values = None
                    self.scatter_csv_y_values = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.scatter_csv_x_values = None
                self.scatter_csv_y_values = None
        else:
            self.scatter_csv_x_values = None
            self.scatter_csv_y_values = None


    def load_pareto_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                categories = []
                values = []
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        if len(row) >= 2:
                            category = row[0].strip()
                            try:
                                value = float(row[1].strip())
                                categories.append(category)
                                values.append(value)
                            except ValueError:
                                continue  # Ignorar filas con valores no numéricos
                if categories and values:
                    self.pareto_csv_categories = categories
                    self.pareto_csv_values = values
                    messagebox.showinfo("Información", f"Se cargaron {len(categories)} categorías desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos válidos en el archivo CSV.")
                    self.pareto_csv_categories = None
                    self.pareto_csv_values = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.pareto_csv_categories = None
                self.pareto_csv_values = None
        else:
            self.pareto_csv_categories = None
            self.pareto_csv_values = None


    def load_control_csv(self):
        # Abrir cuadro de diálogo para seleccionar el archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                # Leer los datos del archivo CSV
                import csv
                data = []
                with open(file_path, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        for value in row:
                            try:
                                data.append(float(value.strip()))
                            except ValueError:
                                continue  # Ignorar valores no numéricos
                if data:
                    self.control_csv_data = data
                    messagebox.showinfo("Información", f"Se cargaron {len(data)} datos desde el archivo CSV.")
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos numéricos en el archivo CSV.")
                    self.control_csv_data = None
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo leer el archivo CSV: {e}")
                self.control_csv_data = None
        else:
            self.control_csv_data = None


    #########

    def add_cause_entry(self):
        # Crear un nuevo frame para la causa y sus subcausas
        cause_frame = ttk.LabelFrame(self.causes_frame, text=f"Causa {len(self.causes_entries)+1}")
        cause_frame.pack(fill=tk.X, pady=5)

        # Campo de entrada para la causa principal
        cause_entry = ttk.Entry(cause_frame, width=25)
        cause_entry.pack(side=tk.LEFT, padx=5, pady=5)
        self.causes_entries.append(cause_entry)

        # Botón para eliminar la causa principal
        remove_cause_button = ttk.Button(cause_frame, text="Eliminar Causa", command=lambda: self.remove_cause_entry(cause_frame, cause_entry))
        remove_cause_button.pack(side=tk.LEFT, padx=5)

        # Botón para añadir subcausas
        add_subcause_button = ttk.Button(cause_frame, text="Añadir Subcausa", command=lambda: self.add_subcause_entry(cause_frame, cause_entry))
        add_subcause_button.pack(side=tk.LEFT, padx=5)

        # Frame para las subcausas de esta causa
        subcauses_frame = ttk.Frame(cause_frame)
        subcauses_frame.pack(fill=tk.X, padx=20)
        self.subcauses_entries[cause_entry] = []


    def add_subcause_entry(self, cause_frame, cause_name):
        # Frame para la subcausa
        subcause_frame = ttk.Frame(cause_frame)
        subcause_frame.pack(anchor='w', padx=25, pady=2)

        # Campo de entrada para la subcausa
        subcause_entry = ttk.Entry(subcause_frame, width=20)
        subcause_entry.pack(side=tk.LEFT)

        # Botón para eliminar la subcausa
        remove_subcause_button = ttk.Button(subcause_frame, text="Eliminar Subcausa", command=lambda: self.remove_subcause_entry(cause_name, subcause_frame, subcause_entry))
        remove_subcause_button.pack(side=tk.LEFT, padx=5)

        # Añadir el Entry de la subcausa a la lista correspondiente
        self.subcauses_entries[cause_name].append(subcause_entry)


    def remove_cause_entry(self, cause_frame, cause_entry):
        # Eliminar las subcausas asociadas
        del self.subcauses_entries[cause_entry]
        # Eliminar la causa de la lista
        self.causes_entries.remove(cause_entry)
        # Destruir el frame de la causa
        cause_frame.destroy()


    def remove_subcause_entry(self, cause_name, subcause_frame, subcause_entry):
        # Eliminar la subcausa de la lista correspondiente
        self.subcauses_entries[cause_name].remove(subcause_entry)
        # Destruir el frame de la subcausa
        subcause_frame.destroy()


    def clear_ishikawa_inputs(self):
        # Limpiar el campo del problema central
        self.problem_entry.delete(0, tk.END)
        # Eliminar subcausas de cada causa
        for cause_name in self.subcauses_entries:
            subcauses_list = self.subcauses_entries[cause_name]
            for subcause_entry in subcauses_list[:]:
                self.remove_subcause_entry(cause_name, subcause_entry.master, subcause_entry)
        # Reiniciar el diccionario de subcausas
        self.subcauses_entries = {cause_name: [] for cause_name in self.subcauses_entries}


    def draw_ishikawa(self, ax, problem, causes):
        # Configurar límites y ocultar ejes
        ax.axis('off')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        # Dibujar la línea principal (efecto/problema)
        ax.plot([2, 8], [5, 5], color='black', lw=2)

        # Añadir el problema al final de la línea principal
        ax.text(8.2, 5, problem, fontsize=14, va='center')

        # Definir posiciones x para las ramas principales
        x_positions_top = [8, 6, 4]  # Posiciones x para las ramas superiores
        x_positions_bottom = [8, 6, 4]  # Posiciones x para las ramas inferiores

        x_positions = x_positions_top + x_positions_bottom

        # Longitud de las ramas principales (ajustar para disminuir el ángulo)
        branch_length_x = 1.5  # Menor longitud en X para ramas más verticales
        branch_length_y = 3    # Mayor diferencia en Y para ramas más verticales

        for i, cause in enumerate(causes):
            if i < 3:
                # Ramas superiores
                y_start = 5
                y_end = y_start + branch_length_y  # Más vertical
                direction = 1  # Arriba
            else:
                # Ramas inferiores
                y_start = 5
                y_end = y_start - branch_length_y  # Más vertical
                direction = -1  # Abajo

            x_pos = x_positions[i]

            # Dibujar la línea de la causa principal (más vertical)
            ax.plot([x_pos, x_pos - branch_length_x], [y_start, y_end], color='black', lw=1.5)

            # Añadir el texto de la causa principal
            ax.text(x_pos - branch_length_x - 0.2, y_end, cause['cause'], fontsize=12, va='center', ha='right')

            # Dibujar subcausas
            num_subcauses = len(cause['subcauses'])
            if num_subcauses > 0:
                # Espaciado entre subcausas a lo largo de la rama principal
                spacing_y = branch_length_y / (num_subcauses + 1)
                for j, subcause in enumerate(cause['subcauses']):
                    # Posición en Y a lo largo de la rama principal
                    sub_y = y_start + direction * spacing_y * (j + 1)
                    # Posición en X correspondiente en la rama principal
                    sub_x = x_pos - (branch_length_x / branch_length_y) * abs(sub_y - y_start)

                    # **Aquí hacemos la línea de la subcausa más corta**
                    line_length = 0.5  # Longitud de la línea de la subcausa
                    text_offset = 0.6  # Desplazamiento del texto

                    # Dibujar línea horizontal de la subcausa (más corta)
                    ax.plot([sub_x, sub_x - line_length], [sub_y, sub_y], color='black', lw=1)

                    # Añadir el texto de la subcausa
                    ax.text(sub_x - line_length - text_offset, sub_y, subcause, fontsize=9, va='center', ha='right')


    def add_check_column(self):
        # Añadir una nueva columna para todos los ítems existentes
        for item_frame, item_entry, count_entry, column_entries in self.verification_data:
            # Crear un nuevo campo de entrada para la nueva columna
            new_column_entry = ttk.Entry(item_frame, width=5)
            new_column_entry.pack(side=tk.LEFT, padx=5)
            # Añadir este nuevo campo a la lista de columnas de ese ítem
            column_entries.append(new_column_entry)


    def add_check_item(self):
        # Frame para el ítem
        item_frame = ttk.Frame(self.check_items_frame)
        item_frame.pack(fill=tk.X, pady=2)

        # Campo de entrada para la descripción del ítem
        item_entry = ttk.Entry(item_frame, width=25)
        item_entry.pack(side=tk.LEFT, padx=5)

        # Campo de entrada para la primera columna (por defecto)
        count_entry = ttk.Entry(item_frame, width=5)
        count_entry.pack(side=tk.LEFT, padx=5)

        # Inicializar la lista de columnas adicionales para este ítem
        column_entries = []

        # Botón para eliminar el ítem
        remove_item_button = ttk.Button(item_frame, text="Eliminar Ítem", command=lambda: self.remove_check_item(item_frame, item_entry, count_entry, column_entries))
        remove_item_button.pack(side=tk.LEFT, padx=5)

        # Almacenar el item_frame y las entradas
        self.verification_data.append((item_frame, item_entry, count_entry, column_entries))


    def remove_check_item(self, item_frame, item_entry, count_entry, column_entries):
        # Eliminar el ítem de la lista
        self.verification_data.remove((item_frame, item_entry, count_entry, column_entries))
        # Destruir el frame del ítem
        item_frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
