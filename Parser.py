alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else", "around"]
metodos=["drop", "walk", "jump", "jumpTo", "veer", "look", "grab", "get", "free", "pop", "PROC", "do", "go",  "if", "GORP", "while", "repeatTimes"]
condiciones =["isfacing", "isValid", "canWalk", "not"]
variables=[]
parametros=[]
walk=["north", "south", "east", "west","right", "left", "front", "back"]
listaveer=["right", "left","around"]

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
    indice+=1
    
def comparadormetodos(palabra:str, indice:int, lineas:str)->tuple:
  tuplaverdadindice=(False,0)
  if palabra == "drop":
    tuplaverdadindice=comparardrop(lineas, indice)
  elif palabra == "walkm":
    tuplaverdadindice=compararwalkmultiple(lineas, indice)    
  elif palabra == "jump":
    tuplaverdadindice=compararjump(lineas, indice)
  elif palabra == "jumpTo":
    tuplaverdadindice=compararjumpTo(lineas, indice) 
  elif palabra == "veer":
    tuplaverdadindice=compararveer(lineas, indice)
  elif palabra == "look":
    tuplaverdadindice=compararlook(lineas, indice)
  elif palabra == "grab":
    tuplaverdadindice=comparargrab(lineas, indice)
  elif palabra == "get":
    tuplaverdadindice=compararget(lineas, indice)
  elif palabra == "free":
    tuplaverdadindice=compararfree(lineas, indice)      
  elif palabra == "pop":
    tuplaverdadindice=compararpop(lineas, indice)
  elif palabra == "isfacing":
    tuplaverdadindice=compararisfacing(lineas, indice)
  elif palabra == "isValid":
    tuplaverdadindice=compararisValid(lineas, indice)
  elif palabra == "canWalk":
    tuplaverdadindice=compararcanwalkmultiple(lineas, indice)
  elif palabra == "not":
    tuplaverdadindice=compararnot(lineas, indice)
  elif palabra == "PROG":
    tuplaverdadindice=compararPROG(lineas, indice)
  elif palabra == "PROC":
    tuplaverdadindice=compararPROC(lineas, indice)
  elif palabra == "go":
    tuplaverdadindice=comparargo(lineas, indice)
  elif palabra == "if":
    tuplaverdadindice=compararif(lineas, indice)
  elif palabra == "GORP":
    tuplaverdadindice=compararGORP(lineas, indice)
  elif palabra == "while":
    tuplaverdadindice=compararwhile(lineas, indice)
  elif palabra == "repeatTimes":
    tuplaverdadindice=compararrepeatTimes(lineas, indice)
  else:
    valor_verdad=False
  return valor_verdad  
   
def comparardrop(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararwalkmultiple(lineas:str, indice:int)->tuple:
  bool = False
  if indice+3 == ")":#se podria mirar
    tuplasimple = compararwalksimple(lineas, indice)
  else:
    tuplacompuesta = compararwalkcompuesto(lineas, indice)
  if tuplasimple[0]==False or tuplacompuesta[0]==False:
    bool=False
  indicefinal =indice
  tupla= (True,indicefinal)
  return tupla

def compararwalksimple(lineas, indice)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2:
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
                sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla = (longitud,sintaxis)
  return tupla

def compararwalkcompuesto(lineas, indice)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  palabra2=""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+5 :
      for indicewalk in walk:
        palabra+=lineas[indice3]
        if palabra == indicewalk:
          longitudactual = lineas[indice3+len(palabra)]
          if lineas[len(longitudactual)+1]==",":
            longitudactual_2+=1
            while longitudactual_2<=longitudactual+1:
              palabra2+=lineas[longitudactual]
              for indicevar in variables:
                for indicepar in parametros:
                  if palabra2 == indicepar or palabra2 == indicevar or palabra2.isdigit() == True:
                    longitudactual3 = lineas[longitudactual+len(palabra2)]
                    if lineas[len(longitudactual3)+1]==")":
                      sintaxis = True
    indice3+=1
  longitud = len(longitudactual3+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararjump(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla
    
  pass
def compararjumpTo(lineas:str, indice:int)->tuple:
  pass
def compararveer(lineas:str, indice:int)->tuple:
  sintaxis = False
  indice2=indice+1
  palabra=""
  if lineas[indice2]=="(":
    while indice2<=indice2+6:    
      for indicevar in listaveer:
        palabra+=lineas[indice2]
        if palabra == indicevar:
          longitudtemp = lineas[indice2+len(palabra)]
          if lineas[longitudtemp+1]==")":
            sintaxis = True
      indice2+=1    
  longitud = len(longitudtemp+1)
  tupla =(longitud,sintaxis)
  pass
def compararlook(lineas:str, indice:int)->tuple:
  pass
def comparargrab(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararget(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit()==True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararfree(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() ==True:
            longitudactual = lineas[indice3+len(palabra)]
            if lineas[len(longitudactual)+1]==")":
              sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararpop(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar on parametros:
          palabra+=lineas[indice3]
            if  palabra== indicepar or palabra == indicevar or isDigit(palabra)==True:
              longitudactual = lineas[indice3+len(palabra)]
                if lineas[len(longitudactual)+1]==")"
                  sintaxis = True
    indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

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
  sintaxis = False
  flag = False
  longitudcondicional=9
  palabra=""
  if lineas[indice+1]=="(":
    indice+=1
    while indice <= indice+9 and not flag:
      palabra+=lineas[indice]
      if(palabra in condiciones):
        flag = True
        sintaxis = compararcondicionales(lineas, indice, palabra)
      indice+=1
  else:
    sintaxis = False

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
