from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

def agregarImagen(ventana, archivo, fila, columna, rowspan, columnspan):
    img = PhotoImage(file=archivo)
    lbl= Label(ventana)
    lbl.config(image=img)
    lbl.image=img
    lbl.grid(row =fila,column = columna, rowspan = rowspan, columnspan = columnspan)
    
    return lbl

def agregarCajaTextoSalida(ventana, ancho, fila, columna, fuente):
    txt = Entry(ventana, width=ancho, font=fuente)
    txt.grid(row=fila, column=columna)
    txt.configure(state=DISABLED)
    return txt

def mostrarCajaTexto(txt, valor):
    txt.configure(state=NORMAL)
    txt.delete(0, END)
    txt.insert(0, valor)
    txt.configure(state=DISABLED)
    
def agregarCaja(ventana,ancho,fila,columna):
    txt = Entry(ventana,width=ancho)
    txt.grid(row=fila, column=columna)
    txt.get()

    
def desplegable(ventana,proc, fila,columna,x,y):
    lista = []
    for p in proc:
        lista.append(p)
    txt = ttk.Combobox(state = "readonly")
    txt.place(x=x,y=y)
    txt.grid(row=fila,column=columna)
    txt["values"] = lista
def dias():
    dias=[]
    for i in range(1,32):
        dias.append(i)
    return dias

def pestana(ventana,text,x,y):
    txt = ttk.Notebook(ventana)
    p=ttk.Frame(txt)
    txt1=ttk.Label(p, text="label")
    txt.add(p,text=text)
    txt.pack(padx=x,pady=y)
    txt.pack(expand=1, fill='both')
    #txt.grid(column=h,row = n)
    ventana.mainloop()
def boton(ventana,text , comando,row,column):
    Button(ventana, text=text, command=comando).grid(row=row, column=column)