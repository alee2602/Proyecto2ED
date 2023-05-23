from neo4j import GraphDatabase
class manejoDB:
    def _init_(self):
        self.conectar()
    def conectar(self):
        driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","12345678"))
        def execute_query(query):
            with driver.session() as session:
                result = session.run(query)
                return list(result)

# Ejemplo de consulta
        query = "MATCH (n) RETURN n"
        result = execute_query(query)
        generoInput = []
        generos = [] 

#Guardar Géneros en Array para preguntarlo
        for i in result:
            nodo=i["n"]
            if nodo["type"] != None:
                generos.append(nodo["type"])

#Preguntar al usuario el género musical
        while True:
            query = "MATCH (n) RETURN n"
            result = execute_query(query)
            contador = 1
            for i in result:
                nodo=i["n"]
                if nodo["type"] != None:
                    print(str(contador) +")"+ nodo["type"])
                    contador += 1
            if(generoInput):
                print("Generos seleccionados:")
                print(', '.join(generoInput))
            genero = input("Ingresa un género musical (o escribe 'fin' para terminar): ")
            

            if genero.lower() == 'fin':
                break
            if (len(generos) >= (int(genero)-1)):
                if (generos[int(genero)-1]) in generoInput:
                        print("Ya está agregado el género"+generos[int(genero)-1]+", intente con otro.")
                else:
                    generoInput.append(generos[int(genero)-1])
                    print("Se agregó:"+generoInput[-1])

            



        driver.close()
        

class buscarGen:
    def _init_(self):
        self.conectar()
    def conectar(self):
        driver=GraphDatabase.driver("bolt://localhost:7687",auth=("neo4j","12345678"))
        def execute_query(query):
            with driver.session() as session:
                result = session.run(query)
                return list(result)

#Definir query
        genre = "hip hop"

        query = "MATCH (GENRE {type: '"+genre+"'})--(SONG) RETURN SONG"
        result = execute_query(query)
        SongsGen = []
        SongsFeeling = []

#Guardar Canciones en Array
        for i in result:
            nodo=i["SONG"]
            if nodo["type"] != None:
                print(nodo["title"])




        driver.close()

app=manejoDB()
app.conectar()
#app=buscarGen()
#app.conectar()