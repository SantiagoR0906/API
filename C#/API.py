import requests
import json
import pandas as pd
from pandas import json_normalize

class apiAccidentes:
    def __init__(self, url_api):
        self.url_api = url_api
    
    def transformacion(self, datos):
        datos = json.loads(datos.text)
        datos = json_normalize(datos)
        arreglo = datos['fecha'].tolist()
        arreglito = pd.DataFrame(datos)
        return arreglito
    
    def consumo (self):
        datos = requests.get(self.url_api)

        if datos.status_code == 200:
            datos_json = self.transformacion(datos)
            return datos_json
        else:
            raise Exception(f'Fallo el consumo: {datos.status_code}')
        # datos = requests.get(url_api)
