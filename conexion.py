

def insertarCupones(listaCuponesJSON):
    for cupon in listaCuponesJSON:
        print(cupon)
        print("id: " + str(cupon["id"]))
        print("imagen: " + cupon["imagen"])
        print("informacion: " + cupon["informacion"])
        print("precio: " + cupon["precio"])
        print("ahorro: " + cupon["ahorro"])
        print("finaliza: " + cupon["finaliza"])
        print("tipo: " + cupon["tipo"])

