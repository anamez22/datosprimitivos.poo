#Ejercicio 1
numeros = [5,10,15,20,25]
cuadrados = [numero**2 for numero in numeros]

print("Lista de números elevados al cuadrado: ", cuadrados)

#Ejercicio 2

nombre = "Gonzalo Arango"
edad = 50
mensaje = f"Hola, mi nombre es {nombre} y tengo {edad} años"

print(mensaje)

#Ejercicio 3 

edad = 63
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Ejercicio 4
saldo = 100.0
while saldo > 10:
    retiro = 15.0
    saldo -=retiro
    print(f"Se ha retirado {retiro}, saldo actual: {saldo}")

#Ejercicio 5
persona ={
    "nombre":"Marco",
    "edad":56,
    "ciudad":"Madrid"
}

for clave, valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")