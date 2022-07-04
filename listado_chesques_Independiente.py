import csv
from datetime import datetime

''' Variables Globales '''
PANTALLA = False
CSV = False
i_ncheque = 0
i_ncuenta = 4
i_fecha = 6
i_DNI = 8
i_tipo = 9
i_estado = 10
hoy = datetime.now()
hoy = hoy.strftime("%d-%m-%Y-(%H-%M)")

# Debugging
# salida = '0'
# opcion = '1'

'''---------------------------------------------------------------- Funciones------------------------------------------------'''
def revision(DNI, list):
    for i in range(1, len(list)):
            if datos[i][i_DNI] == DNI and datos[i][i_ncheque] == datos[i+1][i_ncheque] and datos[i][i_ncuenta] == datos[i+1][i_ncuenta]:
                print('Error: Numero de Cheque de Misma Cuenta repetido')

    
def crudo(DNI):
    for i in range(1, len(datos)):
            if datos[i][i_DNI] == DNI:
                lista.append(datos[i])
                # print(datos[i])
    return lista


def filtros(DNI):
    print('\nQue filtros desea usar? \nOpciones: Tipo de Cheque: 0 / Estado de Cheque: 1') #  / Rango de Fecha: 2
    opcion = input('Opcion: ')
    
    if opcion == '0':
        print('\nTipo de Cheque? \nOpciones: EMITIDO: 0 / DEPOSITADO: 1')
        val_cheque = input('Opcion: ')
        
        for i in range(1, len(datos)):
            if val_cheque == '0' and datos[i][i_tipo] == 'EMITIDO' and datos[i][i_DNI] == DNI:
                lista.append(datos[i])

            elif val_cheque == '1' and datos[i][i_tipo] == 'DEPOSITADO' and datos[i][i_DNI] == DNI:
                lista.append(datos[i])
            
            elif val_cheque != '0' and val_cheque != '1':
                print('Error: Opcion invalida')
                exit(1)
        
    elif opcion == '1':
        print('\nEstado de Cheque? \nOpciones: PENDIENTE: 0 / APROBADO: 1 / RECHAZADO: 2 ')
        val_cheque = input('Opcion: ')
        
        for i in range(1, len(datos)):
            if val_cheque == '0' and datos[i][i_estado] == 'PENDIENTE' and datos[i][i_DNI] == DNI:
                lista.append(datos[i])
             
            elif val_cheque == '1' and datos[i][i_estado] == 'APROBADO' and datos[i][i_DNI] == DNI:
                lista.append(datos[i])
            
            elif val_cheque == '2' and datos[i][i_estado] == 'RECHAZADO' and datos[i][i_DNI] == DNI:
                    lista.append(datos[i])
            
            elif val_cheque != '0' and val_cheque != '1' and val_cheque != '3':
                print('Error: Opcion invalida')
                exit(1)
        
    revision(DNI, lista)
    return lista
    
    # elif opcion == '2':
    #     print('\nFecha de Inicio? \n Formato: xx-xx-xxxx (dia-mes-año)')
    #     fecha1 = input('Opcion: ')
    #     print('\nFecha Final? \n Formato: xx-xx-xxxx (dia-mes-año)')
    #     fecha2 = input('Opcion: ')
        
    #     for i in range(1, len(datos)):
    #         if  fecha1 < datos[i][i_fecha] < fecha2 and datos[i][i_DNI] == str(DNI):
    #             lista.append(datos[i])
    #         else:   print('No hay datos registrados en ese rango')
                
    #     return lista


archivo = input('Nombre de Archivo: ')
# archivo = 'test_itbank.csv'
with open(archivo) as archivo:
    lector = csv.reader(archivo)
    datos = list(lector)
    
lista = []

DNI_Cliente =  input('DNI buscado: ')
# DNI_Cliente = 1617591371
# if int(DNI_Cliente) > 11:
#     print('Error: DNI demasiado largo')
#     exit(1)
    
DNI_Cliente = str(DNI_Cliente)

print('\nSalida? \nOpciones: PANTALLA: 0 / CSV: 1')
salida = input('Opcion: ')
if salida == '0':
    PANTALLA = True
elif salida == '1':
    CSV = True
else:
    print('Error: Salida no seleccionada / no existente')
    exit(1)


print('\nFormato? \nOpciones: Ver todos los registros: 0 / Filtrar: 1')
opcion = input('Opcion: ')
if opcion == '0':
    res = crudo(DNI_Cliente)
elif opcion == '1':
    res = filtros(DNI_Cliente)
else:
    print('Error: No se eleigio una opcion posible.')
    exit(1)


if PANTALLA:
    print(datos[0])
    for i in range(len(res)):
        print(res[i])
    if len(res) == 0:
        print('Lista vacia: DNI No registrado')
elif CSV:
    new_file = '{}-{}.csv'.format(DNI_Cliente,hoy)
    with open(new_file, 'w') as csv_file:
        planilla = csv.writer(csv_file)
        planilla.writerow(datos[0])
        for i in range(len(lista)):
            planilla.writerow(lista[i])

archivo.close()