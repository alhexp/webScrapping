# get_current_date.py

import datetime
import requests
import os

def main():
    dir = os.getcwd()
    archivo = dir + "\\" + 'current_date.txt'
    existe = False
    print(os.listdir(dir))
    print("hello world")

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")    
    str = f"Current Date: {current_date}"     

    try:
        with open(archivo, 'a') as file:
            file.write(current_date + '\n')
            existe = True            
    except FileNotFoundError:
        pass

    if not existe:
        with open(archivo, 'w') as file:
            file.write(current_date + '\n')

if __name__ == "__main__":
    main()
