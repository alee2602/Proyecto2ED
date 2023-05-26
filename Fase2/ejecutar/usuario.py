
class Usuario:
    
    # class attribute
    

    def __init__(self,name,feeling,genre):
        self.name = name
        self.feeling = feeling
        self.genre = genre


#CREAR USUARIO
def CrearUsuario(name,feeling,genre):
    
    usu1 = Usuario(name,feeling,genre)
    
    print("Hola,"+usu1.name+"!")
    if len(usu1.genre) >1:
        print("Tus géneros favoritos son")
        for i in usu1.genre:
            print("- "+i)
    else:
        print("Tu género favorito es el "+usu1.genre[0])

        
    


        
        
