# Importação de bibliotecas
import customtkinter


# Classe de RadioButtons
class RadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values, width):
        super().__init__(master)

        # Atributos
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.width = width
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        # Titulo
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, width=self.width)
        self.title.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="ew")

        # Cria um botão para cada valor de "self.values"
        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, 
                                                       text=value, 
                                                       value=value, 
                                                       variable=self.variable,
                                                       width=self.width,
                                                       command=self.get_value)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    # Obtém o valor do botão
    def get_value(self):
        return self.variable.get()
    
    # Seta um valor para o botão
    def set(self, value):
        self.variable.set(value)