import json

def craerJSON(id ,imagen, informacion, precio, ahorro, finaliza, tipo):
    cuponJSON = {"id":id, "imagen":imagen, "inforacion":informacion, "precio":precio, "ahorro":ahorro, "finaliza":finaliza,"tipo":tipo}
    return cuponJSON