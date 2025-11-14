import ttkbootstrap as ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox
import random

lista_frutas=['🍉','🍊','🍒','🍓','🍎']


class SorteioDeFrutas:
    def __init__(self):


        #configuração da janela principal e da Treeview
        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Sorteio de Fruta")
        self.janela.geometry("950x950+0+0")

       
        
        self.label_sorteio = ttk.Label (self.janela,
                                        text= "SORTEIO DE FRUTAS",
                                        font=("Broadway" , 25))
        self.label_sorteio.pack()


        self.label_fruta1 = ttk.Label (self.janela,
                                  text="🌺",
                                  font=("Arial", 40)
                                  ,relief="raised")
        self.label_fruta1.pack()



        self.label_fruta2 = ttk.Label (self.janela,
                                  text="🌺",
                                  font=("Arial", 40)
                                  ,relief="raised")
        self.label_fruta2.pack()


        self.label_fruta3 = ttk.Label (self.janela,
                                  text="🌺",
                                  font=("Arial", 40)
                                  ,relief="raised")
        self.label_fruta3.pack()



        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack () 


        ttk.Button(frame_botao, text="SORTEAR",command=self.soreteio).pack(side="right", pady= 100, padx=70 )


        label_jogadas = ttk.Label (self.janela,
                                        text= "Historico de Jogadas",
                                        font=("Arial" , 15))
        label_jogadas.pack()



        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack(padx=15, pady=20, fill="both", expand=True)




    def soreteio(self):
         fruta1= random.choice(lista_frutas)
         fruta2= random.choice(lista_frutas)
         fruta3= random.choice(lista_frutas)


         self.label_fruta1.config(text=fruta1)
         self.label_fruta2.config(text=fruta2)
         self.label_fruta3.config(text=fruta3)
         


       
    def run(self):
            self.janela.mainloop()

if __name__ == "__main__":
    jf= SorteioDeFrutas()
    jf.run()
