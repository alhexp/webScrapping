# get_current_date.py

import datetime
import requests

def main():
    archivo = 'current_date.txt'
    existe = False

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")    
    str = f"Current Date: {current_date}" 
    
    try:
        with open(archivo, 'a') as file:
            file.write(current_date + '\n')
            existe = True
            print("Hola mundo desde Agosto Infinito")
    except FileNotFoundError:
        pass

    if not existe:
        with open(archivo, 'w') as file:
            file.write(current_date + '\n')

if __name__ == "__main__":
    main()
