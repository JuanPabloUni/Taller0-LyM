alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else"]
metodos=["drop", "walk", "jump", "jumpTo", "veer", "look", "grab", "get", "free", "pop", "PROC", "do", "go",  "if", "GORP", "while", "repeatTimes"]
condiciones =["isfacing", "isValid", "canWalk","not"]


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

def recorrer(lineas:str)->str:
  palabra = ""
  indice=0
  while indice <= len(lineas):
    caracter = lineas[indice]
    palabra+caracter
    for indicea in range(len(metodos)):
      token = metodos[indicea]
      if palabra in token:
        resultado=comparadormetodos(palabra, indice, lineas)
    indice += resultado[1]
         
def comparadormetodos(palabra:str, indice:int, lineas:str)->tuple:
  tuplaverdadidnice=(False,0)
  if palabra == "drop":
    tuplaverdadidnice=comparardrop(lineas, indice)
  elif palabra == "walkm":
    tuplaverdadidnice=compararwalkmultiple(lineas, indice)    
  elif palabra == "jump":
    tuplaverdadidnice=compararjump(lineas, indice)
  elif palabra == "jumpTo":
    tuplaverdadidnice=compararjumpTo(lineas, indice) 
  elif palabra == "veer":
    tuplaverdadidnice=compararveer(lineas, indice)
  elif palabra == "look":
    tuplaverdadidnice=compararlook(lineas, indice)
  elif palabra == "grab":
    tuplaverdadidnice=comparargrab(lineas, indice)
  elif palabra == "get":
    tuplaverdadidnice=compararget(lineas, indice)
  elif palabra == "free":
    tuplaverdadidnice=compararfree(lineas, indice)      
  elif palabra == "pop":
    tuplaverdadidnice=compararpop(lineas, indice)
  elif palabra == "isfacing":
    tuplaverdadidnice=compararisfacing(lineas, indice)
  elif palabra == "isValid":
    tuplaverdadidnice=compararisValid(lineas, indice)
  elif palabra == "canWalk":
    tuplaverdadidnice=compararcanwalkmultiple(lineas, indice)
  elif palabra == "not":
    tuplaverdadidnice=compararnot(lineas, indice)
  elif palabra == "PROG":
    tuplaverdadidnice=compararPROG(lineas, indice)
  elif palabra == "PROC":
    tuplaverdadidnice=compararPROC(lineas, indice)
  elif palabra == "go":
    tuplaverdadidnice=comparargo(lineas, indice)
  elif palabra == "if":
    tuplaverdadidnice=compararif(lineas, indice)
  elif palabra == "GORP":
    tuplaverdadidnice=compararGORP(lineas, indice)
  elif palabra == "while":
    tuplaverdadidnice=compararwhile(lineas, indice)
  elif palabra == "repeatTimes":
    tuplaverdadidnice=compararrepeatTimes(lineas, indice)
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
def compararPROG(lineas:str, indice:int)->tuple:
  pass  
def compararPROC(lineas:str, indice:int)->tuple:
  pass
def comparargo(lineas:str, indice:int)->tuple:
  pass  
def compararif(lineas:str, indice:int)->tuple:
  pass  
def compararGORP(lineas:str, indice:int)->tuple:
  pass
def compararwhile(lineas:str, indice:int)->tuple:
  pass
def compararrepeatTimes(lineas:str, indice:int)->tuple:
  pass

#       # estructuras si no esta sacar el nombre e ir a posicion y evaluar
#                 """ 
#             else:
#               noencontrado=palabra
#               for indicea in range(len(alfabeto)):
#                 token = cadena[indicea]
#                 if token in noencontrado:
#                   noencontrado=""
#                      """     
# """  
# def verificador(lineas:list)->bool:
#   for lineap in lineas:
#     comparador(lineap)
   
# def comparador(lineacomparada: str)->bool:
#   palabra=""
#   for letra in lineacomparada:
#     palabra+= letra
#     if(palabra in metodos):
#       if palabra = "if":
#         compararif()
# """
  
# file1 = open("Text.txt", "r")
# print(file1.read())

# file = open("Text.txt", "r")
# for line in file:
#   print(line)

print("\nBienvenido al parser de programas de Java\n")
Parser()
