# Mete todo tu código dentro de una función llamada obtener_clima(ciudad) y llámala al final pasándole el nombre que ingresó el usuario.

import requests
from requests.exceptions import Timeout, ConnectionError
def get_weather(name_city):
    
    print(f"Buscando el clima de {name_city}...")

    try: 
        answer = requests.get(f"https://wttr.in/{name_city}?format=j1")
        dates = answer.json()

        condition = dates["current_condition"][0]

        temp_c = condition["temp_C"]
        weather_desc = condition["weatherDesc"][0]["value"]
        humidity = condition["humidity"]

        return f"🌤 {name_city}: {temp_c}°C, {weather_desc}, Humedad: {humidity}%"
    except Timeout:
        return "ERROR: Ha tardado demasiado. Intenta de nuevo mas tarde"
    except ConnectionError:
        return "ERROR: Conexion inestable. Intenta de nuevo mas tarde"
    except requests.exceptions.JSONDecodeError:
        return("Hubo un error. Intenta de nuevo mas tarde")

city_user = input("Ingresa tu ciudad: ")
print(get_weather(city_user))