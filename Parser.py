alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else"]
metodos=[]
encontrado =[]
noencontrado=[]
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
        caracter = cadena[indice]
        palabra+caracter
        for indicea in range(len(alfabeto)):
          token = cadena[indicea]
            if palabra in token:
              encontrado.add()
              palabra = ""
            else:
              noencontrado.add()
     
   
  
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
