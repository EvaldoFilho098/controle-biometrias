import tkinter as tk
from tkinter import N, W, S, E, RIGHT, LEFT, TOP, BOTTOM, BOTH, Y, X
from tkinter import ttk
from PIL import Image, ImageTk




def redimensionar(diretorio, x, y = None):
    
    image = Image.open(diretorio)

    if type(x) == tuple:
        image = image.resize(x)
    else:
        if y:
            image = image.resize((x, y))
        else:
            image = image.resize((x, x))
     
    return ImageTk.PhotoImage(image)


class View:
    def __init__(self, master=tk.Tk):

        ## Janela Principal
        self.root = master

        ## Modelagem de banco de dados
        self.model = None

        ## Imagens da Tela
        self.load_components()

        ## Configurações da Janela
        self.window_settings()

        ## Carrega Pagina Inicial
        self.main_window()

    def window_settings(self):
        """Configurações da Janela
        """

        ## Titulo 
        self.root.title("Meta Certificado Digital - Controle de Biometrias")

        ## Icone
        self.root.iconbitmap(default="Icones/icon.ico")

        ## Cor de Fundo
        self.root.configure(background=self.background_main_color)

        ## Transparencia
        self.root.attributes("-alpha", 0.995)

        ## Tamanho da Pagina
        self.root.geometry("900x700")
        
        ## Tamanho Mínimo da Pagina
        self.root.minsize(width=900, height=700)

        ## Não redimensionar
        self.root.resizable(width=True, height=True)
        
    def load_components(self):
        """
        Carregar Componentes que serão usados na tela
        """

        ##### IMAGENS 
        self.biometria_on = redimensionar("Icones\\biometria_on.png", 50)
        self.biometria_off = redimensionar("Icones\\biometria_off.png", 50)
        self.griaule_on = redimensionar("Icones\\griaule_on.png", 50)
        self.griaule_off = redimensionar("Icones\\griaule_off.png", 50)
        self.treinamento_on = redimensionar("Icones\\treinamento_on.png", 50)
        self.treinamento_off = redimensionar("Icones\\treinamento_off.png", 50)
        self.add = redimensionar("Icones\\add.png", 50)
        self.search = redimensionar("Icones\\search.png", 25)

        ##### CORES
        self.background_main_color = "#333333"          # CINZA ESCURO
        self.background_second_color = "#1F1F1F"        # PRETO
        self.foreground_main_color = "#FFFFFF"          # BRANCO
        self.foreground_second_color = "#B8B8B8"        # PRATEADO
        self.contrast_color = "#FF6900"                 # LARANJA META
        self.silver = "#B8B8B8"                         # PRATEADO
        self.green = "#00B600"                          # VERDE 
        self.red = "#C80000"                            # VERMELHO 
        self.ligh_grey = "#7A7A7A"                      # CINZA CLARO

        ##### FONTES
        #Sugestões: ["Century Gothic"], ["Somatype Heavy"], ["Caudex"]
        self.title_font = ('Century Gothic', 32)
        self.main_font = ('Inter', 18)
        self.description_font = ('Inter', 14)
        self.texts_font = ('Inter', 12)

        self.settings_frame_info = {
            'main_font': self.main_font,
            'description_font': self.description_font,
            'background_color': self.background_second_color,
            'foreground_main_color': self.foreground_main_color,
            'foreground_second_color': self.foreground_second_color,
            'griaule_image': self.griaule_off,
            'biometria_image': self.biometria_on,
            'treinamento_image': self.treinamento_off,
            'border_color': self.silver
        }

    def set_model(self, model):
        self.model = model

    def create_menus(self):
        pass

    def main_window(self):
        

        ###### CABEÇALHO
        ## FRAME
        self.head_frame = tk.Frame(self.root, background=self.background_main_color)
        self.head_frame.pack(fill=X)
        ## TITULO
        self.title = ttk.Label(self.head_frame, 
                               text='Controle de Biometrias', 
                               font=self.title_font, 
                               background=self.background_main_color, 
                               foreground=self.foreground_main_color
                               )
        self.title.pack(side=LEFT, padx=15, pady=15)
        ## BOTÃO DE CADASTRO
        self.add_button = ImageButton(self.head_frame, image=self.add, background=self.background_main_color)
        self.add_button.pack(side=RIGHT, padx=15, pady=15)


        ###### AREA DE PESQUISA
        ## FRAME
        self.search_frame = tk.Frame(self.root, background=self.background_main_color)
        self.search_frame.pack(fill=X)
        ## PESQUISAR NOME
        self.name_search_label = ttk.Label(self.search_frame, 
                               text='Nome: ', 
                               font=self.texts_font, 
                               background=self.background_main_color, 
                               foreground=self.foreground_main_color
                               )
        self.name_search_label.pack(side=LEFT, padx=5)
        ## ENTRY NOME
        self.name_search_entry = tk.Entry(self.search_frame, 
                                          background=self.background_main_color, 
                                          font=self.texts_font, 
                                          highlightbackground=self.background_main_color, 
                                          foreground=self.foreground_main_color,
                                          width=25
                                          )
        self.name_search_entry.pack(side=LEFT, padx=5)
        ## BOTÃO DE PESQUISA NOME
        self.search_name_button = ImageButton(self.search_frame, image=self.search, background=self.background_main_color)
        self.search_name_button.pack(side=LEFT, padx=5)
        
        ## PESQUISAR CPF
        self.cpf_search_label = ttk.Label(self.search_frame, 
                               text='CPF: ', 
                               font=self.texts_font, 
                               background=self.background_main_color, 
                               foreground=self.foreground_main_color
                               )
        self.cpf_search_label.pack(side=LEFT, padx=5)
        ## ENTRY CPF
        self.cpf_search_entry = tk.Entry(self.search_frame, 
                                          background=self.background_main_color, 
                                          font=self.texts_font, 
                                          highlightbackground=self.background_main_color, 
                                          foreground=self.foreground_main_color,
                                          width=25
                                          )
        self.cpf_search_entry.pack(side=LEFT, padx=5)
        ## BOTÃO DE PESQUISA CPF
        self.cpf_search_button = ImageButton(self.search_frame, image=self.search, background=self.background_main_color)
        self.cpf_search_button.pack(side=LEFT, padx=5)

        
        self.frame = InfosFrame(self.root, self.rearrange_name('EVALDO ARÊDES MORAIS FILHO'),'108.285.046-28', self.settings_frame_info)
        self.frame.pack(pady=10)

    def rearrange_name(self, name=str):
        
        if len(name) > 35:
            names = name.split(' ')
            new_name = names[0] + names[2]
            return new_name

        else:
            return name 
        

