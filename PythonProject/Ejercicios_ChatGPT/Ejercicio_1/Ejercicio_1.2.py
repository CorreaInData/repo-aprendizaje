'''
Suponiendo que cada persona en promedio habla 2 palabras por segundo:

A. Pedirle al usuario que diga cualquier texto real y:
    - Calcular cuánto tiempo tardaría en decir la frase
    - Cuántas palabras fue que dijo
B. Si se tarda más de un minuto, decirle "Pará flaco, tampoco te pedí un testamento".
C. Si Dalto habla un 30% más rápido ¿cuánto tiempo tardaría en decirlo?
'''

texto = input("Mister, dime una frase y te calculo cuanto tiempo tardarías si tuvieras que decirla: ")

palabras = len(texto.split())
print("----------------")

if palabras > 120:
    print("Pará flaco, tampoco te pedí un testamento")
else:
    print(f"Mister esa frase te demorarías {palabras*0.5} segundos en decirla")
    print(f"Y en total dijiste {palabras} palabras")
    print("----------------")
    print(f"Si Dalto dijera esa misma frase, tardaría {palabras * 0.5 * 0.7} segundos en decirla")



