import os
import numpy as np

# Eliminar archivo "OSZICAR_tail" si existe
if os.path.exists("OSZICAR_tail"):
    os.remove("OSZICAR_tail")

# Eliminar archivo "energias.txt" si existe
if os.path.exists("energias.txt"):
    os.remove("energias.txt")

# Carpeta principal
carpeta_principal = "."

# Obtener lista de archivos y directorios
archivos_y_directorios = os.listdir(carpeta_principal)

# Filtrar solo directorios
directorios = [archivo for archivo in archivos_y_directorios if os.path.isdir(os.path.join(carpeta_principal, archivo))]

# Recorrer directorios
for directorio in directorios:
    # Ruta del archivo "OSZICAR"
    ruta_archivo = os.path.join(carpeta_principal, directorio, "OSZICAR")

    # Obtener la última línea del archivo
    ultima_linea = os.popen("tail -n 1 {}".format(ruta_archivo)).read().strip()

    # Abrir archivo "OSZICAR_tail" en modo append
    with open(os.path.join(carpeta_principal, "OSZICAR_tail"), "a") as archivo:
        # Agregar la última línea al archivo
        archivo.write(ultima_linea + "\n")

# Imprimir mensaje de éxito
print("Las últimas líneas de los archivos OSZICAR se han añadido al archivo OSZICAR_tail")




# Abrir archivo en modo lectura
with open(os.path.join(carpeta_principal, "OSZICAR_tail"), "r") as archivo:
    # Leer líneas del archivo
    lineas = archivo.readlines()

# Convertir líneas a vector
vector = np.array(lineas)

# Lista para almacenar energías del archivo actual
energias_archivo = []
energias=[]

# Recorrer líneas
for linea in lineas:
    # Separar la línea por espacios
    linea_separada = linea.split()

    # Obtener la energía (quinta columna)
    energia = linea_separada[4]

    # Agregar la energía a la lista
    energias_archivo.append(energia)

# Convertir lista a vector
energias_archivo = np.array(energias_archivo, dtype=float)

# Agregar las energías del archivo actual a la lista general
energias.extend(energias_archivo)

## Crear archivo con las energías y el nombre del directorio, en dos columnas
# Crear lista con el nombre del directorio repetido tantas veces como energías haya
nombres_directorios = [directorio for directorio in directorios for energia in energias_archivo]
print(directorios)

# Crear archivo con las energías y el nombre del directorio
with open(os.path.join(carpeta_principal, "energias.txt"), "w") as archivo:
    # Recorrer las listas
    for directorios, energia in zip(directorios, energias):
        # Escribir en el archivo
        archivo.write("{}\t{}\n".format(directorios, energia))

# Imprimir mensaje de éxito
print("El archivo 'energias.txt' ha sido creado")

# Imprimir las energías
for i in range(len(energias)):
	print(energias[i])