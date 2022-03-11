from tkinter import W
import numpy as np
import conversiones
import math




class Line:
    def __init__(self,f,Er,h):
        self.f = f
        self.Er = Er
        self.h = h
        self.lg=self.guidedWave()
    def lambd(self):
        lg =self.guideWave()
        ElecLength = lg/4
        return ElecLength
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
    
    def ejecutar(self, Zc,le):
        self.ApproximateW(Zc)
        self.Approximatel(le)

class Stripline(Line):
    def __init__(self,w=0,b=1):
        self.w= w
        self.b= b
        

    def wEfectiva(self):
        if self.w/self.b > 0.35:
            wEfectiva= self.w
        elif self.w/self.b<0.35:
            pass
