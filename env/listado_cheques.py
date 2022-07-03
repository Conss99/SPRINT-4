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
v = []


with open('env/csv/cheques_generales.csv', "r") as file:
    lineas = file.read().splitlines()
    lineas.pop(0)

    for l in lineas:
        v = NroCheque, CodigoBanco, CodigoScurusal, NumeroCuentaOrigen, NumeroCuentaDestino, Valor, FechaOrigen, FechaPago, TIPO, DNI, Estado = l.split(
            ';')
        v.append(NroCheque)
        v.append(CodigoBanco)
        v.append(CodigoScurusal)
        v.append(NumeroCuentaOrigen)
        v.append(NumeroCuentaDestino)
        v.append(Valor)
        v.append(FechaOrigen)
        v.append(FechaPago)
        v.append(TIPO)
        v.append(DNI)
        v.append(Estado)
