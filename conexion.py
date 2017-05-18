import requests

url = "http://localhost:9000/cupon"

def insertarCupones(listaCuponesJSON):
    for cupon in listaCuponesJSON:
        #print("id: " + str(cupon["id"]))
        #print("imagen: " + cupon["imagen"])
        #print("informacion: " + cupon["informacion"])
        #print("precioActual: " + cupon["precioActual"])
        #print("ahorro: " + cupon["ahorro"])
        #print("finaliza: " + cupon["finaliza"])
        #print("tipo: " + cupon["tipo"])
        r = requests.post(url, data=cupon)
        print(r.text)
        print(r.status_code)

