import os
import csv

NOMBRE_ARCHIVO = "paises.csv"

def buscar_pais():
    
    while True:
        limpiar()
        print("=== BÚSQUEDA PAÍS ===")
        nombre_pais = input("Ingrese el país a buscar (* para Cancelar): ")

        while es_nombre_vacio(nombre_pais):
            print("\nEl nombre no puede ser vacío.")
            nombre_pais = input("Ingrese el país a buscar (* para Cancelar): ")
            
        if nombre_pais == "*":
            limpiar()
            break

        paises = obtener_paises()
        resultados = []

        for p in paises:
            if nombre_pais.strip().lower() in (p["PAIS"]).strip().lower():
                resultados.append(p)

        if len(resultados) > 0:
            print(f"\nSe encontraron {len(resultados)} resultado(s)")
            print("=========================================")

            for p in resultados:
                print(f"Nombre: {p["PAIS"]}")
                print(f"Población: {p["POBLACION"]} habitantes.")
                print(f"Superficie: {p["SUPERFICIE"]} km²")
                print(f"Continente: {p["CONTINENTE"]}")
                print("================================\n")

            print("\nPresione Enter para continuar...")
            input()
            limpiar()

        else:
            print("\nNo se encontró ninguna coincidencia con la búsqueda.")
            print("Presione Enter para continuar...")
            input()
            limpiar()

def escribir_paisDB(pais): #Agregar un titulo al CSV
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["PAIS", "POBLACION", "SUPERFICIE", "CONTINENTE"])
        escritor.writerow(pais)

def es_numero_positivo(numero):
    
    if numero.isdigit():
        return True
    else:
        return False

def es_nombre_vacio(nombre):
    if nombre == "":
        return True
    else:
        return False

def es_pais_repetido(nombre):
    
    paises_disponibles = obtener_paises()

    for pais in paises_disponibles:
        if nombre.strip().lower() == pais["PAIS"].strip().lower():
            return True
    
    return False

def agregar_pais():
    
    while True:
        limpiar()
        print("=== AGREGAR NUEVO PAÍS ===")

        nombre_pais = input("Nombre del país: ")
        
        # Validar pais repetido
        while es_pais_repetido(nombre_pais):
            print("\nEl país ingresado ya se encuentra en la base de datos. Vuelva a intentarlo.")
            nombre_pais = input("Nombre del país: ")

        # Validar nombre vacio
        while es_nombre_vacio(nombre_pais):
            print("\nEl nombre no puede ser vacío.")
            nombre_pais = input("Nombre del país: ")

        poblacion = input("Población del país: ")

        # Validar numero poblacion
        while not es_numero_positivo(poblacion):
            print("\nSolo se aceptan números positivos. Vuelve a intentarlo.")
            poblacion = input("Población del país: ")

        superficie = input("Superficie del país: ")

        # Validar numero superficie
        while not es_numero_positivo(superficie):
            print("\nSolo se aceptan números positivos. Vuelve a intentarlo.")
            superficie = input("Superficie del país: ")
        
        continente = input("Continente del país: ")

        # Validar continente vacio
        while es_nombre_vacio(continente):
            print("\nEl nombre no puede ser vacío.")
            continente = input("Continente del país: ")

        # Cargar pais

        escribir_paisDB({"PAIS": nombre_pais, "POBLACION": int(poblacion), "SUPERFICIE": int(superficie), "CONTINENTE": continente})
        
        limpiar()
        print("País agregado exitosamente.")
        print("Presione Enter para continuar...")
        input()
        limpiar()
        break

def obtener_paises():
    paises = []
    
    # Si no existe el archivo, lo crea con encabezado
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["PAIS", "POBLACION", "SUPERFICIE", "CONTINENTE"])
            escritor.writeheader()
            return paises
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            paises.append({"PAIS": fila["PAIS"], "POBLACION": int(fila["POBLACION"]), "SUPERFICIE": int(fila["SUPERFICIE"]), "CONTINENTE": fila["CONTINENTE"]})
    
    return paises

def limpiar():
    os.system("cls")

def mostrar_menu():
    menu = [
        "1. Agregar país",
        "2. Actualizar datos",
        "3. Buscar país",
        "4. Filtrar países",
        "5. Ordenar países",
        "6. Mostrar estadísticas",
        "7. Salir"
    ]
    
    while True:
        print("=============================")
        print("===     MENÚ PRINCIPAL    ===")
        print("=============================")
        for opcion in menu:
            print(opcion)
        print("=============================")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1": # Agregar pais
                agregar_pais()                                
            case "2": # Actualizar datos
                pass
            case "3": # Buscar pais
                buscar_pais()
            case "4": # Filtrar paises
                pass
            case "5": # Ordenar paises
                ordenar_paises()
            case "6": # Mostrar estadisticas 
                pass
            case "7": # Salir
                print("\nPrograma terminado. \nHasta la próxima!")
                print()
                break
            case _:
                print("\nLa opción ingresada no es válida. \nPresione Enter para continuar...")
                input()
                limpiar()