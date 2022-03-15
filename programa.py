
from calculos import MicrostripLine

def leerNumero(texto):
    numero = 0
    numeroValido = False
    while not numeroValido:
        try:
            numero = float(input(texto))
            numeroValido = True
        except:
            print("El dato no es numerico")
    return numero

print("--------------CALCULO LINEA MICROSTRIP---------------")
# selec= 0
# while selec != 3:
#     print("1. Calcular linea Microsotrip")
#     print("2. Calcula Linea Minstrip")
#     print("3. Salir")

#     selec= leerNumero("Opcion Escogida: ")

#     if selec == 1:
#         f= leerNumero("Ingrese la frecuencia de operación en GHz: ")
#         Er= leerNumero("Ingrese la permitividad electrica del material: ")
#         zo= leerNumero("Ingrese la impedancia caracteristica: ")
#         h = leerNumero("Ingrese grosor del sustrato dielectrico: ")
#         t = leerNumero("Ingrese grosor del material conductor: ")
#         c = leerNumero("Ingrese la conductividad del material conductor: ")
#         tan = leerNumero("Ingrese la tangente de perdidas del material dielectrico: ")
#         l=0
#         linea = MicrostripLine(f,Er,h,t,l,c,tan,zo)
#         print("Permitividad efectiva= ","{0:.3f}".format(linea.permitividadEfectiva()))
#         print("Impedancia caracteristica= ","{0:.3f}".format(linea.impedanciaCaracteristica()))
#         print("Capacitancia asociada= ","{0:.3f}".format(linea.capacitanciaAsociada()))
#         print("Perdidas debido al conductor","{0:.3f}".format(linea.perdidasConductor()))
#         print("Perdidas debido al dielectrico= ","{0:.3f}".format(linea.perdidasDielectrico()[0]))
        
if __name__ == "__main__":
    f=2.46*10**9 ; Er= 4.3 ; h= 1.56 ; t= 0.0035 ; c= 59600000 ; tan= 0.001 ; zo= 50 ; l= 2
    linea= MicrostripLine(f,Er,h,t,l,c,tan,zo)
    print("Permitividad efectiva= ","{0:.3f}".format(linea.permitividadEfectiva()))
    print("Impedancia caracteristica= ","{0:.3f}".format(linea.impedanciaCaracteristica()))
    print("Capacitancia asociada= ","{0:.3f}".format(linea.capacitanciaAsociada()))
    print("Perdidas debido al conductor","{0:.3f}".format(linea.perdidasConductor()))
    print("Perdidas debido al dielectrico= ","{0:.3f}".format(linea.perdidasDielectrico()[0]))
