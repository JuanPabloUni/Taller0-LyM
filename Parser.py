#Lists containing all of the possible reserved words, methods and conditionals in the program in question.
alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else", "around"]
metodos=["drop", "walk", "jump", "jumpTo", "veer", "look", "grab", "get", "free", "pop", "PROC", "do", "go",  "if", "while", "repeatTimes"]
condiciones =["isfacing", "isValid", "canWalk", "not"]
metodosnoconocidos=[]
variables=[]
parametros=[]
walk=["north", "south", "east", "west","right", "left", "front", "back"]
facing=["north", "south", "east", "west"]
listaveer=["right", "left","around"]

#Main method, which opens and reads the .txt file and calls upon all other methods and prints the final result.
def Parser()->bool:
  try:

    path = input("\nPlease type the file path to parse: ")
    file = open(path, "r")
    output = True

    """
    codigo anterior, el que esta fuera ahora lee todo el archivo en string
    lineas=[]
    for line in file:
      lineas.append(line)
    """

    lineas = file.read().replace("\n", " ")
    file.close()
    lineas.strip()
    output = recorrer(lineas)
    if(output==True):
      print("\nThe program is written correctly.\n")
    else:
      print("\nThe program is written incorrectly. Sintax error.\n")
  
  except FileNotFoundError:
    print("\nFile not found. Please try again.")
    Parser()

#Method used to go over the whole .txt file in String form, calling the methods that verify sintax.
def recorrer(lineas:str)->bool:
  palabra = ""
  indice=0
  flag=True

  if lineas[0]=="P" and lineas[1]=="R" and lineas[2]=="O" and lineas[3]=="G":  
    if lineas[-1]=="P" and lineas[-2]=="R" and lineas[-3]=="O" and lineas[-4]=="G":
        flag=True
    else:
        flag=False
  else:
      flag=False

  indice =4    
      while indice2< len(lineas)-5: 
        palabra2+=lineas[indice2]
          if lineas[indice2+1]==",":
            variables.append(palabra2)
            palabra2=""
            indice2+=1
          elif lineas[indice2-1]=="," and lineas[indice2+1]==";":
            variables.append(palabra2)
            palabra2=""     
        indice2+=1  
      diferencia=indice2-indice
      indice+=diferencia
    indice+=1
  return flag

#Method used to determine which reserved word is identified and call the corresponding verifier.
def compararmetodos(palabra:str, indice:int, lineas:str)->tuple:
  tuplaverdadindice=(False, 0)
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
    """
  elif palabra == "PROG":
    tuplaverdadindice=compararPROG(lineas, indice)
    """
  elif palabra == "PROC":
    tuplaverdadindice=compararPROC(lineas, indice)
  elif palabra == "go":
    tuplaverdadindice=comparargo(lineas, indice)
  elif palabra == "if":
    """
    tuplaverdadindice=compararif(lineas, indice)
  elif palabra == "GORP":
    """
    tuplaverdadindice=compararGORP(lineas, indice)
  elif palabra == "while":
    tuplaverdadindice=compararwhile(lineas, indice)
  elif palabra == "repeatTimes":
    tuplaverdadindice=compararrepeatTimes(lineas, indice)
  else:
    tuplelist = list(tuplaverdadindice)
    tuplelist[0]=False
    tuplaverdadindice = tuple(tuplelist)
  return tuplaverdadindice

#Method used to determine which conditional is identified and call the corresponding verifier.
def compararcondicionales(palabra:str, indice:int, lineas:str)->tuple:
  tuplaverdadindice=(False,0)
  if palabra == "isfacing":
    tuplaverdadindice=compararisfacing(lineas, indice)
  elif palabra == "isValid":
    tuplaverdadindice=compararisValid(lineas, indice)
  elif palabra == "canWalk":
    tuplaverdadindice=compararcanwalkmultiple(lineas, indice)
  elif palabra == "not":
    tuplaverdadindice=compararnot(lineas, indice)
  else:
    tuplelist = list(tuplaverdadindice)
    tuplelist[0]=False
    tuplaverdadindice = tuple(tuplelist)
  return tuplaverdadindice

#Methods used to individually asses the the sintax of every declared method in the .txt file.
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
              longitudactual_2+=1          
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

def compararjumpTo(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  longitudactual=0
  indice4=0
  palabra2=""
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+2 :
      for indicevar in variables:
        for indicepar in parametros:
          palabra+=lineas[indice3]
          if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
            longitudactual = lineas[indice3+len(palabra)]
      indice3+=1
  if longitudactual!=0:          
    if lineas[len(longitudactual)+1]==",":
      indice4=longitudactual+1
      while indice4<= indice4+2 :
        for indicevar in variables:
          for indicepar in parametros:
            palabra2+=lineas[indice4]
            if palabra == indicepar or palabra == indicevar or palabra.isdigit() == True:
              longitudactual = lineas[indice4+len(palabra2)]   
              sintaxis = True
        indice4+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

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
  return tupla

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
  indice2 = indice
  sintaxis = False
  palabra = ""
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

def compararisfacing(lineas:str, indice:int)->tuple:
  indice2= indice
  sintaxis = False
  palabra =""
  indice3 = indice2+1
  if lineas[indice2+1]=="(":
    while indice3 <= indice3+5 :
      for indiceface in facing:
        palabra+=lineas[indice3]
        if palabra == indiceface:
          longitudactual = lineas[indice3+len(palabra)]
          if lineas[len(longitudactual)+1]==")":
            sintaxis = True
      indice3+=1
  longitud = len(longitudactual+1)
  tupla =(longitud,sintaxis)
  return tupla

def compararisValid(lineas:str, indice:int)->tuple:
  pass

def compararcanwalkmultiple(lineas:str, indice:int)->tuple:
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
              longitudactual_2+=1          
      indice3+=1
  longitud = len(longitudactual3+1)
  tupla =(longitud,sintaxis)
  return tupla


def compararnot(lineas:str, indice:int)->tuple:
  if lineas[indice+1] == "(":
    pass
  pass
"""
def compararPROG(lineas:str, indice:int)->tuple:
  sintax = False
  if indice ==4:
    sintax=True
  tupla =(indice,sintax)
  return tupla
"""
def compararPROC(lineas:str, indice:int)->tuple:
    sintaxis = False
    indice2=indice+1
    palabra=""
    if lineas[indice2]+1=="(":
        indice2+=1
        while indice2 <= len(lineas):
            carac=lineas[indice2]
            palabra+=carac
            if lineas[indice2+1]==",":
                parametros.add(palabra)
                palabra=""
                indice2+=1
                indice2+=len(palabra) 
            elif lineas[indice2+1]==")" and lineas[indice2-1]==",":
                parametros.add(palabra)
                palabra=""
                indice2+=1
                indice2+=len(palabra)
                sintaxis = True 
            indice2+1

    longitud = indice2
    tupla =(longitud,sintaxis)
    return tupla
  
def compararif(lineas:str, indice:int)->tuple:
  pass
"""
def compararGORP(lineas:str, indice:int)->tuple:
  sintax = False
  longitud = len(lineas)
  if indice ==longitud:
    sintax=True
  tupla =(indice,sintax)
  return tupla
"""
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
        sintaxis = compararcondicionales(palabra, indice, lineas)
      indice+=1
  else:
    sintaxis = False

def compararrepeatTimes(lineas:str, indice:int)->tuple:
  pass

#Lines of code which call upon the main method and start the parser method as a whole.
print("\n---Welcome to the Java Program Parser---")
Parser()




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
