#uso de for para  contar los numeros pare e impares
cantidad = int(input("¿Cuántos números vas a ingresar? "))

pares = 0
impares = 0
totalimpares=0
totalpares=0

for i in range(cantidad):
    num = int(input("Ingresa un número: "))

    if num % 2 == 0:
      pares +=1
      totalpares += num
    else :
      impares+=1
      totalimpares += num

print("Pares:", pares)
print("Suma de  pares",totalpares)
print("Impares:", impares)
print("Suma de impares",totalimpares)
print("suma de pares mas impares",totalpares+totalimpares)

