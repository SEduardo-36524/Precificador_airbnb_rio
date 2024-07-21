# Importação de bibliotecas
import customtkinter


# Classe dos menus de opções
class OptionMenuFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values, choice, width):
        super().__init__(master)

        # Atributos
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.choice = choice
        self.width = width
        
        # Menu suspenso
        self.variable = customtkinter.StringVar(value="")
        self.optionmenu = customtkinter.CTkComboBox(self, 
                                                      values=values, 
                                                      command=self.get_value, 
                                                      variable=self.variable,
                                                      button_color="#1F6AA5",
                                                      dropdown_fg_color="gray30",
                                                      dropdown_hover_color="gray40",
                                                      width=self.width + 20,
                                                      justify="center")
        self.optionmenu.grid(row=1, column=0, padx=0, pady=(10, 0))

        # Titulo
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, width=self.width)
        self.title.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="ew")

    # Função de escolha da opção
    def get_value(self):
        try:
            if self.optionmenu.get() in self.values:
                return self.optionmenu.get()
        except:
            return self.choice