# get_current_date.py

import datetime, requests, os, re
from bs4 import BeautifulSoup

def main():
    dir = os.getcwd()
    archivo = dir + "\\" + 'current_date.txt'
    existe = False
    html_file = dir + '/public/index.html'

    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    str = f"Current Date: {current_date}"     

    try:
        with open(archivo, 'a') as file:
            file.write(str + '\n')
            existe = True            
    except FileNotFoundError:
        pass

    if not existe:
        with open(archivo, 'w') as file:
            file.write(str + '\n')
    else:
        try:        
            with open(html_file, 'r') as html:
                content = html.read()
                soup = BeautifulSoup(content, 'lxml')
                patron = soup.find('h1')                
                if patron:
                    patron.string = f'{str}'
                    print(patron)
            with open(html_file, 'w') as html:
                html.write(soup.prettify())                
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    main()
