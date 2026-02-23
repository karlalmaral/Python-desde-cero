# Programa: Operaciones básicas
# Autora: Karla Almaral

print("=== CALCULADORA BÁSICA ===")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Validar división entre cero
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

print("\nResultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
