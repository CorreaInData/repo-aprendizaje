'''
Los tiempos para un curso de Python van desde las 2.5 horas como mínimo, 7 horas como máximo y 4 horas como el promedio.
El curso que estoy viendo en Youtube (Soy Dalto) lo logró en 1.5 horas.

A. Cuanta diferencia hay en porcentaje entre el curso de Dalto y:
    - El más rápido
    - El más lento
    - El promedio
B. Teniendo en cuenta que el tiempo en crudo del promedio de los cursos es de 5 horas (4 con edición) y que el tiempo en
crudo del curso de Dalto es de 3.5 horas (1.5 con edición). Que porcentaje de material inservible se reduce en ambos casos
C. ¿Ver 10 horas del curso a cuantas horas de otros cursos equivale? Y viceversa
'''

# Duraciones de los cursos
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
curso_dalto = 1.5

diferencia_con_min = (1 - curso_dalto / otros_cursos_min) * 100
diferencia_con_max = (1 - curso_dalto / otros_cursos_max) * 100
diferencia_con_prom = (1 - curso_dalto / otros_cursos_prom) * 100

# Tiempos en crudo de los cursos
cursos_crudo_prom = 5
curso_crudo_dalto = 3.5

reduccion_dalto = (1 - curso_dalto / curso_crudo_dalto) * 100
reduccion_prom = (1 - otros_cursos_prom / cursos_crudo_prom) * 100

# Equivalencia en tiempo por cursos
equivalencia_dalto = 1000 * otros_cursos_prom // curso_dalto / 100
equivalencia_prom = 10 * curso_dalto / otros_cursos_prom

print("------------------")

# Diferencia porcentual con los cursos de Dalto (Ejercicio A)
print("El curso de Dalto dura:")
print(f" - un {diferencia_con_min:.5}% menos que el curso más rápido")
print(f" - un {diferencia_con_max:.4}% menos que el curso más lento")
print(f" - un {diferencia_con_prom:.5}% menos que un curso promedio")
print("------------------")

# Reducción de tiempo inservible en los cursos (Ejercicio B)
print(f"El curso de Dalto elimina el {reduccion_dalto:.4}% del tiempo vacio")
print(f"Un curso promedio elimina el {reduccion_prom:.4}% del tiempo vacío")
print("------------------")

print(f"Ver 10 horas del curso de Dalto equivalen a ver {equivalencia_dalto} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivalen a ver {equivalencia_prom} horas del curso de Dalto")






''' La mayoría de veces va a ser mejor mostrar los resultados un nuestro valor, respecto otro valor 
print(f"El curso más rápido tarda un {otros_cursos_min/curso_dalto*100:.5}% más de tiempo que el curso de Dalto")
print(f"El curso más lento tarda un {otros_cursos_max/curso_dalto*100:.5}% más de tiempo que el curso de Dalto")
print(f"Un curso en promedio tarda un {otros_cursos_prom/curso_dalto*100:.5}% más de tiempo que el curso de Dalto")
'''