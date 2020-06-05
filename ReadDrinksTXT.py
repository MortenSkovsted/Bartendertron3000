# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:28:26 2020

@author: morte
"""


def GetDrinkList():

    drinksfile = open("drinks.txt")
    
    drinklist = []
    
    firstline = True
    for line in drinksfile:
        #remove newline
        if line[-1] == "\n":
            line = line[:-1]
        
        if firstline:
            firstline = False
            Drinksheader = line.split(";")

            continue
        info = line.split(";")
        drinklist.append(info)

    drinksfile.close()
    
    return drinklist


def GetActiveIngridents():
    
    ActiveIngridents = []
    
    pumpsfile = open("pumps.txt")
    firstline = True
    for line in pumpsfile:
        #remove newline, if there
        if line[-1] == "\n":
            line = line[:-1]
        
        if firstline:
            firstline = False
            pumpheader = line.split(";")

            continue
        temp = line.split(";")
        if temp[1] != "None":
            ActiveIngridents.append(temp[1])
    
    pumpsfile.close()

    return ActiveIngridents
        
def GetpumpGPIO():
    return None

def GetActiveDrinkslist():
    FullDrinksList = GetDrinkList()
    ActiveIngridents = GetActiveIngridents()
    
    ActiveDrinkList = []
    
    for drink in FullDrinksList:
        IngridentNames = drink[2:8]

        HaveAllIngrident = True
        for ingrident in IngridentNames:
            if ingrident != "None" and ingrident not in ActiveIngridents:
                HaveAllIngrident = False
        
        if HaveAllIngrident:
            ActiveDrinkList.append(drink)
    

    return ActiveDrinkList
print(GetActiveIngridents())
"""
Translate from this format:
[['0', 'Gin&Tonic', 'Gin', 'Tonic', 'None', 'None', 'None', 'None', '25', '50', 'None', 'None', 'None', 'None'],
['1', 'Rum&Tonic', 'Rum', 'Tonic', 'None', 'None', 'None', 'None', '25', '50', 'None', 'None', 'None', 'None']]
To this format

[Drink(0, "Gin&Tonic", ["Gin","Tonic"], [25,75]),
 Drink(1, "Rum&Cola", ["Rom","Cola"], [25,75]),
 Drink(2, "Old Fashioned", ["Rom","Sirup","Angostura Bitters"], [50,50,5])]
"""
def FinalDrinksList():
    UnformatedDrinkslist = GetActiveDrinkslist()
    
    
    #Test if there is only one available drink
    if type(UnformatedDrinkslist[0]) == str:
        ID = int(UnformatedDrinkslist[0])
        name = UnformatedDrinkslist[1]
        
        ingredients = []
        for ingredient in UnformatedDrinkslist[2:8]:
            if ingredient != "None":
                ingredients.append(ingredient)
                
        amounts = []
        for amount in UnformatedDrinkslist[8:]:
            if amount != "None":
                amounts.append(int(amount))
        
        return [ID, name, ingredients, amounts]
        
    
    elif type(UnformatedDrinkslist[0]) == list:
        formatedDrinkslist = []
        
        for drink in UnformatedDrinkslist:

            ID = int(drink[0])
            name = drink[1]
        
            ingredients = []
            for ingredient in drink[2:8]:
                if ingredient != "None":
                    ingredients.append(ingredient)
                
            amounts = []
            for amount in drink[8:]:
                if amount != "None":
                    amounts.append(int(amount))
        
            formatedDrinkslist.append([ID, name, ingredients, amounts])
        return formatedDrinkslist
            
        
    else:
        print(f"Error in FinalDrinksList, UnformatedDrinkslist is {UnformatedDrinkslist}")


"""
self.id = id
        self.name = name
        self.ingredients = ingredients
        self.amounts = amounts




drinks = [Drink(0, "Gin&Tonic", ["Gin","Tonic"], [25,75]),
                Drink(1, "Rum&Cola", ["Rom","Cola"], [25,75]),
                Drink(2, "Old Fashioned", ["Rom","Sirup","Angostura Bitters"], [50,50,5])]


"""

