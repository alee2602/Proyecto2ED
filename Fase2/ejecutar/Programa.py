import random
from neo4j import GraphDatabase
from usuario import Usuario

class Neo4jDatabase:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return result.data()


def menu():

    while True:
        print("\n\n")
        print("===== MENÚ =====")
        print("¿Qué desea hacer?")
        print("1.Recomiendame canciones")
        print("2.Agregar canciones")
        print("3.Eliminar canciones")
        print("0.Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            Recomendar()
        elif opcion == "2":
            agregar()
        elif opcion == "3":
            eliminar()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

def eliminar():
    print("Ingrese el nombre de la canción que desea eliminar: ")
    cancion = input("- ")



    query = "MATCH (s:SONG {Title: '"+cancion+"'}) DETACH DELETE s"

    modificar(query)

    print("La canción ha sido eliminada 😔")


def agregar():
    cancion = input("¿Cómo se llama la canción que desea agregar?")
    artista = input("¿De quién es la canción?")
    
    feeling = " "
    
   

    #GENERO
    print("¿De qué género es la canción?")
    gens = buscar("MATCH (g:GENRE) RETURN g","GENRE")
    num = 1
    for g in gens:
        print(str(num)+" "+g)
        num+=1
    genIndex = input("- ")
    genero = gens[int(genIndex)-1]
    print("Tu canción es del género: " + genero)

    #FEELING
    print("¿Cómo te hace sentir '"+ cancion +"'?")
    feels = buscar("MATCH (f:FEELING) RETURN f","FEELING")
    num = 1
    for f in feels:
        print(str(num)+" "+f)
        num+=1
    feelIndex = input("- ")
    feeling = feels[int(feelIndex)-1]
    print("Tu canción te hace sentir:" + feeling)

    ##Ya con las variables definidas, procedemos a insertarlas en el query para eliminarlas 🤠

    query="MERGE (s:SONG {Title: '"+cancion+"'}) "

    query+= " WITH s "
    query+= " MATCH (g:GENRE {type: '"+genero+"'}) "
    query+= " MERGE (s)-[:ES_DE_GENERO]->(g) "

    query+= " WITH s "
    query+= " MERGE (a:ARTIST {name: '"+artista+"'}) "
    query+= " MERGE (s)-[:ES_DE_ARTISTA]->(a) "
    query+= " MERGE (a)-[:CANTA]->(s) "

    query+= " WITH s "
    query+= " MERGE (f:FEELING{Feeling:'"+feeling+"'}) "
    query+= " MERGE (s)-[:TRANSMITE]->(f) "
    query+= " MERGE (f)-[:LO_TRANSMITE]->(s) "
    
    modificar(query)
    print("Su canción se agregó exitosamente :D")
           

def Recomendar():
    canciones = []
    artistas = []
    nombre = input("Ingresa tu nombre: ")
    
    genre = PedirGeneros()

    feeling = PedirFeeling()

    NuevoUsuario = Usuario(nombre, feeling, genre)


    # Conexión a la base de datos Neo4j
    
    #FiltrarM1(NuevoUsuario)
    canciones = FiltrarM2(NuevoUsuario)
    
    print("\n- - - - - - - - - - - - - - - ")
    for i in canciones:
        num = 1
        print(str(num)+". "+i)
        num+=1
        print("- - - - - - - - - - - - - - - ")
    
    
def FiltrarM2(user):

    feeling = user.feeling
    songs = []
    artists = []

    if(len(user.genre)>1):
        for g in user.genre:
            query = f"""MATCH (s:SONG)-[:ES_DE_GENERO]->(g:GENRE) 
        WHERE g.type IN ['{g}'] WITH s, collect(g) AS generos
        MATCH (s)-[:TRANSMITE]->(f:FEELING)
        WHERE f.Feeling = '{feeling}' AND (ANY(g IN generos WHERE g.type = '{g}'))
        WITH s, rand() AS random
        ORDER BY random
        LIMIT 5
        RETURN s
        """
        
            songs.extend(buscar(query,"SONG"))
    else:
        gen = user.genre[0]
        query = f"""MATCH (s:SONG)-[:ES_DE_GENERO]->(g:GENRE) 
        WHERE g.type IN ['{gen}'] WITH s, collect(g) AS generos
        MATCH (s)-[:TRANSMITE]->(f:FEELING)
        WHERE f.Feeling = '{feeling}' AND (ANY(g IN generos WHERE g.type = '{gen}'))
        WITH s, rand() AS random
        ORDER BY random
        LIMIT 5
        RETURN s
        """
        songs = buscar(query,"SONG")
        print("Buscando canciones...")
        random.shuffle(songs)

    if songs:
        print("De acuerdo a tus preferencias, te recomendamos las siguientes canciones:")
        #Buscar artistas
        
        for s in songs:
            artists.append(buscar('MATCH (a:ARTIST)-[:CANTA]->(s:SONG)WHERE s.Title = "'+s+'"RETURN a',"ARTIST"))


    else:
        print("No hay canciones que coincidan con sus preferencias, intente con otras 😔")

    return songs
    

#PRIMER MÉTODO QUE SE INTENTÓ APLICAR, PERO ERA POCO EFECTIVO POR LA ESPERA DE RESPUESTA CON LA BASE DE DATOS
def FiltrarM1(user):
    generos = user.genre
    feeling = user.feeling
    filtro1 = []
    sentimientos = []

    #CREAR CONSULTAS

    if(len(generos)>1):
        #CANCIONES POR GENERO
        for g in generos:

            filtro1.extend(buscar("MATCH (s:SONG)-[:ES_DE_GENERO]->(g:GENRE) WHERE g.type = '"+g+"' RETURN s","SONG"))

        #BUSCAR POR FEELING
        for s in filtro1:
            sentimientos.extend(buscar("MATCH (f:FEELING)-[:LO_TRANSMITE]->(s:SONG) WHERE s.Title = '"+s+"' RETURN f","FEELING"))
        
        for a in filtro1:
            print(a)
        
        for o in sentimientos:
            print(o)
        



def PedirGeneros():
    gens = buscar("MATCH (g:GENRE) RETURN g","GENRE")
    generosUsuario = []
    num = 1
    for g in gens:
        print(str(num)+" "+g)
        num+=1
    print("Ingresa el número de tus géneros favoritos (escribe 'fin' para terminar):")
    

    while True:
        if(generosUsuario):
                print("Generos seleccionados: "+', '.join(generosUsuario))
   
        generoNum = input("- ")
        if generoNum.lower() == 'fin':
            break
        if (gens[int(generoNum)-1]) in generosUsuario:
            print("Ya está agregado el género: "+gens[int(generoNum)-1]+", intente con otro.")
        else:
            generosUsuario.append(gens[int(generoNum)-1])
            print("Se agregó:"+generosUsuario[-1])

        
    return generosUsuario

def PedirFeeling():
    feels = buscar("MATCH (f:FEELING) RETURN f","FEELING")
    feelingUsuario =" "
    num = 1
    for f in feels:
        print(str(num)+". "+f)
        num+=1
    print("Ingresa el número de como te quieres sentir: ")
    

    while True:
   
        FeelingNum = input("- ")
        if((int(FeelingNum)-1)>=len(feels)):
            print("El dato ingresado no es correcto")
            break
        else:
            feelingUsuario = feels[int(FeelingNum)-1]
            print("Te quieres sentir: "+feelingUsuario)
            break

        
    return feelingUsuario

def modificar(query):

    #password = input("Ingrese la contraseña de la Base de Datos")
    password = "12345678"

    db = Neo4jDatabase("bolt://localhost:7687", "neo4j", password)

    #CONSULTA
    db.run_query(query)


    db.close()

def buscar(query,nodeType):

    devuelta = []

    #password = input("Ingrese la contraseña de la Base de Datos")
    password = "12345678"

    db = Neo4jDatabase("bolt://localhost:7687", "neo4j", password)

    #CONSULTA
    result = db.run_query(query)
    atributo = " "
    dic = " "

    if (nodeType == "SONG"):
        dic = "s"
        atributo = "Title"
    elif(nodeType == "FEELING"):
        dic = "f"
        atributo = "Feeling"
    elif(nodeType == "ARTIST"):
        dic = "a"
        atributo = "name"
    elif(nodeType == "GENRE"):
        dic = "g"
        atributo = "type"

    for record in result:
        objeto = record
        texto = objeto[dic][atributo]
        devuelta.append(texto)
        #print(texto)
    
    return devuelta

    db.close()

#buscar("MATCH (s:SONG) RETURN s LIMIT 5","SONG")
#buscar("MATCH (f:FEELING)-[:LO_TRANSMITE]->(s:SONG) WHERE s.Title = 'Monster' RETURN f","FEELING")
#buscar("MATCH (f:FEELING) RETURN f","FEELING")
#buscar("MATCH (g:GENRE) RETURN g","GENRE")

#password = input("Ingrese la contraseña de la Base de Datos")
menu()