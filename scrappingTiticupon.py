from bs4 import BeautifulSoup
import urllib.request
import cuponJSON
import conexion
import psycopg2


cuponesJSON = []

def scrappingTiti():

    source = urllib.request.urlopen('https://www.titicupon.com/').read()
    soup = BeautifulSoup(source, 'html.parser')
    cuponSquares = soup.find_all('div', attrs={"class": "grid-item"})
    count = 0
    for cuponSquare in cuponSquares:
        count+=1


        imagen = cuponSquare.find('img', attrs={"class": "imagecache imagecache-coupon-slider-responsive"})['src']

        informacion = cuponSquare.find('h4', attrs={"class":"product-title"}).get_text()
        informacion = informacion.strip()

        precio = cuponSquare.find('span', attrs={"class":"max-price"}).get_text()

        ahorro = cuponSquare.find('span', attrs={"class":"ahorro-small"}).get_text()

        finaliza = cuponSquare.find('span', attrs={"class":"date-display-single"}).get_text()

        tipo = cuponSquare.find('h5', attrs={"class":"tag-icon"}).get_text()
        tipo = tipo.strip()

        id = count

        URL = cuponSquare.find('div', attrs={"class": "btn-wrapper"})

        a = "https://www.titicupon.com"
        a = a + URL.find('a')['href']

        print(a)

        #cupon = cuponJSON.craerJSON(id,imagen,informacion,precio,ahorro,finaliza,tipo)

        #cuponesJSON.append(cupon)

        if(count == 1):
            break


def getCuponesJSON():
    scrappingTiti()
    #conexion.insertarCupones(cuponesJSON)

getCuponesJSON()