from tkinter import *
from turtle import back
import Util
import math
from conversiones import conversiones
import calculos
from tkinter import ttk 
from pickle import READONLY_BUFFER
from turtle import st



v = Tk()
#v.geometry('500x500')
v.config(background='white')
#v.iconbitmap("./assets/antena.ico")
v.title("Calculo de Radio Enlace Terrestre")
v.configure(bg='beige')

note = ttk.Notebook(v)
note.pack(pady=10, expand=True)
note.grid(row=0,column=0)
webLabel = ttk.Label(note,text="Hello")
frame1 = Frame(note,width=500,height=500,bg='#d7f3bc')
frame2 = Frame(note,width=500,height=500, bg='#B0F9FE')
frame1.pack(fill='both',expand=True)
frame2.pack(fill='both',expand=True)
frame3 = Frame(note,width=500,height=500,bg='#D9B5FE')
frame3.pack(fill='both',expand=True)
# lbl = Util.agregarImagen(frame,"4.png",1,5, 40, 5)
# frame2= Frame(v,height=200,width=200)
# frame.grid(row=1,column=0)
# Label(v,text="").grid(row=6, column=2)
# Label(v,text="").grid(row=7, column=2)
# Label(v,text="Frequency").grid(row=1, column=0)
# Label(v,text="GHz").grid(row=1, column=2)
# caFre = Util.agregarCaja(v,10,1,1)
# Label(v,text="Dielectric Constant [εr]").grid(row=2, column=0)
# caDie = Util.agregarCaja(v,10,2,1)
# Label(v,text="Zo").grid(row=3, column=0)
# Label(v,text="[Ω]").grid(row=3, column=2)
# caImp = Util.agregarCaja(v,10,3,1)
# Label(v,text="Dielectric Height (h)").grid(row=4, column=0)
# Label(v,text="mm").grid(row=4, column=2)
# caHei = Util.agregarCaja(v,10,4,1)
# Label(v,text="Elec. Length").grid(row=5, column=0)
# Label(v,text="deg").grid(row=5, column=2)
# caLen = Util.agregarCaja(v,10,5,1)
# #f = caFre.get(); Er = caDie.get() ; Z = caImp.get() ; h = caHei.get() ; le = caLen.get()
# #W = calculoW(f,E,h)
# #calc = W.ejecutar(Z,le)
# def objeto():
#     calc= calculos.Line()
    




# Util.boton(v,"Synthesize",lambda: objeto(),8,0)
# cajW = Util.agregarCaja(v, 10, 8,1)
# Label(v,text = "[mm]").grid(row = 8, column = 2)
# #cajW.configure(state=NORMAL)
# cajW.delete(0,END)
# cajW.insert(0, calc)
# #cajW.configure(state=DISABLED)
# cajL = Util.agregarCaja(v, 10, 8,1)
# Label(v,text = "[mm]").grid(row = 8, column = 2)
# #cajL.configure(state=NORMAL)
# cajL.delete(0,END)
# cajL.insert(0, calc)
# #cajL.configure(state=DISABLED)


