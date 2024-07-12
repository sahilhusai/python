form tkinter_import *
from tkinter import ttk
win =Tk()
win.title("Wscube Tech")
win.config(bg ="blue")
win.geometry("500*500")

name_lable =Lable(win,text=Wscube Weather App",
                    fornt=("Time New Roman",40,"bold"))
name_lable.place(x=25,y=50,hight=50,width=450)

com =ttk.Combobox(win,text="Wscube Weather App",value)