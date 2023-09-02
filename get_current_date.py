# get_current_date.py

import datetime
import requests
import os

def main():
    dir = os.getcwd()
    archivo = dir + "\\" + 'current_date.txt'
    existe = False
    print(os.getcwd())
    print(os.listdir(dir))
    print("hello world")
    ht = os.chdir(dir + '\public')
    print(os.getcwd())

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
        with open(ht, 'w', encoding='utf-8') as html:
            html.replace('Current Date', f'Current Date\n%str', count=2)
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    main()
