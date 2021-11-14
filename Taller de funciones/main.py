frutas  = open('frutas.txt', 'r')
numeros = open('numeros.txt','r')

lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt

aux=[]
elem="\n"
for i in frutas:
  lista_frutas.append(i.replace(elem," "))

print('lista frutas',lista_frutas)

#Llenar las lista con los datos del archivo numeros.txt

lista_numeros=[]

for i in numeros:
  lista_numeros.append(i.replace(elem,""))

print('lista numeros',lista_numeros)

#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista(str)-->list-->lista
elemento-->str-->elem
Salidas:
lista(str)-->list-->lista
"""

def eliminar_un_caracter_de_toda_la_lista(lista:list,elem:str)->list:
  aux=[]
  for i in lista:
    a=i.replace(elem,"")
    aux.append(a)
  return aux

print('eliminar caracter',eliminar_un_caracter_de_toda_la_lista(lista_frutas,'a'))


#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
Salidas
"""


def copia_lista(lista):
  return lista.copy() 

copia_frutas = copia_lista(lista_frutas)
print('copia frutas',copia_frutas)


#Realizar una funcion que retorne una lista de numeros enteros 
"""  
Entradas:
Salidas
"""


def numeros_pares(lista):
  temp = []
  for i in lista:
    if float(i)%2 == 0:
      temp.append(i)
  
  return temp

pares = numeros_pares(lista_numeros)
print('lista pares',pares)


#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
Salidas
"""
 
def elimina_elemento_lista(lista,elem):
  lista.remove(elem)
  return lista

print('eliminar elemento',elimina_elemento_lista(lista_frutas,'Kiwi'))


#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
Salidas
"""

def letra(lista,letra):
  temp = []
  for i in lista:
    if i[0] == letra:
      temp.append(i)

  return temp

print('iniciales',letra(lista_frutas,'A'))

#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
Salidas
""" 


  
def tamano_lista(lista):
  return len(lista)

print('tamano',tamano_lista(lista_numeros))

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista

"""
Entradas:
Salidas
"""  

def informacion_lista(lista):
  types = [type(i) for i in lista]
  types = set(types)

  return len(lista), types

print('info',informacion_lista(lista_numeros))
 

#Retornar una lista con los numero negativos  
"""
Entradas:
Salidas
"""
  
def numeros_negativos(lista):
  neg = [n for n in lista if float(n) < 0]
  return neg

print('negativos',numeros_negativos(lista_numeros))


#realizar una funcion que retorne la posicion de un elemento que pasa por parametro

def posicion_elemento(lista,elemento):
  return lista.index(elemento)

print('pos',posicion_elemento(lista_frutas,'Coco'))


#realizar una funcion que agregue al final de archivo frutas una fruta
 
def frutas(elemento):
  new_archivo = open('frutas.txt', 'a',encoding="utf8")
  new_archivo.write("\n")
  new_archivo.write(elemento)

frutas('Patilla')

#Realizar una funcion que cuente el numero de veces que se repite un elemento  
 
def repetir(lista,elemento):
  reps = 0
  for i in lista:
    if i == elemento:
      reps += 1

  return reps

print('reps',repetir(lista_numeros,'21'))


 