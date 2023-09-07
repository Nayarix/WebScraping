import requests
from bs4 import BeautifulSoup

def web_scraping(url):
    # Realizar una solicitud HTTP a la página web
    response = requests.get(url)
    # Analizar el contenido HTML usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar los divs con class='val' que contienen los valores de compra y venta
    valores_divs = soup.find_all('div', class_='val')
    
    # Lista de categorías de dólar correspondientes a cada valor
    categorias = ["Dólar Blue", None, "Oficial promedio", "Dólar Bolsa", "Dólar Contado con Liquidación", "Dólar Cripto", "Dólar Solidario"]
    
    # Listas para almacenar los valores de compra y venta de cada categoría
    compras = []
    ventas = []
    
    idx = 0
    # Iterar sobre los divs que contienen los valores
    for val_div in valores_divs:
        # Encontrar el div con class='label' que contiene la descripción del valor
        label_text = val_div.find_previous_sibling('div', class_='label').text.strip()
        # Obtener el valor de compra o venta
        valor = val_div.text.strip()
        
        # Verificar si es un valor de compra y si su índice es par
        if 'compra' in label_text.lower() and idx % 2 == 0:
            categoria = categorias[idx // 2]
            if categoria:
                # Agregar el valor a la lista de compras
                compras.append((categoria, valor))
        # Verificar si es un valor de venta y si su índice es impar
        elif 'venta' in label_text.lower() and idx % 2 == 1:
            categoria = categorias[idx // 2]
            if categoria:
                # Agregar el valor a la lista de ventas
                ventas.append((categoria, valor))
            
        idx += 1
    
    # Imprimir encabezado de la tabla
    print("CATEGORÍA\t\t\t\tCOMPRA\t\t\tVENTA")
    # Imprimir línea separadora
    print("="*80)
    # Imprimir los valores de compra y venta en forma de tabla
    for compra, venta in zip(compras, ventas):
        print(f"{compra[0]:<30}\t{compra[1]:<15}\t{venta[1]:<15}")

if __name__ == "__main__":
    url = 'https://dolarhoy.com/'
    web_scraping(url)