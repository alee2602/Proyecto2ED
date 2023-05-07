#Universidad del Valle de Guatemala
#Algoritmos y Estructuras de Datos
#Sección 20
#Derek Arreaga, Giovanni Santos, César López, Isabella Miralles y Mónica Salvatierra
#Algoritmo de Floyd para recomendar música en base al estado de ánimo y géneros musicales preferidos del usuario

from neo4j import GraphDataBase

#Crear la conexión a la base de datos

def connectneo4j():
    url="bolt://localhost:7687"  #Dirección de la base de datos
    username="" #Usuario para acceder a la base de datos
    password="" #Contraseña para acceder a la base de datos
    driver= GraphDataBase.driver(url, auth=(username, password))
    return driver

#Crear las canciones en la base de datos

def crear_canciones_db(db,canciones):
    for cancion in canciones:
        crear_query= f"CREATE (:Canción {{Nombre: '{cancion.name}', Género: '{cancion.genre}', Artista: '{cancion.artist}', Emoción Transmitida: '{cancion.emotion}'}})"
        with db.session() as session:
            session.run(crear_query)

#Pedir al usuario su estado de ánimo actual

def getemocion(db):

    emocion = input("Ingrese su estado de ánimo actual: ") #Emoción Actual
    # Buscar las canciones que corresponden a la emoción ingresada y la emoción que transmite.
    emocion_query = f"MATCH (c:Canción) WHERE c.Emoción Transmitida = '{emocion}' RETURN c"
    with db.session() as session:
        resultado = session.run(emocion_query)
        canciones = [record["c"] for record in resultado]
    return emocion, canciones

#Pedir al usuario sus géneros preferidos

def getgenerospreferidos(db):
    
    generospreferidos=input("Ingrese sus géneros preferidos separados por comas: ") #Géneros preferidos

    #Guarda los géneros preferidos en la base de datos, haciendo relación con los que ya están establecidos en la db.
    with db.session() as session:
        for genero in generospreferidos.split(","):
            relacion_query= f"MATCH (g:Género {{Nombre: '{genero.strip()}'}}) CREATE (u)-[:GUSTA]->(g)"
            session.run(relacion_query)

    return generospreferidos

#Ejecuta el funcionamiento del sistema mediante el algoritmo de Floyd
def ejecutaralgoritmo(db, emocion, generospreferidos):

    recomendacion_query= f"MATCH (c:Canción)-[:DE]->(e:Emoción {{Nombre: '{emocion}'}}) WHERE c.Género IN {generospreferidos} RETURN c"

    #Ejecutar la consulta 
    with db.session() as sesion:
        result= sesion.run(recomendacion_query)
        recomendaciones= [record["c"] for record in result]

    return recomendaciones

#Muestra las recomendaciones de las canciones
def mostrar_recomendaciones(recomendaciones):

    print("Canciones recomendadas:")
    for cancion in recomendaciones:
        print(cancion["Nombre"] + " - " + cancion["Artista"])

#Manera en la que funciona el algoritmo
def main():
    driver = connectneo4j()
    db = GraphDataBase(driver)
    emocion= getemocion()
    generospreferidos=getgenerospreferidos()
    recomendaciones= ejecutaralgoritmo(emocion, generospreferidos)
    mostrar_recomendaciones(recomendaciones)
