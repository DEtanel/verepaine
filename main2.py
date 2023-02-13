import pandas as pd                 # Data-analytiikka library/modul
import matplotlib.pyplot as plt     # Draw library
# import PyQt5                      / GUI Coming soon as possible. It`a hard work, bro.
# from bs4 import BeautifulSoup     / Web scraping library, extract data from html/xml
# import requests                   / Coming soon in future if possible...

# Funktio: Tallentaminen SYS,DIA,PULE,DATA -tiedoston uusi riville csv-tiedoston
def add(veri_sys, veri_dia, veri_pulse, veri_data):             
    with open('tiedot.csv', 'a', encoding='utf-8') as file:  #Avaa tiedosto "a"(Add)-muodossa
        paine_tiedot = f'{veri_data};{veri_sys};{veri_dia};{veri_pulse}\n' 
        file.write(paine_tiedot)   
        print('Tallenettu CSV-tiedoston!')

# Funktion: Piiristys, tiedot otetaan "tiedot.csv" tiedostosta.   
def draw():
    df = pd.read_csv('tiedot.csv', sep=';', header=0, index_col=0 )
    df.plot()
    # Achtung! Es fehlen wichtige Patameters zum Anzeigen von Linien-Farben usw...
    plt.title('Blood pressure measurements-data')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.show()

# Pääohjelma
while True:
    command = int(input("""Verepaine tallenusohjelma! Blood pressure mega-analyse soft!
    Valitse numero / Take your choice please:
    1 - Lisää tiedot    / Add new Blood pressure measurements-data
    2 - Kuva            / Draw the Graphic of collected date
    3 - Ensiasennus     / Please start at the first Program-Start!) 
    4 - Lopeta ohjelma  / Exit!
    Numero?: """))
    
    if command == 1:    # Lisää verepainelaite mittaukset tiedoston 
        veri_sys = input('SYS: ')
        veri_dia = input('DIA: ')
        veri_pulse = input('Pulse: ')
        veri_data = input('Date(pp.kk.vv): ')
        add(veri_sys, veri_dia, veri_pulse, veri_data)
    
    elif command == 2:  # Kuva
        draw() 

    elif command == 3:  # tiedosto.csv luominen
        with open('tiedot.csv', 'w', encoding='utf-8') as fle:
            line = f'Data;SYS;DIA;PULSE\n'  #taulukon sarake-nimet
            file.write(line)
            print('Uusi CSV-tiedosto luotu!')

    elif command == 4:  # Exit
        print('Kiitos ja tsemppiä!')
        break
