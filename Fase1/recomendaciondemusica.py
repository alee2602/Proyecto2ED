#Universidad del Valle de Guatemala
#Algoritmos y Estructuras de Datos
#Sección 20
#Derek Arreaga, Giovanni Santos, César López, Isabella Miralles y Mónica Salvatierra
#Algoritmo de Floyd para recomendar música en base al estado de ánimo y géneros musicales preferidos del usuario

from neo4j import SongDataBase

#Crear la conexión a la base de datos

url=""  #Dirección de la base de datos
username="" #Usuario para acceder a la base de datos
password="" #Contraseña para acceder a la base de datos
driver= SongDataBase.driver(url, auth=(username, password))

#Crear las canciones en la base de datos

def crear_canciones_db(db):
    for cancion in canciones:
        crear_query= f"CREATE (:Canción {{Nombre: '{cancion.name}', Género: '{cancion.genre}', Artista: '{cancion.artist}', Emoción Transmitida: '{cancion.emotion}'}})"
        with db.session() as session:
            session.run(crear_query)

#Pedir al usuario su estado de ánimo actual

def getemocion():

    emocion="" #Estado de ánimo actual

    return emocion

#Pedir al usuario sus géneros preferidos

def getgenerospreferidos():

    generospreferidos="" #Géneros preferidos

    return generospreferidos


