#program to create the colon of a tuple
from copy import deepcopy
tupley=("higuy" , 5 , [] , True)
print(tupley)
tupley_colon=deepcopy(tupley)
tupley_colon[2].append(50)
print(tupley_colon)
print(tupley)
