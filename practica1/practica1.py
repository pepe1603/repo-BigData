#Leer un archivo .csv desde un script 
#desarrollado en Python y cargar los datos 
#dentro de un dataframe usando la función read_csV de la biblioteca pandas.

import pandas as pd

#cargams el archvivo.csv listadoFertilizadntes3
rutaArchivo = './data/listado_3_beneficiarios_fertilizantes_2023_corte_091023.csv'


# Cargar el archivo CSV en un DataFrame, indicando que la primera fila no contiene los nombres de las columnas
df = pd.read_csv(rutaArchivo, header=None, skiprows=1, encoding='latin1')

# Renombrar las columnas del DataFrame
df.columns = ['NUMERO', 'ESTADO', 'MUNICIPIO', 'ACUSE ESTATAL', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'NOMBRE (S)', 'PAQUETE']

# Mostrar las primeras 10 filas del DataFrame
print("Primeras 10 Filas del Conjunto de Datos Fertilizantes 2023:\n")
print(df.head(10))

#eJERCICIO 1:
#- Identificar las 3 Entidades Federativas con mayor número de personas beneficiadas.
print("\n--------------------- Ejercicio 1: ---------------------------\n")

# Identificar las 3 Entidades Federativas con mayor número de personas beneficiadas
beneficiados_por_estado = df.groupby('ESTADO').size().reset_index(name='Total_Beneficiados')
top_3_entidades = beneficiados_por_estado.nlargest(3, 'Total_Beneficiados')

print("\nLas 3 Entidades Federativas con mayor número de personas beneficiadas son:")
print(top_3_entidades)


#eJERCICIO 2:
#- Crear un subconjunto de datos (dataframe 2), el cual posee la selección de registros que corresponden a Chiapas.
print("\n--------------------- Ejercicio 2: ---------------------------\n")
# Crear un subconjunto de datos que contenga solo los registros de Chiapas
#es decir realizar un filtro para el esdo de chiapas
df_chiapas = df[df['ESTADO'] == 'CHIAPAS']

# Mostramos a las primeras filas del subconjunto de datos de Chiapas
print("\nPrimeras Filas del Subconjunto de Datos de Chiapas:\n")
print(df_chiapas.head())

#Ejerciocio 3:
#Del segundo subconjunto realizar un conteo de paquetes recibidos agrupados por municipio e imprimir en pantalla:  Municipio | TotalPaquetes
print("\n--------------------- Ejercicio 3: ---------------------------\n")

# Realizar un conteo de paquetes recibidos agrupados por municipio
conteo_paquetes_por_municipio = df_chiapas.groupby('MUNICIPIO')['PAQUETE'].count().reset_index()

# Renombrar la columna de conteo de paquetes
conteo_paquetes_por_municipio.rename(columns={'PAQUETE': 'TotalPaquetes'}, inplace=True)

# Imprimir el conteo de paquetes por municipio en pantalla
print("Conteo de Paquetes Recibidos Agrupados por Municipio:\n")
print(conteo_paquetes_por_municipio)


#Ejercicio 4:
#Identificar los 3 3 municipios cin mayor numero de paquetes recibidos , ordenados de mayor a menor

print("\n--------------------- Ejercicio 4: ---------------------------\n")
#paso1: 
# Identificar los 3 municipios con el mayor número de paquetes recibidos
top_municipios = conteo_paquetes_por_municipio.nlargest(3, 'TotalPaquetes')

#paso2:
# Imprimir los 3 municipios con mayor número de paquetes recibidos
print("Los 3 Municipios con Mayor Número de Paquetes Recibidos:\n")
print(top_municipios)


