
import math
def main():
    # Escribe tu código abajo de esta línea
    #radio (flotante)
    #x1 Coordenada x del centro de la circunferencia (flotante)
    #y1 Coordenada y del centro de la circunferencia (flotante)
    #x2 Coordenada x del punto (flotante)
    #y2 Coordenada y del punto (flotante)
    r= float(input("Introduce el radio: "))
    x1= float(input("Introduce x1: "))
    y1= float(input("Introduce y1: "))
    x2= float(input("Introduce x2: "))
    y2= float(input("Introduce y2: "))
    a= math.sqrt((x2-x1)**2+(y2-y1)**2)
    if a>r:
        print("FUERA")
    elif a<r:
        print("DENTRO")
    elif a==r:
        print("SOBRE")    


if __name__ == '__main__':
    main()
