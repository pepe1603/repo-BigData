import pandas as pd
#importar la libreria re para usar expresion regulraes en pyhthon
import re
rutaArchivo = './data/movie_metadata.csv'

# Función para el ejercicio 3:  extraer el código del título
def extract_title_code(link):
    # Utilizar expresiones regulares para buscar el código del título en el enlace
    match = re.search(r'tt\d+', link)
    if match:
        return match.group()
    else:
        return None


# Cargar los datos desde el archivo CSV de nuestra carpeta Data
movies_df = pd.read_csv(rutaArchivo)

# Imprimir los primeros 5 registros antes de la limpieza
print("Primeras 5 Filas del Archivo movie_metadata.csv antes de la limpieza:\n")
print(movies_df.head())

#Ejercicio 1:
# La columna gross posee valores en blanco o nulos, estos deben ser rellenados con el valor promedio de todos los valores de esa columna.
print("\n--------------------- Ejercicio 1: ---------------------------\n")
#imprimir la columna Gross pra ver elcontenido antes de realizar l limpieza

print("\nValores de la columna 'gross' antes de la limpieza:")
print(movies_df['gross'].head(10))
print("\n\t ----> Realizando Cambios en < Gross > ........\n")

# Calculamos el valor promedio de la columna "gross" excluyendo los valores que se encuentren en blanco o nulos
promedio_gross = movies_df['gross'].dropna().mean()

# Reemplazar/rellenar los valores nulos en la columna "gross" con el valor del promedio calculado
movies_df['gross'] = movies_df['gross'].fillna(promedio_gross)
# Imprimir la columna 'gross' después de la limpieza
print("\nValores de la columna 'gross' después de la limpieza:")
print(movies_df['gross'].head(10))



#Ejercicio 2:
# El atributo o columna facenumber_in_poster posee valores nulos o en blanco y valores negativos, los cuales deber rellenados o reemplazados con el valor de cero 0.
print("\n--------------------- Ejercicio 2: ---------------------------\n")
print("Columna facenumber_in_poster posee valores nulos o en blanco y valores negativos, los cuales fueron  rellenados/reemplazados con el valor de cero 0.")
# Reemplazar los valores nulos o negativos en la columna 'facenumber_in_poster' con ceros
movies_df['facenumber_in_poster'] = movies_df['facenumber_in_poster'].fillna(0)
movies_df['facenumber_in_poster'] = movies_df['facenumber_in_poster'].apply(lambda x: 0 if x < 0 else x)

# Mostrar los campos de la columna 'facenumber_in_poster' despues de la limpieza
print("\nSe esta aplicando la liimpieza de 'facenumber_in_poster'  : \t...TErminado... \n")

#Ejercicio 3:
#Crear una nueva columna denominada TittleCode y los valores que serán asignados resultar de realizar una extracción o subcadena de la columna movie_imdb_link.
#        Ejemplo: http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1    se extrae el dato:  tt0499549
print("\n--------------------- Ejercicio 3: ---------------------------\n")

print(
    "3.- Crear una nueva columna denominada TittleCode y los valores que serán asignados resultar de realizar una extracción o subcadena de la columna movie_imdb_link.",
        "\n\tEjemplo: http://www.imdb.com/title/tt0499549/?ref_=fn_tt_tt_1    se extrae el dato:  < tt0499549 >"
)
#hacemos uso de la funcion declarada en el comienxo del programa:
# Aplicar la función a la columna 'movie_imdb_link' para crear la nueva columna 'TitleCode'
movies_df['TitleCode'] = movies_df['movie_imdb_link'].apply(extract_title_code)
print("Creando nueva columna......\n")
# Mostrar los primeros registros de la columna 'TitleCode'
print("\nPrimeros registros de la columna 'TitleCode':")
print(movies_df['TitleCode'].head())

#Ejercicio 4:
#La columna title_year posee valores en blanco o nulos, se debe rellenar todas esas celdas con el valor de cero 0.
print("\n--------------------- Ejercicio 4: ---------------------------\n")
print(" La columna title_year posee valores en blanco o nulos, se debe rellenar todas esas celdas con el valor de cero 0.")
# Rellenar los valores en blanco o nulos en la columna "title_year" con cero
print("\tAppicando cambios a tittle_years:.....")
movies_df['title_year'] = movies_df['title_year'].fillna(0)
print("Terminado.....\n")

#Ejercicio 5:
#Realizar una selección de todas las filas (Rows) de las Movies filmadas en "USA" tomando como referencia la columna country; posteriormente eliminar las filas restantes en el dataframe.
print("\n--------------------- Ejercicio 5: ---------------------------\n")
print("5.- Realizar una selección de todas las filas (Rows) de las Movies filmadas en < USA > tomando como referencia ",
      "la columna country; posteriormente eliminar las filas restantes en el dataframe.\n","\tAplicando a limpieza..\n"
      )
# Filtrar las filas donde el país sea "USA"
movies_usa = movies_df[movies_df['country'] == 'USA']

# Eliminar las filas restantes del DataFrame original
movies_df = movies_usa.copy()
print("DataFrame  actualizado: \n\t Terminado.....\n")
print(movies_df.head())

#Ejercicio 6:
# Generar un nuevo archivo CSV con las películas filmadas en "USA"
print("\n--------------------- Ejercicio 6: ---------------------------\n")

print("Generar un nuevo archivo CSV con las películas filmadas en < USA > \n")
# Guardamo los datos limpios en un nuevo archivo CSV en nuestra carpeta data
movies_usa.to_csv("./data/FilmTV_USAMoviesClean.csv", index=False)
print("\tGenereando archivo...\n\nTErminado\n")
print("El archivo  se guardo con exito  en practica2/data/FilmTV_USAMoviesClean.csv\n")