# Importação de bibliotecas
import customtkinter
from SideBar import SideBar
from TabView import TabView
from DataCompatibility import DataCompatibility


# Classe Principal do Aplicativo
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Atributos diversos
        self.title("Precificador de imóveis AirBnB Rio")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.minsize(780, 540)
        self.maxsize(780, 540)
        self.data_compatibility = DataCompatibility
        self.text_prevision = "Nenhum imóvel precificado"

        # Insere a Barra Lateral
        self.side_bar = SideBar(self)
        self.side_bar.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), rowspan=7, sticky="ns")

        # Insere o TabView
        self.tab_view = TabView(self)
        self.tab_view.grid(row=0, column=1, padx=(0, 10), pady=20, sticky="ns")

        # Preço Sugerido
        self.price_sugestion_label = customtkinter.CTkLabel(self, text=self.text_prevision, fg_color="#1F6AA5", corner_radius=6, width=90)
        self.price_sugestion_label.grid(row=1, column=0, padx=(20, 20), pady=(0, 20), sticky="nsew", rowspan=2)

        # Insere o botão de previsão do preço
        self.button = customtkinter.CTkButton(self, text="Precificar o Imóvel", command=self.button_event, corner_radius=10)
        self.button.grid(row=2, column=1, padx=(10, 10), pady=(10, 20), sticky="ew")

        
    # Função do botão
    def button_event(self):

        # Adiciona o dataframe
        self.data_compatibility.create_dataframe(self)

        # Preço Sugerido
        self.text_prevision = f"Preço sugerido:\n\nR$ {self.data_compatibility.prevision(self)}"
        self.price_sugestion_label = customtkinter.CTkLabel(self, text=self.text_prevision, fg_color="#1F6AA5", corner_radius=6, width=90)
        self.price_sugestion_label.grid(row=1, column=0, padx=(20, 20), pady=(0, 20), sticky="nsew", rowspan=2)


