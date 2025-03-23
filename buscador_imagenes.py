import requests  # Importamos la librería requests para hacer peticiones HTTP

class BuscadorImagenes:
    def __init__(self):
        try:
            # Solicitamos al usuario la consulta de la imagen y eliminamos espacios en blanco
            usuario_consulta = input("Ingresa la imagen a consultar: ").strip()

            # Verificamos que el usuario no deje el campo en blanco
            if not usuario_consulta:
                print("No se puede tener el campo en blanco.")
                return  # Salimos del programa si no hay entrada válida

            # Construimos la URL para la consulta en la API de Unsplash
            self.url_consulta = f"https://api.unsplash.com/search/photos?query={usuario_consulta}&client_id=TU_API_KEY"

            # Hacemos la petición GET a la API
            respuesta = requests.get(self.url_consulta)

            # Convertimos la respuesta en formato JSON
            peticion_json = respuesta.json()

            # Extraemos información de la primera imagen encontrada
            imagen_encontrada = peticion_json["results"][0]["id"]  # ID de la imagen
            descripcion_imagen = peticion_json["results"][0]["description"]  # Descripción de la imagen
            link_imagen = peticion_json["results"][0]["links"]["download"]  # URL de descarga de la imagen

            # Mostramos los resultados en consola
            print(f"Imagen encontrada: {imagen_encontrada}")
            print(f"Descripcion de la imagen: {descripcion_imagen}")
            print(f"Link de descarga de la imagen: {link_imagen}")

        except Exception as error:
            # Capturamos cualquier error y mostramos un mensaje de error
            print(f"Error en el programa: {error}.")

# Punto de entrada del programa
if __name__ == "__main__":
    imagen = BuscadorImagenes()
