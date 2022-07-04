import csv
import re
import sys
from datetime import datetime


class Filtro_cheque:
     def __init__(self,nom_csv,dni,salida,tipo,estado,fecha):
        self.nombreArchivo = nom_csv
        self.dni = dni
        self.salida = salida
        self.tipo = tipo
        self.estado = estado
        self.fecha= fecha
     
        pass

def separar_fechas(cadena):
     
        f_origen =  ''
        f_pago = ''
        i = 1
        for car in str(cadena):
            if car == ':':
                i +=1
            else:
                if i == 1:
                    f_origen += car
                else:
                    f_pago += car
        
        
        return f_origen , f_pago

def validar_argumentos(argumentos):
#Valida los parametros ingresados por la terminal    
    if  1000000 > int(argumentos[2]) >= 100000000 :
        sys.exit(1)

    if not argumentos[3].upper == "PANTALLA" and  argumentos[3].upper =="CSV":
        sys.exit(1)

    if not argumentos[4].upper == 'EMITIDO' and argumentos[4].upper == 'DEPOSITADO':
        sys.exit(1)

    if len(argumentos) == 5:
        argumentos.append("0")
        argumentos.append("0")
    else:
        if len(argumentos) == 6:
           
            if not  argumentos[5].upper  != "PENDIENTE" and argumentos[5].upper  != "APROBADO" and argumentos[5].upper != "RECHAZADO":
                   
                    sys.exit(1)  
            else:
                               
                argumentos.append("0")   
        else:    
                if len(argumentos) == 7:
                
                    busqueda = re.search('\d{2}-\d{2}-\d{4}:\d{2}-\d{2}-\d{4}',argumentos[6])
                         
                    if busqueda == None :
                        sys.exit()
                    
def nro_repetido(lista):
    bandera = False
    nro_che = []
    nro_cuenta = []
    for j in lista:   
        
        nro_che.append((j[0]))
        nro_cuenta.append((j[3]))
    
    for i in range(0, len(nro_cuenta)):
        for j in range(0, len(nro_che)):
            if i != j:
                if nro_cuenta[i] == nro_cuenta[j] and nro_che[i] == nro_che[j]:
                    bandera = True
                   
                    return bandera
    
    return bandera

def leer_archivo(nom, dni ):
    lista = []

    with open(nom, "r") as file:
        lineas = file.read().splitlines()
        lineas.pop(0)
        
        for l in lineas:
            v = []
            nroCheque, codbanco, codSucursal, nCtaOrigen,nCtaDest,Valor,FechaOrigen,FechaPago,Dni,Tipo,Estado = l.split(",")
            
            if Dni == dni:
             
               v.append(nroCheque)
               v.append(codbanco)
               v.append(codSucursal)
               v.append(nCtaOrigen)
               v.append(nCtaDest)
               v.append(Valor)
               v.append(FechaOrigen)
               v.append(FechaPago)
               v.append(Dni)
               v.append(Tipo)
               v.append(Estado)
               lista.append(v)
              

     
    return lista

def to_string_encabezado():
    print('-'*170)
    r = ''    
    r += '{:<15}|'.format(('Nro Cheque'))
    r += '{:<15}|'.format(('Cod Banco'))
    r += '{:<15}|'.format(('Cod Sucursal'))
    r += '{:<15}|'.format(('Cuenta Origen'))
    r += '{:<15}|'.format(('Cuenta Destino'))
    r += '{:15}|'.format(("Valor"))
    r += '{:<15}|'.format("Fecha Origen")
    r += '{:<15}|'.format("Fecha Pago")
    r += '{:<10}|'.format(str("Dni"))
    r += '{:<10}|'.format("Tipo")
    r += '{}'.format("Estado")
    print(r)

