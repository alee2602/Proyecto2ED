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

