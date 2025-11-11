import pprint

filmsDict = {
   "Batman":{
     "yearRelase": 2010,
     "imdbRating": 8.8,
     "genre":["Sci-fi", "Action", "Thriller"]   
    
   },
   "Interstellar": {
       "yearRelase": 2014,
       "imdbRating": 8.6,
       "genre": ["Sci-fi", "Drama"]
   },
    "the dark knight": {
       "yearRelase": 2008,
       "imdbRating": 9.0,
       "genre": ["Action", "Drama", "Crime"] 
    }     
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1- Buscar uma informação dentro de um dicionario alinhado
print(filmsDict["Interstellar"]["genre"])

# 2- Adicionar um novo itens
filmsDict["Batman"]["director"] = "Christopher Nolan"
print(filmsDict["Batman"])

# 3- Excluir um dicionario
del filmsDict["the dark knight"]
pp.pprint(filmsDict)