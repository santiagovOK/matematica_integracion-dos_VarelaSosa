from datetime import date

def ingresar_dnis():
    
    pregunta = input("Querés ingresar tus DNIs (I) o usamos los de ejemplo (E)? Responde con I o E: ").upper().strip()

    if pregunta == "E":
        lista_dnis = ["26931802","28389594"]
    elif pregunta == "I":
        lista_dnis = input("Ingresá los DNIs separados por coma, sin espacios y sin puntos: ").split(",")
    else:
        print("Opción no válida. Usando DNIs de ejemplo.")
        lista_dnis = ["26931802","28389594"]

    # Imprimimos la lista de DNIs ingresados
    print("\nDNIs ingresados: ", lista_dnis, "\n")

    return lista_dnis

def contar_frecuencia_digitos(dni):
    # Creamos un diccionario para almacenar frecuencias de cada dígito
    frecuencias = {}
    for digito in dni:
        if digito in frecuencias:
            frecuencias[digito] += 1
        else:
            frecuencias[digito] = 1
    return frecuencias

# Convertimos el DNI a conjunto de dígitos únicos
def obtener_digitos_unicos(dni):
    return set(dni)

""" 

Agregar la función bubble_sort() que usamos para el programa de programación I, así ordenamos los resultados de unión, intersección, diferencia simétrica, etc.)

"""

def bubble_sort(lista):
    # Obtenemos la longitud de la lista.
    longitud = len(lista)
    # Establecemos un bucle for para iterar sobre la lista. 
    # El rango será la longitud de la lista, por más que el ordenamiento se complete antes. Sino deberíamos usar `break` y es mala práctica.
    for pasada in range(longitud):
        # Realizamos las comparaciones y los intercambios necesarios en la lista para ordenarla.
        for i in range(0, longitud - pasada - 1):
            # Comparamos los elementos adyacentes y los intercambiamos si están en el orden incorrecto.
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    # Retornamos la lista ordenada.
    return lista

def analizar_dnis(lista_dnis):
    # Establecemos listas vacías para almacenar los datos posteriores
    conjuntos_digitos = []
    frecuencias_digitos = []
    sumas_digitos = []

    # Procesamos cada DNI para las operaciones
    for dni in lista_dnis:
        conjunto = obtener_digitos_unicos(dni)
        conjuntos_digitos.append(conjunto)
        frecuencias_digitos.append(contar_frecuencia_digitos(dni))
        suma = sum(int(digito) for digito in dni)
        sumas_digitos.append(suma)

    # Realizamos las operaciones de conjuntos a la vez que ordenamos los resultados con bubble_sort
    union = bubble_sort(list(set.union(*conjuntos_digitos)))
    interseccion = bubble_sort(list(set.intersection(*conjuntos_digitos)))

    # Inicializamos la diferencia simétrica como un conjunto vacío
    diferencia_simetrica = set()

    # Calculamos la diferencia simétrica entre todos los pares
    for conjunto1 in range(len(conjuntos_digitos)):
        for conjunto2 in range(conjunto1 + 1, len(conjuntos_digitos)):
            diferencia_simetrica_actual = conjuntos_digitos[conjunto1] ^ conjuntos_digitos[conjunto2]
            for elemento in diferencia_simetrica_actual:
                diferencia_simetrica.add(elemento)

    # Ordenamos la diferencia simétrica con bubble_sort
    diferencia_simetrica = bubble_sort(list(diferencia_simetrica))

    # Mostramos los resultados
    print(f"Unión: {union}")
    print(f"Intersección: {interseccion}")
    print(f"Diferencia Simétrica: {diferencia_simetrica}")
    print(f"Suma de dígitos por DNI: {sumas_digitos}")
    print(f"Frecuencia de dígitos: {frecuencias_digitos}")


    # Evaluamos la Relación equilibrada entre pares de conjuntos de dígitos en base a la expresión lógica elegida.
    print("\nEvaluación de la condición lógica (expresión lógica sobre relaciones equilibradas) entre los conjuntos de dígitos: ")

    # Calculamos la intersección: dígitos compartidos por ambos DNIs
    for indice_a in range(len(conjuntos_digitos)):
        # Iteramos sobre los conjuntos restantes para comparar con el conjunto actual
        for indice_b in range(indice_a + 1, len(conjuntos_digitos)):
            conjunto_a = conjuntos_digitos[indice_a]
            conjunto_b = conjuntos_digitos[indice_b]

            # Calculamos la intersección: dígitos compartidos por ambos DNIs (intersección A ∩ B)
            interseccion = conjunto_a & conjunto_b

            # Calculamos la unión: todos los dígitos distintos entre ambos DNIs (unión A ∪ B)
            union = conjunto_a | conjunto_b

            # Establecemos una condición para una relación equilibrada: más de 3 compartidos Y al menos 8 distintos
            if len(interseccion) > 3 and len(union) >= 8:
                print(f"\nRelación equilibrada entre DNI {indice_a + 1} y DNI {indice_b + 1}\n")
            else:
                print(f"\nNo hay relación equilibrada entre DNI {indice_a + 1} y DNI {indice_b + 1}\n")

def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 != 0 or anio % 400 == 0:
            return True
    return False

def analizar_anios():
    entrada = input("Ingrese los años de nacimiento separados por coma (sin espacios): ").split(",")
    lista_anios = []

    # Convertimos las cadenas (cada año ingresado) a enteros
    for a in entrada:
        lista_anios.append(int(a))

    print("Años ingresados:", lista_anios)

    # Almancenamos en variables los resultados de las funciones
    todos_despues_2000 = True
    alguno_bisiesto = False

    # Recorremos la lista de años para verificar las condiciones
    for anio in lista_anios:
        if anio <= 2000:
            todos_despues_2000 = False
        if es_bisiesto(anio):
            alguno_bisiesto = True

    # Imprimimos los resultados según las condiciones
    # Si todos los años son mayores a 2000, imprimimos "Grupo Z"
    if todos_despues_2000:
        print("Grupo Z")

    # Si alguno de los años es bisiesto, imprimimos "Tenemos un año especial"
    if alguno_bisiesto:
        print("Tenemos un año especial")

    # Calculamos las edades de las personas nacidas en los años ingresados
    
    # Obtenemos el año actual con date.today().year
    anio_actual = date.today().year
    # Calculamos las edades restando el año actual a cada año de nacimiento
    edades = [anio_actual - anio for anio in lista_anios]

    print("Edades calculadas:", edades)

    # Calculamos el producto cartesiano entre los años y las edades
    print("Producto cartesiano (año × edad):")
    for anio in lista_anios:
        for edad in edades:
            print(f"({anio}, {edad})")

def main():
    # Bandera para controlar el bucle principal
    bandera = True

    # Bucle principal del programa
    while bandera:
        # Mostramos el mensaje de bienvenida
        print("\nBienvenido al programa\n")
        # Llamamos a la función para ingresar los DNI
        lista_dnis = ingresar_dnis()
        # Llamamos a la función para analizar los DNI
        analizar_dnis(lista_dnis)
        # Llamamos a la función para analizar los años de nacimiento
        analizar_anios()


        # Solicitar opción al usuario para continuar o terminar
        opcion = input("Si querés continuar, ingresa 'S', si no, ingresa 'N' y el programa terminará: ").upper().strip()

        if opcion == "N":
            bandera = False
            print("\nEl programa finalizó.\n")
        elif opcion != "S":
            print("Opción no válida. Por favor, ingresa 'S' o 'N'.")


if __name__ == "__main__":
    main()