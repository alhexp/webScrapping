# get_current_date.py

import datetime, requests, os, re
from bs4 import BeautifulSoup

def main():
    dir = os.getcwd()
    archivo = dir + "\\" + 'current_date.txt'
    existe = False
    print(os.getcwd())
    html_file = dir + '/public/index.html'
    print(html_file)

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")    
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

    try:        
        with open(html_file, 'r', encoding='utf-8') as html:
            content = html.read()
        soup = BeautifulSoup(content, 'html.parser')
        patron = soup.find('h1', text='Current Date')
        if patron:
            patron.string = f'Current Date\n%str'
        with open(html_file, 'w', encoding='utf-8') as html:
            html.write(soup.prettify())
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()
