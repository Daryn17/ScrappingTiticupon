import requests, json
import httplib
import urllib

# Host y archivo
host = "http://localhost:9000"

URL = "http://localhost:9000"


def insertarCupones(listaCuponesJSON):
    for cupon in listaCuponesJSON:
        # print("Id: " + str(cupon["id"]))
        # print("Imagen: " + cupon["imagen"])
        # print("Inforación: " + cupon["inforacion"])
        # print("Precio: " + cupon["precio"])
        # print("Ahorro: " + cupon["ahorro"])
        # print("Finaliza: " + cupon["finaliza"])
        # print("Tipo: " + cupon["tipo"])
        # r = requests.post(URL + '/cupon', params=cupon)
        # print(r.status_code, r.reason)
        # paquetes necesarios

        target = "/cupon"
        # cabeceras HTTP usando sintaxis NOMBRE:VALOR
        # si haces un GET, deberías modificar o eliminar la primera cabecera
        headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "application/xhtml+xml,text/html;q=0.9,text/plain;",
            "Referer": "http://www.UnApagina.com/login/ok.php"
        }
        # parametros POST, si solo quieres una peticion get no hacen falta
        params = urllib.urlencode(cupon)
        # conectamos con el host remoto
        conn = httplib.HTTPConnection(host)
        # mandamos la peticion POST con los parametros y las cabeceras anteriores
        # para un get sería lo mismo pero poniendo get y sin parametros
        conn.request("POST", target, params, headers)
        # vemos que narices ha pasado en la petición
        response = conn.getresponse()
        print(response.status, response.reason)
        # y si todo ha ido bien ahora imprimiremos los resultados :)
        data = response.read()
        print(data)
        conn.close()

# -----------------------------------------------------
