# get_current_date.py

import datetime

def main():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    print(current_date)

if __name__ == "__main__":
    main()
