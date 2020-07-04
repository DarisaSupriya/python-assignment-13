#program to remove an item of a tuple
tupley="w",3,"r","s","o","u","r","c","e"
print(tupley)
tupley=tupley[:2]+tupley[3:]
print(tupley)
listx=list(tupley)
listx.remove("c")
tupley=tuple(listx)
print(tupley)
