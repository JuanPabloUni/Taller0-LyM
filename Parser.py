alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else"]
metodos=[]
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
           bool=comparadormetodos(palabra, indice)
           palabra = ""
         else:
           noencontrado.add()
              
  def comparadormetodos(palabra:str, indice:int)->bool:
    valor_verdad=False
    if palabra == "drop":
      valor_verdad=comparardrop(lineas:string, indice:int)
    elif palabra == "walkm":
      valor_verdad=compararwalkmultiple(lineas:string, indice:int)    
    elif palabra == "jump":
      valor_verdad=compararjump(lineas:string, indice:int)
    elif palabra == "jumpTo":
      valor_verdad=compararjumpTo(lineas:string, indice:int) 
    elif palabra == "veer":
      valor_verdad=compararveer(lineas:string, indice:int)
    elif palabra == "look":
      valor_verdad=compararlook(lineas:string, indice:int)
    elif palabra == "grab":
      valor_verdad=comparargrab(lineas:string, indice:int)
    elif palabra == "get":
      valor_verdad=compararget(lineas:string, indice:int)
    elif palabra == "free":
      valor_verdad=compararfree(lineas:string, indice:int)      
    elif palabra == "pop":
      valor_verdad=compararpop(lineas:string, indice:int)
    elif palabra == "isfacing":
      valor_verdad=compararisfacing(lineas:string, indice:int)
    elif palabra == "isValid":
      valor_verdad=compararisValid(lineas:string, indice:int)
    elif palabra == "canWalk":
      valor_verdad=compararcanwalkmultiple(lineas:string, indice:int)
    elif palabra == "not":
      valor_verdad=compararnot(lineas:string, indice:int)
    else:
      valor_verdad=False
    return valor_verdad  
   
  


  
  def comparardrop(lineas:string, indice:int)->bool:
  def compararwalkmultiple(lineas:string, indice:int)->bool:
  def compararjump(lineas:string, indice:int)->bool:
  def compararjumpTo(lineas:string, indice:int)->bool:
  def compararveer(lineas:string, indice:int)->bool:
  def compararlook(lineas:string, indice:int)->bool:
  def comparargrab(lineas:string, indice:int)->bool:
  def compararget(lineas:string, indice:int)->bool:
  def compararfree(lineas:string, indice:int)->bool:
  def compararpop(lineas:string, indice:int)->bool:
  def compararisfacing(lineas:string, indice:int)->bool:
  def compararisValid(lineas:string, indice:int)->bool:
  def compararcanwalkmultiple(lineas:string, indice:int)->bool:
  def compararnot(lineas:string, indice:int)->bool:
  
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      estructuras si no esta sacar el nombre e ir a posicion y evaluar
      
      
      
      
      
      
      
      
      
      
    
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
