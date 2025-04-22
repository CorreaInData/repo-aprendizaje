# Operadores Aritméticos

num1 = 10
num2 = 3

rsum = num1 + num2
rres = num1 - num2
rmul = num1 * num2
rdiv = num1 / num2
rdiv2 = num1 // num2    # División redondeado hacia abajo
rmod = num1 % num2     # Módulo
rexp = num1 ** num2     # Potenciación

print("El resultado de la suma es: ",rsum)
print("El resultado de la resta es: ",rres)
print("El resultado de la multiplicación es: ",rmul)
print("El resultado de la división es: ",rdiv)
print("El resultado de la división entera es: ",rdiv2)
print("El residuo de la división es: ",rmod)    # Residuo de la división
print("El resultado de la potenciación es: ",rexp)

'''
Python respeta la jerarquía de las operaciones a la hora de realizar sus operaciones aritméticas es decir,
da prioridad en este orden: paréntesis, potenciación, división, multiplicación, módulo, suma y resta.
'''

print("")

# Ejmplo. Se quiere realizar la siguiente operación aritmética: 3^3 * (13/5 - (2*4))

operacion = 3 ** 3 * (13 / 5 - (2 * 4))

print(operacion)
print("")

# Operadores Relacionales

resultado = 10 < 20
print(resultado)
print("")

'''
Los operadores relacionales son los siguientes:
Mayor que: >
Menor que: <
Mayor o igual que: >=
Menor o igual que: <=
Igualdad: ==
Diferencia: !=
'''

# Operaciones aritmeticas con operaciones relacionales

a = 10
b = 20
c = 30

respuesta = a+b == c

print("- Resultado operación: ",respuesta)
print("")

# Operadores lógicos

'''
Son tres operadores: and, or, not. Y permiten obtener como resultados booleanos (True o False)
Su prioridad es: not, and, or. 

Nota: 'not' cambia las expresiones a su contraparte (T -> F o F -> T)
'and' en sus operaciones basta con haber un false en la operación, para que su resultado sea false (multiplicación lógica). 
'or' en sus operaciones basta con haber un true en la operación, para que su resultado sea true (suma lógica). 
'''

q = 10
w = 12
e = 13
r = 10

t = ((q>w)or(q<e))and((q==e)or(q>=w))

print("- Resultado operación lógica : ",t)
print("")

'''
La prioridad general de los operadores es:
1. ()
2. **
3. *,/,%,not
4. +,-,and
5. >,<,==,>=,<=,!=,or
'''

p = 10
i = 15
o = 20

ejemplo = not((p<i)and(i<o))
print("- El resultado del ejemplo es: ",ejemplo)
print("")

# Operadores de asignación

g = 3   # Para usar los operadores de asignación, siempre hay que declarar y asignar una variable a la que se pueda operar
print("Variable original: ",g)
g += 5
print("Suma en asignación: ",g)
g -= 2
print("Resta en asignación: ",g)
g *= 5
print("Multiplicación en asignación: ",g)
g /= 3
print("División en asignación: ",g)
g **= 2
print("Potencia en asignación; ",g)
g %= 9
print("Módulo en asignación: ",g)


