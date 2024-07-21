# Importação de bibliotecas
import customtkinter


# Classe do spinbox
class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, 
                 master, 
                 title,
                 *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: int | float = 1,
                 command: callable = None,
                 **kwargs):
        super().__init__(master, *args, width=width, height=height, **kwargs)

        # Atributos
        self.step_size = step_size
        self.command = command
        self.title = title

        # Cor do frame
        # self.configure(fg_color=("gray78", "gray28"))

        # Configura os botões para não expandir
        self.grid_columnconfigure((0, 2), weight=0)

        # Configura a entrada de dados para expandir
        self.grid_columnconfigure(1, weight=1)

        # Configura o botão de subtração de valor
        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, command=self.subtract_button_callback)
        self.subtract_button.grid(row=1, column=0, padx=(3, 0), pady=10)

        # Configura a caixa de valor
        self.entry = customtkinter.CTkEntry(self, width=width-(2*height))
        self.entry.grid(row=1, column=1, padx=3, pady=10, sticky="ew")

        # Configura o botão de adição de valor
        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, command=self.add_button_callback)
        self.add_button.grid(row=1, column=2, padx=(0, 3), pady=10)

        # Titulo
        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6, width=width)
        self.title.grid(row=0, column=0, padx=0, pady=0, sticky="ew", columnspan=3)

        # Valor padrão
        self.entry.insert(0, "0.00")

    # Função do botão adicionar valor
    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    # função do botão subtrair valor
    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    # Função para obter o valor no campo
    def get_value(self) -> float | None:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    # Função para inserir valor no campo
    def set_value(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))