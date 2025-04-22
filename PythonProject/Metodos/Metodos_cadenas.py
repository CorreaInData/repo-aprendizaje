'''
La diferencia entre método y función es que
METODO: variable.metodo() ó variable.metodo(parámetro)
FUNCIÓN: funcion(variable)
¡¡¡LAS FUNCIONES SIEMPRE VAN A DEVOLVER TEXTOOOS!!!
'''

cadena1 = "Hola soy Sebastian"
cadena2 = "Bienvenido maquinola"

# Convierte en mayusculas
mayus = cadena1.upper()

# Convierte en minúsculas
minus = cadena1. lower()

# Primera letra en mayúsculas
primera_mayus = cadena1.capitalize()    # Convierte t0do en minúsculas y luego la primera en mayúscula

# Buscar una cadena en otra cadena
busqueda_find = cadena1.find("soy")    # Devuelve la posición en dónde se encuentra el parámetro. Si no hay coincidencia, devuelve un -1

# Buscar una cadena en otra cadena
busqueda_index = cadena1.index("Hola")  # Devuelve la posición en dónde se encuentra el parámetro. Si no hay coincidencia, devuelve error

# Si es númerico devuelve True, si no devuelve false
es_numerico = cadena1.isnumeric()   # Así sea un texto con números, lo va a marcar como verdadero

# Si es alfanúmerico devuelve True, si no devuelve false
es_alfanumerico = cadena1.isalpha() # Solo si son letras de la A a la Z sin caracteres especiales, marcará True

# Cuenta cuantos caracteres tiene una cadena
contar_coincidencias = cadena1.count("a")  # Devuelve el número de coincidencias

# Verifica si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith("Hola")    # Texto literal (tal cual)

# Verifica si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith("n") # Texto literal (tal cual)

# Reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("la","lu")   # Reemplaza el primer párametro por el segundo, si no encuentra coincidencia, devuelve el primer valor

# Separar cadenas por el caracter que le indiquemos. Devuelve una lista
cadena_separada = cadena1.split(" ")

print(cadena_separada)