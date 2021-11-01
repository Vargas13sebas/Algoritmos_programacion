a = int(input("digite de donde va a comenzar a sumar: "))
b = int(input("digite hasta donde va a terminar a sumar: "))
suma = 0

for i in range(a,b+1):
    if i%2==0: # si el numero es par
        suma += i 

print(f"\n la suma de numeros pares dentro del rango es: {suma}")
