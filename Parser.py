alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else"]
metodos=["drop", "free", "walk", "PROC","canWalk", "do", "walk", "od", "fi", "go", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if"]
encontrado =[]
noencontrado=[]
programas = []

def Parser()->bool:
  path = input("\nPorfavor digite el path del archivo: ")
  file = open(path, "r")
  """
  codigo anterior, el que esta fuera ahora lee todo el archivo en string
  lineas=[]
  for line in file:
    lineas.append(line)
   """
  lineas = file.read().replace("\n", " ")
  file.close()
  lineas.strip()

  def recorrer(lineas:)->str:
     palabra = ""
     noecontrado=""
     for indice in range(len(lineas)):
       caracter = lineas[indice]
       palabra+caracter
       for indicea in range(len(metodos)):
         token = cadena[indicea]
         if palabra in token:
           encontrado.add()
           bool=comparadormetodos(palabra, indice, )
           palabra = ""

              
  def comparadormetodos(palabra:str, indice:int, lineas:str)->bool:
    valor_verdad=False
    if palabra == "drop":
      valor_verdad=comparardrop(lineas:str, indice:int)
    elif palabra == "walkm":
      valor_verdad=compararwalkmultiple(lineas:str, indice:int)    
    elif palabra == "jump":
      valor_verdad=compararjump(lineas:str, indice:int)
    elif palabra == "jumpTo":
      valor_verdad=compararjumpTo(lineas:str, indice:int) 
    elif palabra == "veer":
      valor_verdad=compararveer(lineas:str, indice:int)
    elif palabra == "look":
      valor_verdad=compararlook(lineas:str, indice:int)
    elif palabra == "grab":
      valor_verdad=comparargrab(lineas:str, indice:int)
    elif palabra == "get":
      valor_verdad=compararget(lineas:str, indice:int)
    elif palabra == "free":
      valor_verdad=compararfree(lineas:str, indice:int)      
    elif palabra == "pop":
      valor_verdad=compararpop(lineas:str, indice:int)
    elif palabra == "isfacing":
      valor_verdad=compararisfacing(lineas:str, indice:int)
    elif palabra == "isValid":
      valor_verdad=compararisValid(lineas:str, indice:int)
    elif palabra == "canWalk":
      valor_verdad=compararcanwalkmultiple(lineas:str, indice:int)
    elif palabra == "not":
      valor_verdad=compararnot(lineas:str, indice:int)
    else:
      valor_verdad=False
    return valor_verdad  
   
  


  
  def comparardrop(lineas:str, indice:int)->tuple:
    pass
  def compararwalkmultiple(lineas:str, indice:int)->tuple:
    pass
  def compararjump(lineas:str, indice:int)->tuple:
    pass
  def compararjumpTo(lineas:str, indice:int)->tuple:
    pass
  def compararveer(lineas:str, indice:int)->tuple:
    pass
  def compararlook(lineas:str, indice:int)->tuple:
    pass
  def comparargrab(lineas:str, indice:int)->tuple:
    pass
  def compararget(lineas:str, indice:int)->tuple:
    pass
  def compararfree(lineas:str, indice:int)->tuple:
    pass
  def compararpop(lineas:str, indice:int)->tuple:
    pass
  def compararisfacing(lineas:str, indice:int)->tuple:
    pass
  def compararisValid(lineas:str, indice:int)->tuple:
    pass
  def compararcanwalkmultiple(lineas:str, indice:int)->tuple:
    pass
  def compararnot(lineas:str, indice:int)->tuple:
    pass
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      # estructuras si no esta sacar el nombre e ir a posicion y evaluar
      
      
      
      
      
      
      
      
      
      
    
                """ 
            else:
              noencontrado=palabra
              for indicea in range(len(alfabeto)):
                token = cadena[indicea]
                if token in noencontrado:
                  noencontrado=""
                     """

                  
        
        
        

          
        
"""  
def verificador(lineas:list)->bool:
  for lineap in lineas:
    comparador(lineap)
   
def comparador(lineacomparada: str)->bool:
  palabra=""
  for letra in lineacomparada:
    palabra+= letra
    if(palabra in metodos):
      if palabra = "if":
        compararif()
"""
  
# file1 = open("Text.txt", "r")
# print(file1.read())

# file = open("Text.txt", "r")
# for line in file:
#   print(line)

print("\nBienvenido al parser de programas de Java\n")
Parser()
