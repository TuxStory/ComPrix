#!/usr/bin/python3
# 14/07/2022
# Version 0.0.5 (Don't judge it now)
# Antoine Even

import pandas as pd

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
    Data["Date"] = pd.to_datetime(Data["Date"])
    sorted_df = Data.sort_values("Date")
    return sorted_df   

def Filtre(Data,Item):
    data = Data[Data.Article == Item] #data = Data[Data.Article == 'Coca 33cl']
    return data                       #df.query('ctg == "B" and val > 0.5')

def main():
    #Variable et lecture des données
    quit = False
    Tab = DataList()

    #Boucle
    while quit != True:
        Action = Menu()
        print ("="*48)
        if Action == "Q":
            quit = True
            
        if Action == "1":
            ListProd = Unique(Tab)
            print(ListProd)
            print ("\n")
            
        if Action == "2":
            ListMag = Magasin(Tab)
            print(ListMag)
            print ("\n")
            
        if Action == "3":
            Article = input ("Nom du produit désiré : ")
            Fil = Filtre(Tab,Article)
            Tri2 = Sorted(Fil)
            print(Tri2)
            print ("\n")
        
        if Action == "4":
            Article = input ("Nom du produit désiré : ")
            Fil = Filtre(Tab,Article)
            Chrono = Date(Fil)
            print(Chrono)
            print ("\n")
            
        if Action == "5":
            Tri = Sorted(Tab)
            print(Tri)
            print ("\n")

if __name__=="__main__":
    main()
