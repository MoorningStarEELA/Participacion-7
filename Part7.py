from collections import Counter

print("El texto a leer: ")
# Leer, abrir y mostrar el texto seleccionado

with open("Gullivers_Travels.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
    contador = Counter(contenido)
carac_ordernar = sorted(contador.items(), key=lambda x: x[1], reverse=True)# El parámetro key se establece como lambda x: x[1], 
#lo que significa que se esta ordenando, basandose en el segundo elemento de cada tupla (que es la frecuencia)

# reverse=True se utiliza para ordenar en orden descendente, de mayor a menor frecuencia.

# Contar los caracteres del texto
num_carac = len(contenido)
print("\nNumero de caracteres en el texto son:", num_carac)

# Crear y escribir en el archivo de salida
with open("salida.txt", "w") as salida:
    salida.write("Numero de caracteres en el texto son: " + str(num_carac) + "\n\n")
    salida.write("Caracter : frecuencia\n")
    for caracter, frecuencia in carac_ordernar:
        salida.write(f"{caracter}:{frecuencia}\n")

print("Se ha guardado en 'salida.txt'")
