#mi primer calculadora en python
print("Bienvenido a la calculadora básica ... ")
#declaramos un mensaje de bienvenida para el usuario
while True:
    #usamos while para generar un menu de opciones para el usuario
    print("\n--- Calculadora basica ---")
    print("1. Suma ")
    print("2. Resta")
    print("3. Multiplicación")
    print("4.División")
    print("5. Salir")

    opcion = input("Elige una opción: ")
    #pedimos al usuario que ingrese una opción para realizar la operación deseada

    if opcion == "1":
        print("---Bienvenido a Sumar---")
        #pedimos al usuario que ingrese la cantidad de números que desea sumar
        cantidad = int(input("¿Cuántos números deseas sumar? "))
        total = 0
        contador = 1
        while contador <= cantidad:
            #usamos un conrador para iterar la cantidad de números que el usuario desea sumar
            num = float(input("Ingrese un número: "))
            total += num
            contador += 1
        print("El total de la suma es:", total)

    elif opcion == "2":#elección de la opción 2 para realizar la resta
        print("---Bienvenido  a Restar----")
        num1 = float(input("ingresa el primer numero: "))
        num2 =float(input("ingresa el segundo numero:  "))
        resta = num1 - num2
        print("Resultado:", resta)
    elif opcion=="3":#elección de la opción 3 para realizar la multiplicación
        print("Bienvenido a Multiplicación")
        num1 = float ( input("ingresa el primer número"))
        num2 = float (input("ingresa el segundo número"))
        multi= num1 * num2
        print("Resultadom",multi)

    elif opcion =="4":#elección de la opción 4 para realizar la división
      print("Bienvenido a división")
      num1 = float(input("Ingresa el primer número: "))
      num2 = float(input("Ingresa el segundo número: "))
      if num2 != 0:
        print("Resultado:", num1 / num2)
      else:
        print("Error: no se puede dividir entre cero.")
        #si el usuario ingresa 0 como segundo número se muestra un mensaje de error para evitar la división entre cero

    elif opcion == "5":
        print("Saliendo del programa...")
        break #si el usuario ingresa 5 se muestra un mensaje de despedida y se sale del programa
    else:
        print("Opción inválida. Intenta otra vez.")
        #si el usuario ingresa una opción diferente a 1,2,3,4 o 5 se muestra un mensaje de error para que intente nuevamente