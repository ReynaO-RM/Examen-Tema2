import tkinter as tk
from tkinter import ttk
from logic import DataManager
from table import Tables
from style import StyleManager
import tkinter.messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Librería")
        self.root.geometry("1200x640")
        self.root.resizable(False, False)

        # Instancia de DataManager
        self.data_manager = DataManager()

        # Instancia de Tables
        self.table_handler = Tables(self.root, self.data_manager)

        # Instancia de StyleManager
        self.style_manager = StyleManager(self.root)

        # Crear el menú principal
        self.create_main_menu()

    def create_main_menu(self):
        # Limpiar la interfaz actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear un frame para centrar los botones
        frame = tk.Frame(self.root)
        frame.pack(expand=True, pady=20)

        # Creación de botones con estilos
        button_style = self.style_manager.get_button_style()

        show_all_button = tk.Button(
            frame,
            text="Mostrar Todos los Registros",
            command=self.show_all_records,
            bg=button_style['bg'],
            fg=button_style['fg'],
            font=button_style['font'],
            height=2,
            width=30
        )
        show_all_button.pack(pady=10)

        search_button = tk.Button(
            frame,
            text="Buscar Registro Específico",
            command=self.create_search_menu,
            bg=button_style['bg'],
            fg=button_style['fg'],
            font=button_style['font'],
            height=2,
            width=30
        )
        search_button.pack(pady=10)

    def create_search_menu(self):
        # Limpiar la interfaz actual
        for widget in self.root.winfo_children():
            widget.destroy()

        # Obtención de registros para el menú desplegable
        self.table_handler.set_data()
        self.ids = [record['id'] for record in self.table_handler.data]

        # Menú desplegable para seleccionar un registro
        self.selected_id = tk.StringVar()
        search_label = tk.Label(self.root, text="Selecciona un ID para buscar:")
        search_label.pack(pady=10)

        search_dropdown = ttk.Combobox(self.root, textvariable=self.selected_id, values=self.ids)
        search_dropdown.pack(pady=10)

        search_button = tk.Button(
            self.root,
            text="Buscar Registro",
            command=self.show_specific_record,
            bg=self.style_manager.get_button_style()['bg'],
            fg=self.style_manager.get_button_style()['fg'],
            font=self.style_manager.get_button_style()['font']
        )
        search_button.pack(pady=10)

        # Botón para regresar al menú principal
        back_button = tk.Button(
            self.root,
            text="Regresar al Menú Principal",
            command=self.create_main_menu,
            bg=self.style_manager.get_button_style()['bg'],
            fg=self.style_manager.get_button_style()['fg'],
            font=self.style_manager.get_button_style()['font']
        )
        back_button.pack(pady=10)

    def show_all_records(self):
        # Limpiar la tabla antes de mostrar los datos
        self.table_handler.create_table()
        self.table_handler.set_data()
        self.table_handler.insert_data(self.table_handler.data)

        # Botón para refrescar la tabla
        refresh_button = tk.Button(
            self.root,
            text="Refrescar",
            command=self.refresh_table,
            bg=self.style_manager.get_button_style()['bg'],
            fg=self.style_manager.get_button_style()['fg'],
            font=self.style_manager.get_button_style()['font']
        )
        refresh_button.pack(pady=10)

        # Botón para regresar al menú principal
        back_button = tk.Button(
            self.root,
            text="Regresar al Menú Principal",
            command=self.create_main_menu,
            bg=self.style_manager.get_button_style()['bg'],
            fg=self.style_manager.get_button_style()['fg'],
            font=self.style_manager.get_button_style()['font']
        )
        back_button.pack(pady=10)

    def refresh_table(self):
        # Refrescar los datos y la tabla
        self.table_handler.set_data()
        self.table_handler.insert_data(self.table_handler.data)

    def show_specific_record(self):
        selected_id = self.selected_id.get()

        # Verificar si se ha seleccionado un ID
        if not selected_id:
            # Mostrar un mensaje de advertencia
            tk.messagebox.showwarning("Selección requerida", "Por favor, selecciona un ID para buscar.")
            return

        # Limpiar la tabla antes de mostrar los datos
        self.table_handler.create_table()

        # Buscar el registro específico
        record = next((item for item in self.table_handler.data if item['id'] == selected_id), None)

        if record:
            # Insertar el registro encontrado en la tabla
            self.table_handler.insert_data([record])
        else:
            tk.messagebox.showerror("Registro no encontrado", "No se encontró el registro con el ID seleccionado.")

        # Botón para regresar al menú principal
        back_button = tk.Button(
            self.root,
            text="Regresar al Menú Principal",
            command=self.create_main_menu,
            bg=self.style_manager.get_button_style()['bg'],
            fg=self.style_manager.get_button_style()['fg'],
            font=self.style_manager.get_button_style()['font']
        )
        back_button.pack(pady=10)
