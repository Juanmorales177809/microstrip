from numpy import deg2rad,rad2deg
from math import sqrt, pi, exp, log



class Line:
    def __init__(self,f,Er,h,t,l,conductividad,tan,zo):
        self.f = f
        self.Er = Er
        self.h = h
        self.t= t
        self.c= 3*10**8
        self.l= l
        self.mu = 4*pi*10**-7
        self.conductividad= conductividad
        self.tanPerdidas= tan
        self.zo= zo
        self.eta= 120*pi #Impedancia de la onda en el espacio libre
        
        
    def longitudElectrica(self):
        return pi/(2*self.beta())
        
            
    def ondaGuiada(self):
        return 3*10**8/(self.f*sqrt(self.Er))
    def ApproximateW(self):
        A = self.zo/60*((self.Er+1)/2)**0.5+(self.Er-1)/(self.Er+1)*0.23+0.11/self.Er
        W = (8*exp(A)*self.h)/(exp(2*A)-2)
        return W
    def Approximatel(self):
        return rad2deg(self.l)*self.ondaGuiada()/(2*pi)
    def beta(self):
        return 2*pi/0.059
    def velocidadPropagacion(self):
        return self.c/sqrt(self.permitividadEfectiva())
    
class Stripline(Line):
    
    def wEfectiva(self):
        if self.w/self.b > 0.35:
            wEfectiva= self.w
        elif self.w/self.b<0.35:
            pass

class MicrostripLine(Line):
    
    def rs(self):
        return sqrt((2*pi*self.f*self.mu)/(2*self.conductividad))
    
    def ko(self):
        return self.beta()/sqrt(self.permitividadEfectiva())
    
    def permitividadEfectiva(self):
        w= self.ApproximateW()
        if w/self.h <= 1:
            ereff= (self.Er+1)/2+(self.Er-1)/2*(1+12*(self.h/w)**(-0.5)+0.04*(1-(w/self.h)**2))
        else:
            ereff= (self.Er+1)/2+(self.Er-1)/2*(1+12*(self.h/w)**(-0.5))
        return ereff
    
    def impedanciaCaracteristica(self):
        w= self.ApproximateW()
        if w/self.h <= 1:
            zc=  self.eta/2*pi*sqrt(self.permitividadEfectiva())*log((8*self.h)/w+0.25*(w/self.h))
        else:
            zc= self.eta/sqrt(self.permitividadEfectiva())*((w/self.h)+1.393+0.677*log((w/self.h)+1.444))**-1
        return zc
    
    
    
    def capacitanciaAsociada(self):
        w= self.ApproximateW()
        wh= self.ApproximateW()/self.h
        if w/self.h <=1:
            capacitancia= self.permitividadEfectiva()/(60*self.c*log(8*self.h/w+w/(4*self.h)))
        else:
            cap= self.permitividadEfectiva()*self.longitudElectrica()
            ci = (wh+1.393+0.667)
            tanc= log(wh+1.444)
            div= 120*pi*3*10**8
            capacitancia= (cap*(ci*tanc))/(120*pi*3*10**8)

        return capacitancia, cap, ci, tanc,div

    def perdidasConductor(self):
        w= self.ApproximateW()
        return 8.686*self.rs()/(self.impedanciaCaracteristica()*w)
    
    def perdidasDielectrico(self):
        alfaNp= (self.ko()*self.Er*(self.permitividadEfectiva()-1)*self.tanPerdidas)/(2*sqrt(self.Er)*(self.permitividadEfectiva()-1))
        alfadB= 8.686*pi*(self.permitividadEfectiva()-1)/(self.Er-1)*self.Er/(self.permitividadEfectiva())*self.tanPerdidas/self.ondaGuiada()
        return alfaNp, alfadB


