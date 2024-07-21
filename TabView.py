# Importação de bibliotecas
import customtkinter
from OptionMenuFrame import OptionMenuFrame
from RadioButtonFrame import RadioButtonFrame
from FloatSpinbox import FloatSpinbox
from Entry import Entry


# Cria páginas
class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # Cria os Tabs e seta o tab padrão
        self.add("Informações do Host")
        self.add("Informações do Imóvel")
        self.add("Data e local")
        self.set("Informações do Host")

        # Adiciona Widgets nos Tabs

        # Informações do Host
        # Superhost
        self.superhost = RadioButtonFrame(self.tab("Informações do Host"), "Superhost", values=["Sim", "Não"], width=180)
        self.superhost.grid(row=0, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

        # Reserva imediata
        self.instant_bookable = RadioButtonFrame(self.tab("Informações do Host"), "Reserva Imediata", values=["Sim", "Não"], width=180)
        self.instant_bookable.grid(row=0, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")
  
        # Política de Cancelamento
        self.cancellation_policy = RadioButtonFrame(self.tab("Informações do Host"), "Política de Cancelamento", values=["Flexível", "Moderada", "Estrita"], width=180)
        self.cancellation_policy.grid(row=1, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")
    
        # Número de casas do Host
        self.host_listings_count = RadioButtonFrame(self.tab("Informações do Host"), "Quantidade de casas", values=["1", "2", "3"], width=180)
        self.host_listings_count.grid(row=1, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")

        # Extra por Pessoa
        self.extra_people = FloatSpinbox(self.tab("Informações do Host"), title="Extra por pessoa em R$", width=180, step_size=0.01)
        self.extra_people.grid(row=2, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

        # Quantidade mínima de noites
        self.minimum_nights = OptionMenuFrame(self.tab("Informações do Host"), "Mínimo de noites", values=["1", "2", "3", "4", "5", "6", "7", "8"], choice="", width=180)
        self.minimum_nights.grid(row=2, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")

        # ----------------------------------------------------------------------------------------------------------------
        # Informações do Imóvel

        # Tipo de propriedade
        self.property_type = RadioButtonFrame(self.tab("Informações do Imóvel"), "Tipo de propriedade", values=["Apartamento", "Outros"], width=180)
        self.property_type.grid(row=0, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

	    # Tipo de Quarto
        self.room_type = RadioButtonFrame(self.tab("Informações do Imóvel"), "Tipo de Quarto", values=["Casa/Apartamento inteiro", "Outros"], width=180)
        self.room_type.grid(row=0, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")

	    # Quantas pessoas acomoda
        self.accommodates = OptionMenuFrame(self.tab("Informações do Imóvel"), "Quantas pessoas acomoda", values=["1", "2", "3", "4", "5", "6", "7", "8", "9"], choice="", width=180)
        self.accommodates.grid(row=1, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

	    # Numero de Banheiros 
        self.bathrooms = OptionMenuFrame(self.tab("Informações do Imóvel"), "Número de Banheiros", values=["1", "2", "3", "4"], choice="", width=180)
        self.bathrooms.grid(row=1, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")

	    # Número de Quartos
        self.bedrooms = OptionMenuFrame(self.tab("Informações do Imóvel"), "Número de Quartos", values=["1", "2", "3"], choice="", width=180)
        self.bedrooms.grid(row=2, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

	    # Número de Camas 
        self.beds = OptionMenuFrame(self.tab("Informações do Imóvel"), "Número de Camas", values=["1", "2", "3"], choice="", width=180)
        self.beds.grid(row=2, column=1, padx=(15, 0), pady=(15, 5), sticky="nswe")

	    # Número de Comodidades
        self.num_amenities = Entry(self.tab("Informações do Imóvel"), title="Número de comodidades", width=180)
        self.num_amenities.grid(row=3, column=0, padx=(0, 15), pady=(15, 5), sticky="nswe")

        # ----------------------------------------------------------------------------------------------------------------
        # Data e Local

        # Label Data
        self.date = customtkinter.CTkLabel(self.tab("Data e local"), text="Data", fg_color="#1F6AA5", corner_radius=6)
        self.date.grid(row=0, column=0, padx=0, pady=(15, 5), sticky="ew", columnspan=2)

        # Mês
        self.month = OptionMenuFrame(self.tab("Data e local"), "Mês", values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"], choice="", width=180)
        self.month.grid(row=1, column=0, padx=(0, 15), pady=(0, 0), sticky="ew")

        # Ano
        self.year = OptionMenuFrame(self.tab("Data e local"), "Ano", values=["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"], choice="", width=180)
        self.year.grid(row=1, column=1, padx=(15, 0), pady=(0, 0), sticky="ew")

        # Label localização
        self.localization = customtkinter.CTkLabel(self.tab("Data e local"), text="Localização", fg_color="#1F6AA5", corner_radius=6)
        self.localization.grid(row=2, column=0, padx=0, pady=(15, 5), sticky="ew", columnspan=2)

        # Latitude
        self.latitude = Entry(self.tab("Data e local"), title="Latitude", width=200)
        self.latitude.grid(row=3, column=0, padx=(0, 15), pady=(0, 0), sticky="ew")

        # Longitude
        self.longitude = Entry(self.tab("Data e local"), title="longitude", width=200)
        self.longitude.grid(row=3, column=1, padx=(15, 0), pady=(0, 0), sticky="ew")