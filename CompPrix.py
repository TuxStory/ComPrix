#!/usr/bin/python3
# 14/07/2022
# Version 0.0.2
# Antoine Even

import pandas as pd

def DataList():
    Data = pd.read_csv("ArticlesData.csv")
    return Data

def Sorted(Data):
    sorted_df = Data.sort_values("Prix")
    return sorted_df

def Filtre(Data):
    data = Data[Data.Article == 'Coca 33cl']
    return data
#df.query('ctg == "B" and val > 0.5')

def main():
    Tab = DataList()
#    print (Tab)
    Tri = Sorted(Tab)
    print (Tri)
    print ("="*48)
    Fil = Filtre(Tab)
    print (Fil)
    print ("="*48)
    Tri2 = Sorted(Fil)
    print (Tri2)

if __name__=="__main__":
    main()
