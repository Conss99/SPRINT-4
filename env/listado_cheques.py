# with open('env/csv/cheques_generales.csv', "r") as file_object:
#     lectura = file_object.readline().split(',')

#     for i in range(len(lectura)):
#         lectura[i] = lectura[i].split()
# print(lectura[2])

# import csv

# with open('env/csv/cheques_generales.csv', "r") as file:  # abre el archivo
#     fileCSV = csv.reader(file)  # lee el archivo
#     next(fileCSV)  # salta el encabezado
#     for row in fileCSV:  # recorre el archivo
#         print(row)

# def cheques():
#     for l in lineas:
#         linea = l.split(';')

#         nroCheque = linea[0]
#         CODbanco = linea[1]
#         CODSUCURSAL = linea[2]
#         NCTAOrigen = linea[3]
#         NCTADest = linea[4]
#         Valor = linea[5]
#         FechaOrgi = linea[6]
#         FecPago = linea[7]
#         Tipo = linea[8]
#         DNI = linea[9]
#         Estado = linea[10]

#         print(nroCheque, CODbanco, CODSUCURSAL, NCTAOrigen,
#               NCTADest, Valor, FechaOrgi, FecPago, Tipo, DNI, Estado)

import csv

nroCheque = []
CODbanco = []
CODSUCURSAL = []
NCTAOrigen = []
NCTADest = []
Valor = []
FechaOrgi = []
FecPago = []
Tipo = []
DNI = []
Estado = []

with open('env/csv/cheques_generales.csv', "r") as file:
    lineas = file.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea = l.split(';')
        DNI.append([int(linea[9])])  # agrega el DNI al array


digitosDNI = []

for elem in sorted(DNI):
    digitosDNI.append(elem[0])  # agrega los digitos del DNI a una lista
print(' Cantidad de digitos del DNI: ')
print(len(str(digitosDNI[2])))
