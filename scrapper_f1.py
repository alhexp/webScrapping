import datetime, requests, os, re
from bs4 import BeautifulSoup

file = 'list_url.txt'
def readURL(line_number):
    i = 0
    with open(file, 'r') as archivo:
        for line in archivo:
            if i == line_number:
                return line.split('::')[0], line.split('::')[1]
            i = i + 1

def writeURL(line_number, string):
    i = 0
    with open(file, 'w') as archivo:
        for line in archivo:
            print(line)
            if i == line_number:
                pass
                print(string)
                #archivo.write(string)
                break

def main():
    title, url = readURL(line_number=0)
    respuesta = requests.get(url)
    contenido = BeautifulSoup(respuesta.text, 'lxml')
    cc = {'href':'', 'chapter': 0}
    for chap in contenido.find_all('a', attrs={'class': 'btn btn-block purple darken-3'}):
        cc['chapter'] = int(chap.get('href').split('-')[1])
        cc['href'] = chap.get('href')
    msg = ''
    if cc['chapter'] > int(url.split('-')[1]):
        url = cc['href']
        url_write = title + '::' + url
        writeURL(line_number=0, string=url_write)
        respuesta = requests.get(url)
        contenido = BeautifulSoup(respuesta.text, 'lxml')
        msg = 'New chapter found'
    else:
        msg = 'No news chapters found'
    print(msg)

if __name__ == "__main__":
    main()