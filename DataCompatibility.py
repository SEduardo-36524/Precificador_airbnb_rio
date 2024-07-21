# Importação de bibliotecas
import customtkinter
import pandas as pd
import joblib
from TabView import TabView


# Classe de compatibilização dos dados
class DataCompatibility:
    def __init__(self):
        super().__init__()

        # Atributos diversos (Se houver)
        self.tab_view = TabView(self)
        self.price = 0
        self.df = {}

    def create_dataframe(self):

        try: 
        # Adiciona os itens ao dicionário
            dict = {'host_is_superhost': [1 if self.tab_view.superhost.get_value() == "Sim" else 0],
                    'host_listings_count': [int(self.tab_view.host_listings_count.get_value())],
                    'latitude': [float(self.tab_view.latitude.get_value())],
                    'longitude': [float(self.tab_view.longitude.get_value())],
                    'accommodates': [int(self.tab_view.accommodates.get_value())],
                    'bathrooms': [int(self.tab_view.bathrooms.get_value())],
                    'bedrooms': [int(self.tab_view.bedrooms.get_value())],
                    'beds': [int(self.tab_view.beds.get_value())],
                    'extra_people': [float(self.tab_view.extra_people.get_value())],
                    'minimum_nights': [int(self.tab_view.extra_people.get_value())],
                    'instant_bookable': [1 if self.tab_view.instant_bookable.get_value() == "Sim" else 0],
                    'ano': [int(self.tab_view.year.get_value())],
                    'mes': [int(self.tab_view.month.get_value())],
                    'num_amenities': [int(self.tab_view.num_amenities.get_value())],
                    'property_type_Apartment': [1 if self.tab_view.property_type.get_value() == "Apartamento" else 0],
                    'property_type_Outros': [1 if self.tab_view.property_type.get_value() == "Outros" else 0],
                    'room_type_Entire home/apt': [1 if self.tab_view.room_type.get_value() == "Casa/Apartamento inteiro" else 0],
                    'room_type_Outros': [1 if self.tab_view.room_type.get_value() == "Outros" else 0], 
                    'cancellation_policy_flexible': [1 if self.tab_view.cancellation_policy.get_value() == "Flexível" else 0],
                    'cancellation_policy_moderate': [1 if self.tab_view.cancellation_policy.get_value() == "Moderada" else 0],
                    'cancellation_policy_strict_14_with_grace_period': [1 if self.tab_view.cancellation_policy.get_value() == "Estrita" else 0],
                    }
            
            # Exibe a mensagem de dados corretos
            self.error = customtkinter.CTkLabel(self, text="Dados Corretamente preenchidos", fg_color="green", corner_radius=6, width=90)
            self.error.grid(row=1, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew")

        # Exibe um erro acima do botão de "Precificar Imóvel"
        except:
            self.error = customtkinter.CTkLabel(self, text="Um ou mais campos não foram preenchidos corretamente,\nverifique-os e tente novamente.", fg_color="red", corner_radius=6, width=90)
            self.error.grid(row=1, column=1, padx=(10, 10), pady=(0, 0), sticky="nsew")
            
        # Transforma em dataframe
        self.df = pd.DataFrame(data=dict)

    def prevision(self):
        # Lê o modelo criado na análise de dados
        model = joblib.load('modelo.joblib')
        # Armazena o preço na variável
        self.price = model.predict(self.df)
        # Escreve o valor previsto
        print(self.price[0])
        return self.price[0]