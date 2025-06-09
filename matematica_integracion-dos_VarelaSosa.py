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

    # Realizamos las operaciones de conjuntos
    union = set.union(*conjuntos_digitos)
    interseccion = set.intersection(*conjuntos_digitos)
    diferencia_simetrica = set()

    # Calculamos la diferencia simétrica entre todos los pares

    for conjunto1 in range(len(conjuntos_digitos)):
        for conjunto2 in range(conjunto1 + 1, len(conjuntos_digitos)):
            diferencia_simetrica_actual = conjuntos_digitos[conjunto1] ^ conjuntos_digitos[conjunto2]
            for elemento in diferencia_simetrica_actual:
                diferencia_simetrica.add(elemento)

    # Mostramos los resultados

    print(f"Unión: {union}")
    print(f"Intersección: {interseccion}")
    print(f"Diferencia Simétrica: {diferencia_simetrica}")
    print(f"Suma de dígitos por DNI: {sumas_digitos}")
    print(f"Frecuencia de dígitos: {frecuencias_digitos}")

    # Evaluamos la Relación equilibrada entre ambos conjuntos (Compuertas) en base a la expresión lógica elegida.

    for indice_a in range(len(conjuntos_digitos)):
        for indice_b in range(indice_a + 1, len(conjuntos_digitos)):
            conjunto_a = conjuntos_digitos[indice_a]
            conjunto_b = conjuntos_digitos[indice_b]

            # Números compartidos (intersección A ∩ B)
            interseccion = conjunto_a & conjunto_b

            # Números distintos totales (unión A ∪ B)
            union = conjunto_a | conjunto_b

            # Condición: más de 3 compartidos Y al menos 8 distintos
            if len(interseccion) > 3 and len(union) >= 8:
                print(f"\nRelación equilibrada entre DNI {indice_a + 1} y DNI {indice_b + 1}\n")


def main():
    # Bandera para controlar el bucle principal
    bandera = True

    while bandera:
        print("\nBienvenido al programa\n")
        lista_dnis = ingresar_dnis()
        analizar_dnis(lista_dnis)

        # Solicitar opción al usuario para continuar o terminar
        opcion = input("Si querés continuar, ingresa 'S', si no, ingresa 'N' y el programa terminará: ").upper().strip()

        if opcion == "N":
            bandera = False
            print("\nEl programa finalizó.\n")
        elif opcion != "S":
            print("Opción no válida. Por favor, ingresa 'S' o 'N'.")


if __name__ == "__main__":
    main()