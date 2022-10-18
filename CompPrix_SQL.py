#!/usr/bin/python3
# 17/10/2022
# Version 0.0.2
# Antoine Even

import sqlite3
from tabulate import tabulate

# Connection à la base de donnée SQLite
connection = sqlite3.connect("ArticlesData.db")
print(connection.total_changes)
cursor = connection.cursor()

def Menu():
    print("1. Afficher la liste des produits.")
    print("2. Afficher la liste des enseignes.")
    print("3. Afficher la liste d'un produit par prix.")
    print("4. Afficher la liste d'un produit par date.")
    print("5. Afficher les données.")
    print("Q. Sortir du programme.")
    Choix = input("Votre choix [1-5] : ")
    return Choix

def Unique():
    rows = cursor.execute("SELECT DISTINCT Article FROM ArticlesData").fetchall()
    Data = tabulate(rows)
    return Data

def Magasin():
    rows = cursor.execute("SELECT DISTINCT Enseigne FROM ArticlesData").fetchall()
    Data = tabulate(rows)
    return Data

def Filtre(Article):
    rows = cursor.execute("Select * FROM ArticlesData WHERE Article= ? order by Prix",(Article,)).fetchall()
    Data = tabulate(rows)
    return Data

def Filtre2(Article):
    rows = cursor.execute("Select * FROM ArticlesData WHERE Article= ?",(Article,)).fetchall()
    Data = tabulate(rows)
    return Data

def DataList():
    rows = cursor.execute("SELECT * FROM ArticlesData order by prix").fetchall()
    Data = tabulate(rows)
    return Data

def Press():
    print ("\n")
    input("Appuyer sur 'Entrer' pour continuer...")

def main():
    quit = False

    #boucle
    while quit != True:
        Action = Menu()
        print("="*51)
        if Action == "Q" or Action == "q":
            print(">>> Bye!")
            quit = True

        if Action == "1":
            Tab = Unique()
            print (Tab)
            Press()

        if Action == "2":
            Tab = Magasin()
            print (Tab)
            Press()

        if Action == "3":
            Article = input ("Nom du produit désiré : ")
            Tab = Filtre(Article)
            print (Tab)
            Press()

        if Action == "4":
            Article = input ("Nom du produit désiré : ")
            Tab = Filtre2(Article)
            print (Tab)
            Press()

        if Action == "5":
            Tab = DataList()
            print (Tab)
            Press()

if __name__=="__main__":
    main()
