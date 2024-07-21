# Importação de bibliotecas
import customtkinter


# Classe de caixa de valores
class Entry(customtkinter.CTkFrame):
    def __init__(self, master, title, width):
        super().__init__(master)

        # Atributos
        self.grid_columnconfigure(0, weight=1)
        #self.placeholder = placeholder
        self.title = title
        self.width = width
        self.variable = customtkinter.StringVar(value="")

        # Entry
        self.entry = customtkinter.CTkEntry(self, textvariable=self.variable, width=self.width)
        self.entry.grid(row=1, column=0, padx=0, pady=(5, 5), sticky="ew")

        # Titulo
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, width=self.width)
        self.title.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="ew")

    # Obtém o valor do botão
    def get_value(self):
        return self.variable.get()