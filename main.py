import csv
import pandas


def cargar_csv(file_name):
    df = pandas.read_csv(file_name, sep = ',')
    print(df)

def cargar_excell(file_name):
    df = pandas.read_excel(file_name, sep = ',')
    print(df)

def menu1():
    print("""
- · MENU DE OPCIONES · -
          
-> 1: Cargar datos csv
-> 2: Cargar datos excel
-> 3: Salir del programa
""")
    option = int(input(": "))

    if option == 1:
        file_name = str(input("file_name: "))
        cargar_csv(file_name)

    if option == 2:
        file_name = str(input("file_name: "))
        cargar_excell(file_name)
        



menu1()