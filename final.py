import numpy as np
import pandas as pd

# DECLARACION DE VARIABLES PARA INGRESAR POR CONSOLA LA CANTIDAD DE VACAS
nv = int(input("Numero de vacas: "))
# CICLO WHILE PARA NO DEJAR AVANZAR EL PROGRAMA SI EL NUMERO DE VACAS A INGRESAR ES MAYOR A 50
while (nv > 50):
    print("error")
    nv = int(input("Numero de vacas: "))
print("informacion correcta")
# DECLARACION DE VARIABLE CON DATO ENTERO DE 7 PORQUE HACE REFERENCIA A LOS DIAS DE LA SEMANA
cd = 7
# VARIABLE TIPO MATRIZ PARA ALMACENAR TODOS LOS DATOS QUE SE VAN A INGRESAR
matriz = []

# CICLO FOR QUE PERMITE CREAR EL TAMAÑO DE LA MATRIZ DE ACUERDO A LOS DATOS QUE EN ESTE RETO EL MAXIMO ES 7X50
for i in range(cd):
    matriz.append([])
    for j in range(nv):
        valor  =  float(input("dia {}, vaca {} :".format(i+1, j+1)))
        matriz[i].append(valor)


# ESTA FUNCION NOS PERMITE CREAR UN TIPO DE TABLA DE EXCEL CON COLUMNAS POR FILAS, INDEX HACE REFERENCIA A LAS FILAS

df = pd.DataFrame(matriz, index=["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"])

# CREAMOS UNA LISTA PARA ALMACENAR EL NUMERO DE VACAS
listn=[]
# EL FOR QUE NOS PERMITE DARLE UN RANGOGO DE 1 EN 1 A LAS VACAS Y DE ESTA FORMA LLAMAR LAS COLUMNAS
for i in range(len(df.columns)):
    listn.append(f'vaca {i + 1}')
df.set_axis(listn, axis=1, inplace=True)


#FUNCION SUMA QUE CON EL AGREGADO AXIS QUE NOS CREA UN NUEVA COLUMNA CON LA SUMATORIA DE LOS DIAS
df['total leche en el dia']=df.sum(axis=1)
print(df)

#CREAMOS VARIABLES MAXIMOS Y MINIMOS CON FUNCIO .MAX Y .MIN PARA TRAER EL VALOR MAXIMO Y MINIMO DE LA COLUMNA QUE SUMA EL TOTAL 
maxval = df['total leche en el dia'].max()
minval = df['total leche en el dia'].min()

#MOSTRAR POR PANTALLA LAS VARIABLES DE MINIMOS Y MAXIMOS 
print("el maximo de recogido en un dia" , maxval,)
print("el minimo de recogido en un dia" , minval)

#VIDEO EXPLICACION
#https://www.dropbox.com/s/gl4a4ch08v3tzoj/difficultpressuresdirectsecondly%20on%202022-09-06%2023-28.mp4?dl=0




    
   




 




