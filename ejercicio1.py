#edad_1= int(input("Introduzca la edad del primer usuario"))
#edad_2= int(input("Introduzca la edad del segundo usuario"))

#if (edad_1 > edad_2):
#    print("El primer usuario es mayor" )
#else:
#     print( "El segundo usuario es mayor")


palabra =input("Introduzca una palabra: ")
cadena_palindroma = palabra[::-1]
if cadena_palindroma==palabra:
    print("Es un palindromo")
else:
    print("No es un palindromo")
