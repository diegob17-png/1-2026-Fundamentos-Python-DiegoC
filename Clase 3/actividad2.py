print ("hola mundo")
# Mensaje de bienvenida
print("Cálculo de IMC")

#datos
nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
edad = input("Ingrese su edad: ")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Cálculo del IMC
imc = peso / (altura ** 2)

# Variables del IMC
if imc < 18.5:
    rango = "Bajo peso"
elif imc < 25:
    rango = "Peso normal"
elif imc < 30:
    rango = "Sobrepeso"
else:
    rango = "Obesidad"

# Resultados
print("\n--- Resultado ---")
print("Nombre completo:", nombre, apellidos)
print("Edad:", edad)
print("Su IMC es:", round(imc, 2))
print("Rango:", rango)