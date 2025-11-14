import ttkbootstrap as ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox


class SorteioDeFrutas:
    def __init__(self):


        #configuração da janela principal e da Treeview
        self.janela = ttk.Window(themename="darkly")
        self.janela.title("Sorteio de Fruta")
        self.janela.geometry("950x950+0+0")

       
       
        
        label_caixa1 = ttk.Label (self.janela)
                                        
        label_caixa1.pack()


        label_caixa2 = ttk.Label (self.janela)
                                        
        label_caixa2.pack()


        label_caixa3 = ttk.Label (self.janela)
                                        
        label_caixa3.pack()



        # #campo de espaço para escrever as infomaçoes pedidas (item_nome) 
        # self.campo_item = ttk.Entry(self.janela, width=10)
        # self.campo_item.pack(pady=5)



        
        label_sorteio = ttk.Label (self.janela,
                                        text= "SORTEIO DE FRUTAS",
                                        font=("Broadway" , 25))
        label_sorteio.pack()


        label_fruta1 = ttk.Label (self.janela,
                                  text="🌺",
                                  font=("Arial", 40)
                                  ,relief="raised")
        label_fruta1.pack()



        # #informações do cabeçalho
        # self.treeview["columns"] = ( "ID", "ITEM", "DESCRIÇÃO", "STATUS" )
        # self.treeview["show"] = "headings"

    def run(self):
            self.janela.mainloop()

if __name__ == "__main__":
    jf= SorteioDeFrutas()
    jf.run()
