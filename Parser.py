alfabeto = ["drop", "free", "walk", "var", "PROC", "canWalk", "do", "walk", "od", "fi", "go", "GORP", "(", ")", "{", "}", ",", ".", ";", "north", "south", "east", "west", "right", "left", "front", "back", "jump", "jumpTo", "veer", "look", "grab", "get", "pop", "if", "else"]

def Parser()->bool:
  path = input("\nPorfavor digite el path del archivo: ")
  file = open(path, "r")
  lineas=[]
  for line in file:
    lineas.append(line)

def verificador(lineas:list)->bool:
  for lineap in lineas:
    comparador(lineap)
   
def comparador(lineacomparada: str)->bool:
  palabra=""
  for letra in lineacomparada:
    palabra+= letra
    if(palabra in alfabeto):
      

# file1 = open("Text.txt", "r")
# print(file1.read())

# file = open("Text.txt", "r")
# for line in file:
#   print(line)

print("\nBienvenido al parser de programas de Java\n")
Parser()
