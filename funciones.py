import os
import csv

NOMBRE_ARCHIVO = "paises.csv"


def ordenar_por_opcion(opc, orden):
    
    paises = obtener_paises()
    numero_paises = len(paises)

    match opc:
        case 1: # Ordenar por nombre
            
            opcion = "PAIS"

            if orden == True:
                for i in range(numero_paises - 1):
                    for j in range(i+1, numero_paises):
                        if paises[i][opcion].lower() > paises[i+1][opcion].lower():
                            paises[i], paises[j] = paises[j],paises[i]
            else:
                for i in range(numero_paises - 1):
                    for j in range(i+1, numero_paises):
                        if paises[i][opcion] < paises[i+1][opcion]:
                            paises[i], paises[j] = paises[j],paises[i]    
            
            return paises
        
        case 2: # Ordenar por poblacion
            opcion = "POBLACION"
        case 3: # Ordenar por superficie
            opcion = "SUPERFICIE"
    
    if opcion == "POBLACION" or opcion == "SUPERFICIE":
        if orden == True:
            for i in range(numero_paises - 1):
                for j in range(i+1, numero_paises):
                    if paises[i][opcion] > paises[i+1][opcion]:
                        paises[i], paises[j] = paises[j],paises[i]
        else:
            for i in range(numero_paises - 1):
                for j in range(i+1, numero_paises):
                    if paises[i][opcion] < paises[i+1][opcion]:
                        paises[i], paises[j] = paises[j],paises[i]    
        
        return paises

def ordenar_paises():
    
    while True:    
        limpiar()
        print("=== ORDENAR PAÍSES ===")
        print("1. Por nombre")
        print("2. Por población")
        print("3. Por superficie")
        print("\n4. Volver al menú anterior")


        opcion = input("\nSeleccione una opción: ").strip()

        match opcion:
            case "1": # Ordenar por nombre
                
                orden_ascendente = True
                opcion = 1
                
                while True:
                    
                    paises_ordenados = ordenar_por_opcion(opcion, orden_ascendente)

                    if orden_ascendente == True:
                        orden = "Ascendente"
                    else:
                        orden = "Descendente"

                    limpiar()
                    print("=========================================")
                    print(f"====== PAÍSES ORDENADOS POR NOMBRE ======")
                    print("=========================================")
                    print(f"Orden: {orden}\n")

                    for i, p in enumerate(paises_ordenados):
                        print(f"{i+1}. {p["PAIS"]}")
                    
                    print("\n=== MENÚ ===")
                    print("1. Invertir orden")
                    print("2. Volver al menú anterior")
                    opcion_menu = input("\nOpción: ")

                    while opcion_menu not in ("12"):
                        print("\nOpción incorrecta. Vuelva a intentarlo.")
                        print("\n=== MENÚ ===")
                        print("1. Invertir orden")
                        print("2. Volver al menú anterior")
                        opcion_menu = input("\nOpción: ")
                    
                    if opcion_menu == "1":
                        if orden_ascendente == True:
                            orden_ascendente = False
                        else:
                            orden_ascendente = True
                        continue

                    else:
                        limpiar()
                        break


            case "2": # Ordenar por poblacion
                
                orden_ascendente = True           
                opcion = 2
                
                while True:
                    
                    paises_ordenados = ordenar_por_opcion(opcion, orden_ascendente)

                    if orden_ascendente == True:
                        orden = "Ascendente"
                    else:
                        orden = "Descendente"

                    limpiar()
                    print("========================================")
                    print(f"==== PAÍSES ORDENADOS POR POBLACIÓN ====")
                    print("========================================")
                    print(f"Orden: {orden}\n")
                    
                    for i, p in enumerate(paises_ordenados):
                        print(f"{i+1}. {p["PAIS"].upper()}")
                        print(f"-- Población: {p["POBLACION"]} habitantes.")
                    
                    print("\n=== MENÚ ===")
                    print("1. Invertir orden")
                    print("2. Volver al menú anterior")
                    opcion_menu = input("\nOpción: ")

                    while opcion_menu not in ("12"):
                        print("\nOpción incorrecta. Vuelva a intentarlo.")
                        print("\n=== MENÚ ===")
                        print("1. Invertir orden")
                        print("2. Volver al menú anterior")
                        opcion_menu = input("\nOpción: ")
                    
                    if opcion_menu == "1":
                        if orden_ascendente == True:
                            orden_ascendente = False
                        else:
                            orden_ascendente = True
                        continue

                    else:
                        limpiar()
                        break

            case "3": # Ordenar por superficie

                orden_ascendente = True           
                opcion = 3

                while True:
                    
                    paises_ordenados = ordenar_por_opcion(opcion, orden_ascendente)

                    if orden_ascendente == True:
                        orden = "Ascendente"
                    else:
                        orden = "Descendente"

                    limpiar()
                    print("========================================")
                    print(f"=== PAÍSES ORDENADOS POR SUPERFICIE ===")
                    print("========================================")
                    print(f"Orden: {orden}\n")
                    
                    for i, p in enumerate(paises_ordenados):
                        print(f"{i+1}. {p["PAIS"].upper()}")
                        print(f"-- Superficie: {p["SUPERFICIE"]} kms²")
                    
                    print("\n=== MENÚ ===")
                    print("1. Invertir orden")
                    print("2. Volver al menú anterior")
                    opcion_menu = input("\nOpción: ")

                    while opcion_menu not in ("12"):
                        print("\nOpción incorrecta. Vuelva a intentarlo.")
                        print("\n=== MENÚ ===")
                        print("1. Invertir orden")
                        print("2. Volver al menú anterior")
                        opcion_menu = input("\nOpción: ")
                    
                    if opcion_menu == "1":
                        if orden_ascendente == True:
                            orden_ascendente = False
                        else:
                            orden_ascendente = True
                        continue

                    else:
                        limpiar()
                        break
                    
            case "4": # Volver al menu
                limpiar()
                break
            case _:
                print("\nLa opción ingresada no es válida. \nPresione Enter para continuar...")
                input()
                limpiar()

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