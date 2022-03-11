from tkinter import *
import Util
import math
from Conversiones import conversiones

class calculoW:
    def __init__(self,caFre,caDie,caHei):
        self.f = caFre.get()
        self.Er = caDie.get()
        self.h = caHei.get()
    def guidedWave(self):
        lg = 300/(self.f*math.sqrt(self.Er)) 
        return lg
    def ApproximateW(self,Zc):
        A = Zc/60*((self.Er+1)/2)**0.5+(self.Er-1)/(self.Er+1)*0.23+0.11/self.Er
        W = (8*math.exp(A)*self.h)/(math.exp(2*A)-2)
        return W
    def Approximatel(self,deg):
        rs = conversiones()
        l = (rs.raDeg(deg)*self.guidedWave())/(2*math.pi)
        return l
    def lambd(self):
        lg =self.guideWave()
        ElecLength = lg/4
        return ElecLength
    def ejecutar(self, Zc,le):
        self.ApproximateW(Zc)
        self.Approximatel(le)
v = Tk()
v.title("Microstrip Line Calculator")
v.minsize(width =512 ,height = 256)
lbl = Util.agregarImagen(v,"4.png",1,5, 40, 5)
Label(v,text="").grid(row=6, column=2)
Label(v,text="").grid(row=7, column=2)
Label(v,text="Frequency").grid(row=1, column=0)
Label(v,text="GHz").grid(row=1, column=2)
caFre = Util.agregarCaja(v,10,1,1)
Label(v,text="Dielectric Constant [εr]").grid(row=2, column=0)
caDie = Util.agregarCaja(v,10,2,1)
Label(v,text="Zo").grid(row=3, column=0)
Label(v,text="[Ω]").grid(row=3, column=2)
caImp = Util.agregarCaja(v,10,3,1)
Label(v,text="Dielectric Height (h)").grid(row=4, column=0)
Label(v,text="mm").grid(row=4, column=2)
caHei = Util.agregarCaja(v,10,4,1)
Label(v,text="Elec. Length").grid(row=5, column=0)
Label(v,text="deg").grid(row=5, column=2)
caLen = Util.agregarCaja(v,10,5,1)
#f = caFre.get(); Er = caDie.get() ; Z = caImp.get() ; h = caHei.get() ; le = caLen.get()
#W = calculoW(f,E,h)
#calc = W.ejecutar(Z,le)
Util.boton(v,"Synthesize",calculoW,8,0)
cajW = Util.agregarCaja(v, 10, 8,1)
Label(v,text = "[mm]").grid(row = 8, column = 2)
#cajW.configure(state=NORMAL)
cajW.delete(0,END)
cajW.insert(0, calc)
#cajW.configure(state=DISABLED)
cajL = Util.agregarCaja(v, 10, 8,1)
Label(v,text = "[mm]").grid(row = 8, column = 2)
#cajL.configure(state=NORMAL)
cajL.delete(0,END)
cajL.insert(0, calc)
#cajL.configure(state=DISABLED)


