print ("cajero automatico")
print ("bienvenido al cajero automatico")

saldo = 0
while  True:
    print ("1. consultar saldo")
    print ("2. retirar dinero")
    print ("3. depositar dinero")
    print ("4. salir")
    opcion = int (input ("seleccione una opcion: "))
    if opcion == 1: 
        print ("su saldo es: ", saldo)
    elif opcion == 2: 
        cantidad = int(input("ingrese la cantidad a retirar: "))
        if cantidad > saldo:
            print ("no tiene suficiente saldo")
        else:
            saldo = saldo - cantidad 
            print (f"ha retirado:{cantidad}")
    elif opcion == 3: 
        cantidad = int (input("ingrese la cantidad a depositar: "))
        saldo = saldo + cantidad
        print (f"ha depositado: {cantidad}")
    elif opcion == 4:
        print ("gracias por usar el cajero automatico")
        break
    else:
        print ("opcion no valida")

