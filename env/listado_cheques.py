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

NroCheque = []
CodigoBanco = []
CodigoScurusal = []
NumeroCuentaOrigen = []
NumeroCuentaDestino = []
Valor = []
FechaOrigen = []
FechaPago = []
TIPO = []
DNI = []
Estado = []

with open('env/csv/cheques_generales.csv', "r") as file:
    lineas = file.read().splitlines()
    lineas.pop(0)
    for l in lineas:
        linea = l.split(';')
        DNI.append([int(linea[9])])  # agrega el DNI al array
        NroCheque.append([int(linea[0])])
        CodigoBanco.append([linea[1]])
        CodigoScurusal.append([linea[2]])
        NumeroCuentaOrigen.append([linea[3]])
        NumeroCuentaDestino.append([linea[4]])
        Valor.append([linea[5]])
        FechaOrigen.append([linea[6]])
        FechaPago.append([linea[7]])
        TIPO.append([linea[8]])
        Estado.append([linea[10]])


def cheques():
    print('Número cheque: ', NroCheque, '\n')
    print('Codigo del banco: ', CodigoBanco, '\n')
    print('Código de la sucursal: ', CodigoScurusal, '\n')
    print('Número Cuenta origen: ', NumeroCuentaOrigen, '\n')
    print('Número Cuenta destino: ', NumeroCuentaDestino, '\n')
    print('Valor: ', Valor, '\n')
    print('Fecha de origen: ', FechaOrigen, '\n')
    print('Fecha de pago: ', FechaPago, '\n')
    print('Tipo: ', TIPO, '\n')
    print('DNI: ', DNI, '\n')
    print('Estado: ', Estado, '\n')


cheques()

# digitosDNI = []

# for elem in sorted(DNI):
#     digitosDNI.append(elem[0])  # agrega los digitos del DNI a una lista
# print(' Cantidad de digitos del DNI: ')
# print(len(str(digitosDNI[2])))
# # muestra la cantidad de digitos del segundo DNI de la lista
