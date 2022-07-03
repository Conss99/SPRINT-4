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
        DNI.append([(linea[9])])  # agrega el DNI al array
        NroCheque.append([(linea[0])])
        CodigoBanco.append([linea[1]])
        CodigoScurusal.append([linea[2]])
        NumeroCuentaOrigen.append([linea[3]])
        NumeroCuentaDestino.append([linea[4]])
        Valor.append([linea[5]])
        FechaOrigen.append([linea[6]])
        FechaPago.append([linea[7]])
        TIPO.append([linea[8]])
        Estado.append([linea[10]])

repeticiones = {}


def cheques():
    pantalla = (str(input('Ingrese el DNI: ')))

    for i in enumerate(linea[0]):

        if pantalla in enumerate(linea[9]):
            if linea[0].count(i) > 1:
                print('Se repite el DNI: ', i)
            else:
                print('No se repite el DNI: ', i)

        # print('El valor de la posición {posicion} es {valor}', '\n')

        # if pantalla in linea[9]:
        #     print(f'Existe')
        # else:
        #     print(f'No existe')
        #     break


cheques()

# print(f'El valor de la posición {posicion} es {valor}', '\n')
# print('Número cheque: ', NroCheque[0], '\n')
# print('Codigo del banco: ', CodigoBanco[0], '\n')
# print('Código de la sucursal: ', CodigoScurusal[0], '\n')
# print('Número Cuenta origen: ', NumeroCuentaOrigen[0], '\n')
# print('Número Cuenta destino: ', NumeroCuentaDestino[0], '\n')
# print('Valor: ', Valor[0], '\n')
# print('Fecha de origen: ', FechaOrigen[0], '\n')
# print('Fecha de pago: ', FechaPago[0], '\n')
# print('Tipo: ', TIPO[0], '\n')
# print('DNI: ', DNI[0], '\n')
# print('Estado: ', Estado[0], '\n')
# break

# cheques()

# def validacionDNI():

#     pantalla = (str(input('Ingrese el DNI: ')))
#     for posicion, valor in enumerate(DNI):
#         # print(f'El valor de la posición {posicion} es {valor}')

#         while str(pantalla) in valor:
#             print('DNI correcto')
#             break
#         else:
#             print('DNI incorrecto')
#             break

# validacionDNI()
