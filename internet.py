from googlesearch import search
import requests
from bs4 import BeautifulSoup

def obtener_respuesta_google(query):
    try:
        resultados = list(search(query, num=1, stop=1, pause=2, lang='es'))
        if resultados:
            enlace = resultados[0]
            response = requests.get(enlace)
            soup = BeautifulSoup(response.text, 'html.parser')
            texto = soup.find('p').get_text(separator='\n', strip=True)
            return texto[:500]  # Ajustado para mostrar los primeros 500 caracteres de forma resumida.
        else:
            return "No se encontraron resultados en Google para esta consulta."
    except Exception as e:
        print(f"Error al buscar en Google: {e}")
        return "Lo siento, no pude realizar la búsqueda en este momento."

# Bucle para permitir múltiples preguntas
while True:
    consulta = input("Hazme una pregunta (o escribe 'salir' para terminar): ")
    
    if consulta.lower() == 'salir':
        print("¡Hasta luego!")
        break
    
    respuesta_google = obtener_respuesta_google(consulta)
    print(respuesta_google)