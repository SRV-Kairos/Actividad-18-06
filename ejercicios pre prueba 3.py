#Ejercicio 1
import time
import os
'''
while  True:
    try:
        cant = int (input("Ingrese la cantigad de personas a registrar: "))
        break
    except:
        print("Debe ingresar un numero entero.")
esquema_completo,esquema_incompleto=[0,0]
dosis_completa=3
for _ in range(cant):
    while True:
        try:
            dosis = int(input("Ingrese cantidad de dosis recibidas:\n "))
            break
        except:
            print("Debe ingresar un numero entero.")
    if dosis == dosis_completa:
        print("Esquema Completo")
        esquema_completo += 1
    else:
        print("Esquema Incompleto")
        esquema_incompleto += 1
print(f"Se registraron {esquema_completo} personas con esquema completo.\nSe registraron {esquema_incompleto} personas con esquema incompleto.")
'''
#Ejercicio 2
mayor=-1
menor=101
suma=0
contador=0

while True:
    
        print("         Menu Principal          ")
        print("1.-Ingresar Numero Entero")
        print("2.-Mostrar Numero Mayor")
        print("3.-Mostrar Promedio")
        print("4.-Fin del Programa")
        op=input("Elija Opcion: ")
        if op == "1":
            while  True:
                try:
                    n = int(input("Ingrese numero entre 0 y 100"))
                    if n >= 0 and n <=100:
                        print("Ingreso Exitoso")
                        break
                    else:
                        print("Debe ingresar un numero entre 0 y 100")    
                except:
                    print("Debe Ingresar un numero entero!!")
            if n > mayor:
                mayor=n
            suma += n
            contador += 1   

        elif op == "2":
            if mayor == -1:
                print("No se ha ingresado un numero.")
            else:
                print(f"El numero mayor hasta el momento es: {mayor}")    

        elif op == "3":
            if contador == 0:
                print("No se ha ingresado numero para calcular promedio")
            else:
                promedio = suma / contador
                print(f"El promedio de los numeros ingresados es: {promedio:.2f}")
        elif op == "4":
            print("Fin del Progama. Adios.")
            break
        else:
            print("Debe ingresar una opcion valida!")                    

