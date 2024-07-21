# Importação de bibliotecas
import customtkinter
import webbrowser
from PIL import Image
from DataCompatibility import DataCompatibility


# Classe da Barra Lateral
class SideBar(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Atributos
        self.grid_columnconfigure(0, weight=1)
        self.data_compatibility = DataCompatibility

        # Titulo do aplicativo
        self.app_title = customtkinter.CTkLabel(self, text="Sobre o aplicativo", fg_color="#1F6AA5", corner_radius=10, width=150, font=("Arial", 20), padx=10, pady=10)
        self.app_title.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="ew", columnspan=3)

        # Breve Texto sobre o Aplicativo
        self.app_description = customtkinter.CTkLabel(self, text="Baseado nos preços praticados no AirBnb Rio", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=1, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Feito para novos locatários", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=2, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Precificação rápida e prática", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=3, column=0, padx=10, pady=4, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Utiliza inteligência artificial", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=4, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Totalmente offline", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=5, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Totalmente offline", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=5, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="Totalmente gratuito", fg_color="gray30", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=5, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        self.app_description = customtkinter.CTkLabel(self, text="", fg_color="#2B2B2B", corner_radius=6, width=150, pady=10)
        self.app_description.grid(row=6, column=0, padx=10, pady=5, sticky="nswe", columnspan=3)

        # Redes sociais
        self.social_media = customtkinter.CTkLabel(self, text="Saiba mais", fg_color="gray30", corner_radius=6, width=150, font=("Arial", 16))
        self.social_media.grid(row=7, column=0, padx=10, pady=(5, 5), sticky="nswe", columnspan=3)

        # Adiciona GitHub
        self.github_icon = customtkinter.CTkImage(dark_image=Image.open("icons/github_icon.png"), size=(50, 50))
        self.github = customtkinter.CTkButton(self, text="", image=self.github_icon, command=self.button_event_github, width=90, fg_color="#2B2B2B")
        self.github.grid(row=9, column=0, padx=(10, 0), pady=(5, 5))

        # Adiciona Kaggle
        self.kaggle_icon = customtkinter.CTkImage(dark_image=Image.open("icons/kaggle_icon.png"), size=(50, 50))
        self.kaggle = customtkinter.CTkButton(self, text="", image=self.kaggle_icon, command=self.button_event_kaggle, width=90, fg_color="#2B2B2B")
        self.kaggle.grid(row=9, column=1, padx=0, pady=(5, 5))

        # Adiciona LinkedIn
        self.linkedin_icon = customtkinter.CTkImage(dark_image=Image.open("icons/linkedin_icon.png"), size=(50, 50))
        self.linkedin = customtkinter.CTkButton(self, text="", image=self.linkedin_icon, command=self.button_event_linkedin, width=90, fg_color="#2B2B2B")
        self.linkedin.grid(row=9, column=2, padx=(0, 10), pady=(5, 5))

    # Função do botão github
    def button_event_github(self):
        webbrowser.open_new("https://github.com/SEduardo-36524")

    # Função do botão Kaggle
    def button_event_kaggle(self):
        webbrowser.open_new("https://www.kaggle.com/eduardoferreirasilva")

    # Função do botão LinkedIn
    def button_event_linkedin(self):
        webbrowser.open_new("https://www.linkedin.com/in/eduardo-ferreira-silva-40751218a/")