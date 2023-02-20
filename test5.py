import csv 
import matplotlib.pyplot as plt
# import PyQt5                      / GUI Coming soon as possible. It`a hard work, bro.
# from bs4 import BeautifulSoup     / Web scraping library, extract data from html/xml
# import requests                   / Coming soon in future if possible...

def draw():
    data_list = []
    with open("date.txt") as file3:
        file_reader3 = csv.reader(file3)
        for row in file_reader3:
            data_list.append(row[0])

    pulse = []
    with open("pulse.txt") as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            pulse.append(row[0])

    sys_list = []
    with open("sys.txt") as file1:
        file_reader1 = csv.reader(file1)
        for row in file_reader1:
            sys_list.append(row[0])

    dia_list = []
    with open("dia.txt") as file2:
        file_reader2 = csv.reader(file2)
        for row in file_reader2:
            dia_list.append(row[0])


    x = data_list
    y1 = sys_list
    y2 = dia_list
    y3 = pulse

    plt.title('Blood Pressure & Pulse')
    plt.xlabel(xlabel='Date')
    plt.ylabel(ylabel='Value')
    plt.plot(x, y1, label='sys', color='red')
    plt.plot(x, y2, label='dia', color='blue')
    plt.plot(x, y3, label='pulse', color='green')
    plt.grid()
    plt.draw()
    plt.legend(loc='upper left')
    plt.show()


# import pandas as pd                 # Data-analytiikka library/modul
# import matplotlib.pyplot as plt     # Draw library
# import PyQt5                      / GUI Coming soon as possible. It`a hard work, bro.
# from bs4 import BeautifulSoup     / Web scraping library, extract data from html/xml
# import requests                   / Coming soon in future if possible...

# Funktio: Tallentaminen SYS,DIA,PULE,DATA -tiedoston uusi riville csv-tiedoston
# def add(veri_sys, veri_dia, veri_pulse, veri_data):
#    with open('tiedot.csv', 'a', encoding='utf-8') as file:  # Avaa tiedosto "a"(Add)-muodossa
#        paine_tiedot = f'{veri_data};{veri_sys};{veri_dia};{veri_pulse}\n'
#        file.write(paine_tiedot)
#       print('Tallenettu CSV-tiedoston!')


# Pääohjelma
while True:
    command = int(input("""
        Verepaine tallenusohjelma! Blood pressure mega-analysing soft!
    
    Valitse numero / Take your choice, please:
    1 - Lisää mittaustiedot     / Add new Blood pressure measurements-data
    2 - Kuva                    / Draw the Graphic of collected date
    3 - Lopeta ohjelma          / Exit!
    Numero?: """))

    if command == 1:  # Lisää verepainelaite mittaukset tiedoston
        veri_sys = input('SYS: ')
        with open("sys.txt",'a') as sysfile:3
            sysfile.write(str(veri_sys) + '\n')
            print('SYS-mittaus tallennettu!')
        sysfile.close()

        veri_dia = input('DIA: ')
        with open("dia.txt",'a') as diafile:
            diafile.write(str(veri_dia) + '\n')
            print('DIA-muttaus tallennettu!')
        diafile.close()

        veri_pulse = input('Pulse: ')
        with open("pulse.txt",'a') as pulsefile:
            pulsefile.write(str(veri_pulse) + '\n')
            print('Pulse-tieto tallennetuu!')
        pulsefile.close()

        veri_data = input('Date(pp.kk.vv): ')
        with open("date.txt",'a') as datefile:
            datefile.write(str(veri_data) + '\n')
            print('Date tallennettu')
        datefile.close()

#        add(veri_sys, veri_dia, veri_pulse, veri_data)

    elif command == 2:  # Kuva
        draw()

#   elif command == 3:  # tiedosto.csv luominen
#       with open('tiedot.csv', 'w', encoding='utf-8') as fle:
#            line = f'Data;SYS;DIA;PULSE\n'  # taulukon sarake-nimet
#           file.write(line)
#           print('Uusi CSV-tiedosto luotu!')

    elif command == 3:  # Exit
        print('Kiitos käynnistä ja tsemppiä!')
        break