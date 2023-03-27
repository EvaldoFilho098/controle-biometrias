import tkinter as tk
from PIL import Image, ImageTk


def redimensionar(diretorio, tam, x = ''):
    
    image = Image.open(diretorio)

    if x == '':
        x = tam
    
    if type(tam) == tuple:
        image = image.resize(tam)
    else:
        image = image.resize((tam, x))

        
    return ImageTk.PhotoImage(image)


class View:
    def __init__(self, master=tk.Tk):
        self.root = master
        self.model = None
        self.load_images()

        # Icone
        self.root.iconbitmap(default="Icones/icon.ico")

        # Cor de Fundo
        self.root.configure(background='black')

        # Transparencia
        self.root.attributes("-alpha", 0.995)

        #self.root.attributes("-fullscreen", True)
        #self.root.state('zoomed')

        # Lista de todos os Widgets adicionados na tela
        self.lista_widgets = []

        # Tamanho da Pagina
        self.root.geometry("1224x700")
        #self.root.geometry("1300x745")

        # Tamanho Mínimo da Pagina
        self.root.minsize(width=1224, height=700)

        # Nao redimensionar
        self.root.resizable(width=True, height=True)

        self.root.title("Meta Certificado Digital - Controle de Biometrias")



        # Criar o botão
        self.bio = 0
        self.button = tk.Button(self.root, image=self.biometria_off, background='black', relief='flat',command=self.increment_counter)
        self.button.pack()

        # Criar o label
        self.label = tk.Label(self.root, text="Contador: 0")
        self.label.pack()
    
    def load_images(self):
        self.biometria_on = redimensionar("Icones\\biometria_on.png", 50)
        self.biometria_off = redimensionar("Icones\\biometria_off.png", 50)
        self.griaule_on = redimensionar("Icones\\griaule_on.png", 50)
        self.griaule_off = redimensionar("Icones\\griaule_off.png", 50)
        self.treinamento_on = redimensionar("Icones\\treinamento_on.png", 50)
        self.treinamento_off = redimensionar("Icones\\treinamento_off.png", 50)

        
    def set_model(self, model):
        self.model = model

    def increment_counter(self):
        if self.bio == 0:
            self.button.config(image=self.biometria_on)
            self.bio = 1
        else:
            self.button.config(image=self.biometria_off)
            self.bio = 0



        
