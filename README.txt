Necesario:
    Python3
    -librerias siguiente: csv, re, sys, datetime 

Los argumentos aceptados por la terminal son:
    El orden de los argumentos son los siguientes: 
        1-Nombre del archivo .py
        2 -Nombre del archivo csv.
        3 -DNI del cliente donde se filtraran.
        4 -Salida: PANTALLA o CSV
        5 -Tipo de cheque: EMITIDO o DEPOSITADO
        6 -Estado del cheque: PENDIENTE, APROBADO, RECHAZADO. (Opcional)
        7- Rango fecha: xx-xx-xxxx:yy-yy-yyyy (Opcional)

ATENCION: en caso de no pasar un estado de cheque como argumento, no se podra filtrar por rango de fecha.

Nota: - El codigo no esta modularizado en diferentes archivos .py para evitar errores 
-el archivo cheques_generales.csv fue el archivo que se utilizo para testear el codigo
