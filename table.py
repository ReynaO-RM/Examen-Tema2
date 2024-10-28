import tkinter as tk
from tkinter import ttk

class Tables:
    def __init__(self, parent_frame, data_manager):
        self.parent_frame = parent_frame
        self.data_manager = data_manager
        self.table = None
        self.scrollbar_vertical = None
        self.scrollbar_horizontal = None
        self.data = []

    def create_table(self):
        # Limpiar el marco de la tabla si es necesario
        for widget in self.parent_frame.winfo_children():
            widget.destroy()

        # Frame para la tabla y los scrollbars
        table_container = tk.Frame(self.parent_frame)
        table_container.pack(fill='both', expand=True)

        # Scrollbar vertical
        self.scrollbar_vertical = tk.Scrollbar(table_container, orient='vertical')
        self.scrollbar_vertical.pack(side='right', fill='y')

        # Scrollbar horizontal
        self.scrollbar_horizontal = tk.Scrollbar(table_container, orient='horizontal')
        self.scrollbar_horizontal.pack(side='bottom', fill='x')

        # Crear tabla con Treeview
        self.table = ttk.Treeview(table_container, yscrollcommand=self.scrollbar_vertical.set,
                                   xscrollcommand=self.scrollbar_horizontal.set)
        self.table.pack(fill='both', expand=True)

        # Configurar scrollbars
        self.scrollbar_vertical.config(command=self.table.yview)
        self.scrollbar_horizontal.config(command=self.table.xview)

        # Definir columnas de la tabla
        self.table["columns"] = ("ID", "Título", "Autor", "Mes de Publicación", "Editorial", "Precio", "ISBN", "Ejemplares")
        self.table.column("#0", width=0, stretch=tk.NO)  # Ocultar la primera columna por defecto
        self.table.column("ID", anchor=tk.CENTER, width=50)
        self.table.column("Título", anchor=tk.W, width=200)
        self.table.column("Autor", anchor=tk.W, width=150)
        self.table.column("Mes de Publicación", anchor=tk.CENTER, width=120)
        self.table.column("Editorial", anchor=tk.W, width=150)
        self.table.column("Precio", anchor=tk.CENTER, width=80)
        self.table.column("ISBN", anchor=tk.CENTER, width=150)
        self.table.column("Ejemplares", anchor=tk.CENTER, width=150)

        # Encabezados de la tabla
        self.table.heading("#0", text="", anchor=tk.CENTER)
        self.table.heading("ID", text="ID", anchor=tk.CENTER)
        self.table.heading("Título", text="Título", anchor=tk.W)
        self.table.heading("Autor", text="Autor", anchor=tk.W)
        self.table.heading("Mes de Publicación", text="Mes de Publicación", anchor=tk.CENTER)
        self.table.heading("Editorial", text="Editorial", anchor=tk.W)
        self.table.heading("Precio", text="Precio", anchor=tk.CENTER)
        self.table.heading("ISBN", text="ISBN", anchor=tk.CENTER)
        self.table.heading("Ejemplares", text="Ejemplares", anchor=tk.CENTER)

    def insert_data(self, data):
        # Limpiar la tabla antes de insertar datos
        for item in self.table.get_children():
            self.table.delete(item)

        for record in data:
            self.table.insert(
                "", "end",
                values=(
                    record.get('id', 'N/A'),
                    record.get('Titulo', 'N/A'),
                    record.get('Autor', 'N/A'),
                    record.get('Mes_publicacion', 'N/A'),
                    record.get('Editorial', 'N/A'),
                    record.get('Precio', 'N/A'),
                    record.get('ISBN', 'N/A'),
                    record.get('Ejemplares', 'N/A')
                )
            )
    def set_data(self):
        self.data = self.data_manager.get_all_data()
