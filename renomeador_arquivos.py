import os
from tkinter import filedialog

class Arquivo:    
    def abrir_pasta():
        return filedialog.askdirectory()

class Renomeador:
    def renomear_planilha():
        pasta = Arquivo.abrir_pasta()
        print(pasta)
        for arquivo in os.listdir(pasta):
            if arquivo.endswith('.txt'):
                os.rename(pasta+'/'+arquivo,pasta+'/RENOMEADO.txt')
        return

Renomeador.renomear_planilha()