class ImageButton(tk.Button):
    def __init__(self, master, image, background, **cnf):
        super().__init__(master, image=image, background=background, relief='flat', cnf=cnf)

        self.value = False

class InfosFrame(tk.Frame):
    def __init__(self, master, main_info, second_info, settings, **cnf):
        super().__init__(master, cnf=cnf)

        self.configure(width=750, 
                       height=70, 
                       background=settings['background_color'], 
                       highlightbackground=settings['border_color'], 
                       highlightthickness='1px'
                       )

        self.frame = tk.Frame(self, width=750, height=70, background=settings['background_color'])
        self.frame.grid(sticky=(N, S, E, W))
        self.frame.grid_propagate(0)
        
        self.main_info = ttk.Label(self.frame, 
                                   text=main_info, 
                                   font=settings["main_font"], 
                                   background=settings["background_color"], 
                                   foreground=settings["foreground_main_color"]
                                   )
        self.second_info = ttk.Label(self.frame, 
                                    text=second_info, 
                                    font=settings["description_font"], 
                                    background=settings["background_color"], 
                                    foreground=settings["foreground_second_color"]
                                    )
        self.griaule_button = ImageButton(self.frame, 
                                        image=settings["griaule_image"], 
                                        background=settings["background_color"]
                                        )
        self.biometria_button = ImageButton(self.frame, 
                                        image=settings["biometria_image"], 
                                        background=settings["background_color"]
                                        )
        self.treinamento_button = ImageButton(self.frame, 
                                        image=settings["treinamento_image"], 
                                        background=settings["background_color"]
                                        )

        columnspan = 5
        self.main_info.grid(column=0, row=0, columnspan=columnspan ,sticky=(N, W), padx=5, pady=5, ipady=5)
        self.second_info.grid(column=0, row=1, columnspan=columnspan, sticky=(N, W), padx=5, pady=5, ipady=5)
        self.griaule_button.grid(column=columnspan+1, row=0, rowspan=2, sticky=(N, S, E, W), padx=5)
        self.biometria_button.grid(column=columnspan+2, row=0, rowspan=2, sticky=(N, S, E, W), padx=5)
        self.treinamento_button.grid(column=columnspan+3, row=0, rowspan=2, sticky=(N, S, E, W), padx=5)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=columnspan)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
                    




        


        
