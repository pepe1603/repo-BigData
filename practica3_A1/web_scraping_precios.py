from bs4 import BeautifulSoup
import requests
import csv

# Función para guardar los datos extraídos en un archivo CSV
def guardar_datos_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['Nombre', 'Precio', 'Descripción'])
        writer.writerows(datos)

# URLs de los sitios web donde se encuentra el producto iPhone 13 128GB
urls = {
    'Coppel': 'https://www.coppel.com/celular-apple-iphone-13-128gb-negro-reacondicionado-mkp-10426006',
    'Apple': 'https://www.apple.com/mx/shop/buy-iphone/iphone-13/pantalla-de-6.1-pulgadas-128gb-medianoche',
    'Bodega Aurrera': 'https://www.amazon.com.mx/Apple-iPhone-13-Blanco-Estrella/dp/B09LNW3CY2/ref=asc_df_B09LNW3CY2/?tag=gledskshopmx-20&linkCode=df0&hvadid=641178390665&hvpos=&hvnetw=g&hvrand=5014768144660264696&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010030&hvtargid=pla-1874323612310&mcid=0af51a1705363eef82b4789163e19122&th=1'
}

# Método para obtener el HTML de la página correspondiente
# Método para obtener el HTML de la página correspondiente
def obtener_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f'Error al obtener la página {url}: {response.status_code}')
        return None


# Métodos para extraer datos específicos de cada sitio web
def extraer_datos_coppel(html):
    soup = BeautifulSoup(html, 'html.parser')
    nombre_tag = soup.find('h1', class_='productTitle')
    descripcion_tag = soup.find('div', class_='contentBox')
    precio_tag = soup.find('span', id='offerPrice_4092205')  # Tag precio

    if nombre_tag:
        nombre = nombre_tag.text.strip()
    else:
        nombre = 'Nombre no encontrado'

    if precio_tag:
        precio = precio_tag.get_text()
    else:
        precio = 'Precio no encontrado'

    if descripcion_tag:
        descripcion = descripcion_tag.text.strip()
    else:
        descripcion = 'Descripción no encontrada'

    print("-- DAtos Coopel")
    print("nombre", nombre)
    print("precio", precio)
    print("Descirpcion; ",descripcion)

    return nombre, precio, descripcion


def extraer_datos_apple(html):
    soup = BeautifulSoup(html, 'html.parser')
    nombre_tag = soup.find('h1', class_='productTitle')
    descripcion_tag = soup.find('div', class_='contentBox')
    precio_tag = soup.find('span', '#df7bf390-e662-11ee-ac14-692af4fa05d8_label > span > span.column.form-selector-right-col.rf-bfe-selector-right-col > span > span')
    # precio_tag = soup.find('div', class_='price-display').find('span', class_='current_price')
   
    if nombre_tag:
        nombre = nombre_tag.text.strip()
    else:
        nombre = 'Nombre no encontrado'

    if precio_tag:
        precio = precio_tag.get_text()
    else:
        precio = 'Precio no encontrado'

    if descripcion_tag:
        descripcion = descripcion_tag.text.strip()
    else:
        descripcion = 'Descripción no encontrada'
    

    print("-- DAtos Applel")
    print("nombre", nombre)
    print("precio", precio)
    print("Descirpcion; ",descripcion)

    return nombre, precio, descripcion

def extraer_datos_bodega_aurrera(html):
    soup = BeautifulSoup(html, 'html.parser')
    nombre_tag = soup.find('h1', class_='productTitle')
    descripcion_tag = soup.find('div', class_='contentBox')
    precio_tag = soup.find('div', class__= '#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span:nth-child(2)')
    # precio_tag = soup.find('span', class_='price-text')

    if nombre_tag:
        nombre = nombre_tag.text.strip()
    else:
        nombre = 'Nombre no encontrado'

    if precio_tag:
        precio = precio_tag.get_text()
    else:
        precio = 'Precio no encontrado'

    if descripcion_tag:
        descripcion = descripcion_tag.text.strip()
    else:
        descripcion = 'Descripción no encontrada'

    
    print("-- DAtos Bodega Aurrera")
    print("nombre", nombre)
    print("precio", precio)
    print("Descirpcion; ",descripcion)

    return nombre, precio, descripcion

# Ejecutar el proceso para cada sitio web
datos_coppel = extraer_datos_coppel(obtener_html(urls['Coppel']))
datos_apple = extraer_datos_apple(obtener_html(urls['Apple']))
datos_bodega_aurrera = extraer_datos_bodega_aurrera(obtener_html(urls['Bodega Aurrera']))

# Verificar si se obtuvieron los datos (precio) correctamente y guardar en CSV
if datos_coppel[1] != 'Precio no encontrado' and datos_apple[1] != 'Precio no encontrado' and datos_bodega_aurrera[1] != 'Precio no encontrado':
    datos_precios = [datos_coppel, datos_apple, datos_bodega_aurrera]
    guardar_datos_csv(datos_precios, 'datos_precios.csv')
    print('Datos guardados en datos_precios.csv')
else:
    print('No se pudieron obtener todos los precios.')

# Imprimir precios obtenidos
print('\nPrecios obtenidos:')
print(f'Coppel: {datos_coppel[1]}')
print(f'Apple: {datos_apple[1]}')
print(f'Bodega Aurrera: {datos_bodega_aurrera[1]}')
