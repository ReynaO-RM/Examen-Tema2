from tkinter import ttk

class StyleManager:
    def __init__(self, root):
        self.root = root
        self.configure_styles()

    def configure_styles(self):
        # Configurar estilos de la ventana
        self.root.configure(bg='#f0f0f0')  # Color de fondo

        # Configurar estilos de la tabla
        style = ttk.Style()
        style.theme_use("alt")

        # Estilo para la tabla
        style.configure("Treeview",
                        background="#ffffff",
                        foreground="#000000",
                        rowheight=25,
                        fieldbackground="#ffffff")
        style.configure("Treeview.Heading",
                        background="#e1e1e1",
                        foreground="#000000",
                        font=('Times New Roman', 12, 'bold'))

    def get_button_style(self):
        # Definir estilo para los botones
        return {
            'bg': '#6495ed',  # Color de fondo
            'fg': '#050001',  # Color del texto
            'font': ('Times New Roman', 12, 'italic')
        }