def to_string(Cheque):
    
    print('-'*170)
    r = ''
    r += '{:<16}'.format((Cheque[0]))
    r += '{:<16}'.format((Cheque[1]))
    r += '{:<16}'.format((Cheque[2]))
    r += '{:<16}'.format((Cheque[3]))
    r += '{:<16}'.format((Cheque[4]))
    r += '{:<16}'.format((Cheque[5]))
    r += '{:<16}'.format(Cheque[6])
    r += '{:<16}'.format(Cheque[7])
    r += '{:<11}'.format((Cheque[8]))
    r += '{:<16}'.format(Cheque[9])
    r += '{}'.format(Cheque[10])

    return r

def filtro_tipo(lista, tipo):

    l = []

    for i in lista:
        
        if i[9] == tipo:
            l.append(i)
    
    return l

def filtro_estado(lista, estado):
    l = []

    for i in lista:
        
        if i[10] == estado:
            l.append(i)
    
    return l

def filtro_fecha(lista, fechajunta):
    f_origen , f_pago = separar_fechas(fechajunta)
    f_inf =  datetime.strptime(f_origen, '%d-%m-%Y')
    f_sup = datetime.strptime(f_pago, '%d-%m-%Y')
    
    f_min = datetime.timestamp(f_inf)
    f_max= datetime.timestamp(f_sup)
    l = []
    for i in lista:
        # sub 6 es echa orifen 7 efcha pago
        if f_min <= int(i[6]) <= f_max and f_min <= int(i[7]) <= f_max:
            l.append(i)
    
    return l

def pantalla(lista):
    if len(lista) >0:
        to_string_encabezado()
        for i in lista:
            print(to_string(i))
    else:
        print('No hubo coincidencias para la busqueda.')    

def salida_csv(lista,dni):
    now = datetime.now()
    st = str(datetime.timestamp(now))
    nom = str(dni)+'-'+st +'.csv'

    if len(lista)>0:
        head = ['Cuenta Origen','Cuenta Destino','Valor','Fecha Origen','Fecha Pago']
        

        with open(nom, 'w', newline='') as file:
            write = csv.writer(file, delimiter=',')
            write.writerow(head)
            
            for i in lista:
                
                v = [i[3],i[4],i[5],i[6],i[7]]
                write.writerow(v)
        
        
        print('Archivo generado. El nombre del archivo es: ',nom)
    else:
        print('El archivo no se genero porque no hubo coincidencias')
   
      
def principal(): 
   
    #Devuelve una lista de los parametros ingresados por la terminal 
    argumentos = sys.argv  
    
    #Si no ingresa estado del cheque no puede filtrar por fecha
    validar_argumentos(argumentos)
    
    #Crea un arreglo con el que vamos a trabajar para filtrar
    filtro = Filtro_cheque(argumentos[1],argumentos[2],argumentos[3],argumentos[4],argumentos[5],argumentos[6])
    
    lista_dni = leer_archivo(filtro.nombreArchivo,filtro.dni)
 
    if nro_repetido(lista_dni) == True:
       print("ERROR, un número de cheque de una misma cuenta de origen para el dni ingresado se repite.")
       sys.exit(1)
    
    lista_tipo = filtro_tipo(lista_dni, filtro.tipo)
    
    #Filtro_cheque(nom_csv,dni,salida,tipo,estado,fecha)
    if filtro.estado == '0' and filtro.fecha=='0':
     #FILTRA SOLO POR TIPO DE CHEQUE               
        if filtro.salida == "PANTALLA":
            pantalla(lista_tipo)
        else:
                    salida_csv(lista_tipo,filtro.dni)
    
    else:
        lista_estado = filtro_estado(lista_tipo,filtro.estado)
        
        if filtro.estado != '0' and filtro.fecha == '0':
            if filtro.salida == "PANTALLA":
                pantalla(lista_estado)
            else:
                    salida_csv(lista_estado,filtro.dni)
        else:
            if filtro.estado != '0' and filtro.fecha != '0':
                lista_fecha = filtro_fecha(lista_estado,filtro.fecha)
                if filtro.salida == "PANTALLA":
                    pantalla(lista_fecha)
                else:
                    salida_csv(lista_fecha,filtro.dni)
        
principal()