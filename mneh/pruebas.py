import csv
from ClassUsuario import Usuario
with open('datos.csv','r',encoding='utf-8') as file:

    reader = csv.reader(file)

    for fila in reader:
        obj = Usuario(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])

file.close()