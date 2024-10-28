import requests

class Database:
    def __init__(self):
        self.url = "https://671be4152c842d92c381a48c.mockapi.io/Libros"

    def get_all_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener los datos. Código de estado: {response.status_code}")
                return []
        except Exception as e:
            print(f"Error en la conexión con la base de datos: {e}")
            return []

    def get_record_by_id(self, record_id):
        try:
            response = requests.get(f"{self.url}/{record_id}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error al obtener el registro con ID {record_id}. Código de estado: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error en la conexión con la base de datos: {e}")
            return None