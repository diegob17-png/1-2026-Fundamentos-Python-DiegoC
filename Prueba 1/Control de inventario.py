print ("Hola mundo")

#Control inventario

print ("Control inventario")

nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad disponible: "))

# Calcular valor total
total_inventario = precio * cantidad

# Mostrar resultados
print("\n--- Inventario ---")
print("Producto:", nombre_producto)
print("Precio:", precio)
print("Cantidad disponible:", cantidad)
print("Valor total del inventario:", total_inventario)
