import pandas as pd
import folium
import re
import imgkit
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

#//////// Seccion de Funciones

# Función para crear el mapa con los marcadores de los 3 mejores museos o galerías de arte en Brooklyn usado en el ejercico 5
def crear_mapa_top_3(top_3_mejor_calificados):
    # Crear un mapa centrado en Brooklyn
    mapa = folium.Map(location=[40.6782, -73.9442], zoom_start=12)

    # Función para extraer coordenadas de la columna the_geom
    def extraer_coordenadas(geom):
        coords = re.findall(r"[-+]?\d*\.\d+|\d+", geom)
        return [float(coords[1]), float(coords[0])]

    # Agregar marcadores para los 3 mejores museos o galerías de arte en Brooklyn
    for index, row in top_3_mejor_calificados.iterrows():
        coords = extraer_coordenadas(row['the_geom'])
        folium.Marker(coords, popup=row['NAME']).add_to(mapa)

    # Guardar el mapa como un archivo HTML
    mapa.save("mapa_top_3_brooklyn.html")
    #tambien guardamos como png para poderlo usar en el pdf

# Función para generar el informe en PDF
def generar_informe_pdf(top_3_mejor_calificados, mapa_html):
    # Crear un objeto PDF
    doc = SimpleDocTemplate("informe_mejores_museos_galerias.pdf", pagesize=letter)

    # Contenido del informe
    contenido = []

    # Estilo del párrafo
    styles = getSampleStyleSheet()
    estilo_titulo = styles["Title"]
    estilo_normal = styles["Normal"]

    # Titulo del informe
    titulo = Paragraph("Mejores Museos y Galerías de Brooklyn", estilo_titulo)
    contenido.append(titulo)

    # Agregar el mapa
    contenido.append(Image(mapa_html, width=500, height=500))

    # Encabezados de la tabla
    encabezados = [("Nombre", "Dirección", "Grados")]

    # Datos para la tabla
    datos_tabla = [(row['NAME'], row['ADDRESS1'], f"{row['GRADING']}°") for index, row in top_3_mejor_calificados.iterrows()]

    # Crear la tabla
    tabla = Table(encabezados + datos_tabla)

    # Estilo de la tabla
    estilo_tabla = TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                               ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), (0.8, 0.8, 0.8)),
                               ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])

    tabla.setStyle(estilo_tabla)

    # Agregar la tabla al contenido del informe
    contenido.append(tabla)

    # Generar el PDF
    doc.build(contenido)

#////// Fin de Seccion de Funciones

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('data/new-york-city-art-galleries.csv', encoding='latin1')

#Mostramos primero 5 filas del DataFrame Original
print("---------------- Data frame Original ------------------")
print(df.head())

#Ejercioco1: Eliminar Filas Duplicadas
print("\n------------------- Ejercicio 1: eliminar filas duplicadas -----------------\n")

# Eliminar filas duplicadas
df_sin_duplicados = df.drop_duplicates()
# Mostrar el DataFrame sin filas duplicadas
print(df_sin_duplicados)

#Ejercioco2: Eliminar collumna ADDRESS2
print("\n------------------- Ejercicio 2: eliminar Columna ADRRESS2 -----------------\n")

# Eliminamos la columna "Address2"
df_sin_address = df.drop(columns=['ADDRESS2'])

# mostrar el DataFrame sin la columna "Address2" .
print(df_sin_address)


#Ejercioco3: eleccionar a los museos o galerías de arte del distrito Brooklyn
print("\n------------------- Ejercicio 3: eleccionar a los museos o galerías de arte del distrito Brooklyn -----------------\n")
# Seleccionar los museos o galerías de arte del distrito de Brooklyn
brooklyn_df = df[df['CITY'] == 'Brooklyn']

# Mostrar los museos o galerías de arte del distrito de Brooklyn
print(brooklyn_df)


#Ejercioco3: Filtrar a los 3 mejor calificados (museo o galería)
print("\n------------------- Ejercicio 4: Filtrar a los 3 mejor calificados (museo o galería) de Brooklyn-----------------\n")

 #ordenamos las calificaciones en orden descendente usando el filro amnterior
brooklyn_df_sorted = brooklyn_df.sort_values(by='GRADING', ascending=False)

# Filtrar los 3 mejores calificados 
top_3_mejor_calificados = brooklyn_df_sorted.head(3)
# Mostrar los 3 mejores calificados
print(top_3_mejor_calificados)

#Ejercioccio 5: Generar Mapa para ubicar a los top 3 de la ciudad de Brooklyn
print("\n------------------- Ejercicio 5:Generar imagen de Mapa indicando la ubicación de los 3 mejores\n")
print("\n\tGenerando Mapa en formato < HTML > Top 3 Mejores de  Brooklyn...\n")
# Llamamos a la funcion para crear el mapa del top-3
crear_mapa_top_3(top_3_mejor_calificados)

print("\nMapa Generado con Exito , puedes visualizarlo en el directorio actual: mapa_top_3_brooklyn.html")



#Ejercioccio 6: Generar el reporte final en un archivo de tipo PDF  con un Titulo , etiqueta nombre: Addreess y grados..
print("\n------------------- Ejercicio 6:Generar reporte final en formato pdf del mapa top_3 \n")
print("\n\tGenerando Reporte Final en PDF --> Espera...\n")

#Convertimosel  mapa de top3.html en formato   PNG
print("\t\tConvirtiendo ...\n")

# Convertir el archivo HTML a imagen usando imgkit
#mapa_html = 'mapa_top_3_brooklyn.html'
salida_mapa_png = 'mapa_top_3_brooklyn.png'
#imgkit.from_file (mapa_html, salida_mapa_png)

print("[mapa_top_3_brooklyn.png ] \n Completado...")

# Llamamos a la funcion para generar el informe PDF 
generar_informe_pdf(top_3_mejor_calificados, salida_mapa_png)

print("\n\tInforme Generado Exitosamente: informe_mejores_museos_galerias.pdf\n")

