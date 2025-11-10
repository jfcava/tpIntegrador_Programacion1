# 🐍 Trabajo Práctico Integrador – Programación I  
**Tema:** Gestión de Países (Python + CSV)

---

## 👥 Integrantes
- **Juan Franco Cavallieri**
- **Julian Rossi**

---

## 📘 Descripción del proyecto
Este trabajo práctico consiste en el desarrollo de una **aplicación de consola en Python** que permite gestionar un conjunto de países con sus principales datos: **nombre, población, superficie y continente**.  

El sistema trabaja con un archivo CSV como base de datos (`paises.csv`) y ofrece distintas funcionalidades de alta, búsqueda, actualización, filtrado, ordenamiento y análisis estadístico, cumpliendo con los lineamientos del TPI integrador de la cátedra.

---

## 📂 Estructura del proyecto

tpiIntegrador_Programacion1/
│
├─ main.py # Programa principal – contiene el menú principal
├─ funciones.py # Archivo con todas las funciones del sistema
├─ paises.csv # Base de datos de países (persistencia en CSV)
└─ README.md # Este documento


---

## ⚙️ Funcionalidades implementadas

| Nº | Función | Descripción |
|----|----------|-------------|
| **1** | **Agregar país** | Permite cargar un nuevo país solicitando nombre, población, superficie y continente. Valida duplicados, campos vacíos y tipos de datos. |
| **2** | **Actualizar país** | Modifica la población y superficie de un país existente. Reescribe el archivo CSV con los cambios. |
| **3** | **Buscar país** | Busca coincidencias parciales o exactas por nombre. Muestra resultados formateados. |
| **4** | **Filtrar países** | Permite filtrar por continente o por rango de población/superficie. Admite rangos abiertos (solo mínimo o máximo). |
| **5** | **Ordenar países** | Ordena la lista por nombre, población o superficie en forma ascendente o descendente. |
| **6** | **Mostrar estadísticas** | Calcula y muestra: país con mayor y menor población, promedios de población y superficie, y cantidad de países por continente. |
| **7** | **Salir** | Cierra el programa guardando los cambios. |

---

## 🧩 Validaciones realizadas
- No se permiten **campos vacíos**.  
- La **población** debe ser un número entero **≥ 0**.  
- La **superficie** debe ser un número entero **> 0**.  
- No se pueden cargar países **repetidos**.  
- Se manejan errores de lectura/escritura del CSV.  
- Se evita el uso de **expresiones lambda**, cumpliendo con las restricciones del TPI.

---

## 🧠 Conceptos aplicados
- **Estructuras de datos:** listas y diccionarios.  
- **Control de flujo:** bucles `for`, condicionales `if`, estructuras de menú con `while True`.  
- **Funciones:** definición modular para cada caso del menú.  
- **Manejo de archivos:** lectura y escritura de archivos CSV con el módulo `csv`.  
- **Validaciones y manejo de errores:** control de entrada del usuario.  
- **Persistencia de datos:** almacenamiento permanente en `paises.csv`.

---

## ▶️ Ejecución del programa

---

### Requisitos
- Python **3.x** instalado.

---

### Pasos
1. Descargar el proyecto o clonarlo desde GitHub:
   ```bash
   git clone https://github.com/<usuario>/<repositorio>.git
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el programa:
   python main.py
4. Seguir las instrucciones del menú en consola.

---

### 📈 Ejemplo de uso

===== Gestión de Países =====
1) Agregar país
2) Actualizar país (población y superficie)
3) Buscar por nombre
4) Filtrar por continente o rango
5) Ordenar (nombre/población/superficie)
6) Mostrar estadísticas
7) Salir

Ejemplo de salida de estadísticas:

=========== ESTADÍSTICAS ===========
- País con mayor población: Brasil (213993437)
- País con menor población: Uruguay (3473730)
- Promedio de población: 88,321,543.50
- Promedio de superficie: 3,126,952.75
- Cantidad de países por continente:
  · América: 5
  · Europa: 3
  · Asia: 2
  
====================================

---

### 🧾 Entregables

- main.py y funciones.py correctamente comentados.
- paises.csv con datos de ejemplo.
- README.md con descripción y guía de uso.
- Video explicativo (10–15 min):
  - Presentación del grupo
  - Demostración de cada caso del menú
  - Explicación breve del código
  - Conclusión final

---

### 🎥 Video sugerido

- Mostrar el programa ejecutándose en consola.
- Mostrar el código fuente en VS Code.
- Explicar brevemente las estructuras usadas y validaciones.
- Cierre mencionando la experiencia y los aprendizajes.

---

### 🧾 Conclusión del grupo

El trabajo permitió aplicar todos los contenidos de la materia, integrando manejo de archivos, estructuras de datos, modularización de funciones y control de errores.
Además, fortaleció la práctica de trabajo colaborativo con Git y GitHub, simulando un entorno real de desarrollo.

---

### 📅 Versión

v1.0 – Noviembre 2025
Proyecto desarrollado para la cátedra Programación I, UTN.
