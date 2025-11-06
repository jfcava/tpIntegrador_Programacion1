import os

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
                pass                                
            case "2": # Actualizar datos
                pass
            case "3": # Buscar pais
                pass
            case "4": # Filtrar paises
                pass
            case "5": # Ordenar paises
                pass
            case "6": # Mostrar estadisticas 
                pass
            case "7": # Salir
                print("\nPrograma terminado. Hasta la próxima!")
                break
            case _:
                print("\nLa opción ingresada no es válida. \nPresione Enter para continuar...")
                input()
                limpiar()