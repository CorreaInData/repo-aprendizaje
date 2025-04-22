# Listas

lista = []  # Lista vacía
print("4-",lista,"\n")

lista2 = ["lunes","martes,","miércoles","jueves","viertes"]
print("7-",lista2)   # Impresión de una lista
print("8-",lista2[0])    # Impresión de un elemento (inicial): La lista empieza por el elemento 0
print("9-",lista2[4])    # Impresión de un elemento (final): Aunque la lista tiene 5 elementos, por empezar en 0 sería el 4
print("10-",lista2[-2])   # una lista se puede imprimir contando los elementos desde atrás empezando por -1
print("11-",lista2[1:3])  # Imprime una parte indicada de la lista (hasta un elemento menos del número final indicado)
print("12-",lista2[:4])   # Imprime la lista desde el principio hasta un elemento menos del número final indicado
print("13-",lista2[2:],"\n")  # Imprime la lista desde el número indicado, hasta el final

lista3 = ["sábado","domingo",40,5.67,[1,2,3],True]  # Una lista puede tener t0do tipo de variable
print("16-",lista3)
print("17- lista3 tiene ",len(lista3)," elementos") # La función len sirve para contar los elementos que hay en una lista
lista3[5] = False   # Cambia un elemento especifico de la lista
print("19-",lista3,"\n")

lista4 = [0,1,2,4,5]
lista4.append(6)    # Es un método que sirve para agregar elementos al final de la lista
print("23-",lista4)
lista4.insert(3,3)  # Es un método que sirve para insertar un elemento en el lugar indicado. (lugar de la lista,elemento a insertar)
print("25-",lista4)
lista4.extend([7,8,9])  # Sirve para insertar una lista al final de una lista
print("27-",lista4)
lista4.pop()    # Sirve para eliminar un elemento de la lista. Si se deja vacío elimina el último elemento
print("29-",lista4)
lista4.pop(3)   # Si se pone un número, eliminará el elemento que está en dicha ubicación en la lista
print("31-",lista4)
lista4.remove(1)    # Elimina un elemento indicado (no por su posición) de la lista
print("33-",lista4,"\n")

lista5 = [0,1,4,9,16,25]
lista6 = [36,49,64,81]
lista7 = lista5 + lista6    # Concatenación de 2 listas
print("38-",lista7)
print("39-",36 in lista7) # Sirve para verificar si un elemento está en la lista
print("40-",lista7.index(49)) # Indica el indice que indica en que indice se ubica un elemento especifico
lista7.reverse()    # Sirve para poner una lista al revés
print("42-",lista7*2) # Sirve para copiar n veces los elementos que están en la lista
print("43-",lista7,"\n")

lista8 = [1,2,3,1,1,3,2,3,2,3,1,2,3,1,3,1,2,3,1,3,2,1,3,1,2,3,1,3,1,2,3,1,2,3,2,1,3]
print("46-",lista8)
print("47-",lista8.count(1))  # Sirve para contar cuantas veces está un elemento en la lista
lista8.sort()   # Sirve para organizar númericamente de forma ascendente los elementos de una lista
print("49-",lista8)
lista8.sort(reverse=True)   # Sirve para organizar númericamente de forma descendente los elementos de una lista
print("51-",lista8)

lista8.clear()  # Elimina todos los elementos de una lista. La deja vacía
print("54-",lista8)






