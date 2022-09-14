#!/usr/bin/python3
# 14/07/2022
# Version 0.1.0 (Don't judge it now)
# Antoine Even

import pandas as pd

pd.set_option('display.max_rows', None) # Pour afficher toutes les lignes du DF, 10 par défaut.
pd.set_option('display.expand_frame_repr', False)

def Menu():
    print("1. Afficher la liste des produits.")
    print("2. Afficher la liste des enseignes.")
    print("3. Afficher la liste d'un produit par prix.")
    print("4. Afficher la liste d'un produit par date.")
    print("5. Afficher les données.")
    print("Q. Sortir du programme.")
    Choix = input("Votre choix [1-5] : ")
    return Choix

def DataList():
    try:
        Data = pd.read_csv("ArticlesData.csv")
        return Data
    except:
        print ("[ Erreur ] Avec le fichier des données ou les données")

def Unique(Data):
    Data = Data.sort_values("Article")
    Data = Data['Article']
    unique_df = Data.drop_duplicates()
    return unique_df

def Magasin(Data):
    Data = Data.sort_values("Enseigne")
    Data = Data['Enseigne']
    Magasin_df = Data.drop_duplicates()
    return Magasin_df

def Sorted(Data):
    sorted_df = Data.sort_values("Prix")
    return sorted_df

def Date(Data):
    DF = Data.copy() #Copie de la DataFrame pour eviter les warnings.
    DF["Date"] = pd.to_datetime(DF["Date"])
    sorted_df = DF.sort_values("Date")
    return sorted_df

def Filtre(Data,Item):
    data = Data[Data.Article == Item] #data = Data[Data.Article == 'Coca 33cl']
    return data                       #df.query('ctg == "B" and val > 0.5')

def Press():
    print ("\n")
    input("Appuyer sur 'Entrer' pour continuer...")

def main():
    #Variable et lecture des données
    quit = False
    Tab = DataList()

    #Boucle
    while quit != True:
        Action = Menu()
        print ("="*51)
        if Action == "Q" or Action == "q":
            print (" >>> Bye!")
            quit = True

        if Action == "1":
            ListProd = Unique(Tab)
            print(ListProd)
            Press()

        if Action == "2":
            ListMag = Magasin(Tab)
            print(ListMag)
            Press()

        if Action == "3":
            Article = input ("Nom du produit désiré : ")
            Fil = Filtre(Tab,Article)
            Tri2 = Sorted(Fil)
            print(Tri2)
            Press()

        if Action == "4":
            Article = input ("Nom du produit désiré : ")
            Fil = Filtre(Tab,Article)
            Chrono = Date(Fil)
            print(Chrono)
            Press()

        if Action == "5":
            Tri = Sorted(Tab)
            print(Tri)
            Press()

if __name__=="__main__":
    main()
