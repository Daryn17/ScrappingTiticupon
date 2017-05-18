import json

def craerJSON(id ,imagen, informacion, precioActual, ahorro, finaliza, tipo, precioOriginal, lugar, periodoDeUso, horario, comoLlegar):
    cuponJSON = {"id":id, "imagen":imagen, "informacion":informacion, "precioActual":precioActual, "ahorro":ahorro, "finaliza":finaliza,
                 "tipo":tipo, "precioOriginal":precioOriginal, "lugar":lugar, "periodoDeUso":periodoDeUso, "horario":horario, "comoLlegar":comoLlegar}
    return cuponJSON