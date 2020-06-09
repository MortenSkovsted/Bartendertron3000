# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:04:45 2020

@author: morte
"""


# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import wx
import ReadDrinksTXT as MyDrinks
from pumpconfig import GetIngridentsPumpDict


########################################################################
class Drink:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, id, name, ingredients, amounts):
        """Constructor"""
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.amounts = amounts     
      

    
    
########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self,parent,id):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "BartenderTron 3000", size = (700,420))

        # Add a panel so it looks the correct on all platforms
        panel = wx.Panel(self, wx.ID_ANY)
        
        drinkslist = MyDrinks.FinalDrinksList()
        drinks = []
        
        #Test if there is only one available drink
        if type(drinkslist[0]) == int:
            drinks = Drink(drinkslist[0], drinkslist[1], drinkslist[2], drinkslist[3])
        
        elif type(drinkslist[0]) == list:
            for drink in drinkslist:
                drinks.append(Drink(drink[0], drink[1], drink[2], drink[3]))
        else:
            print("Error in MyForm__init__")
        
        #drinks = [Drink(0, "Gin&Tonic", ["Gin","Tonic"], [25,75]),    Old hardcoded
        #        Drink(1, "Rum&Cola", ["Rom","Cola"], [25,75]),
        #        Drink(2, "Old Fashioned", ["Rom","Sirup","Angostura Bitters"], [50,50,5])]

        sampleList = []
        self.cb = wx.ComboBox(panel,
                              size= (200, 100),
                              choices=sampleList)
        self.widgetMaker(self.cb, drinks)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.cb, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        
        #Drink_btn = wx.Button(self, label='Pour Drink', pos=(100, 100))
        #self.Drink_btn.Bind(wx.EVT_BUTTON, self.onDrinkClick)
        
        

        
        
        
        
        button = wx.Button(panel, label = 'Pour Drink', pos=(300, 160), size = (100,60))
        self.Bind(wx.EVT_BUTTON, self.PourDrink, button)

    def PourDrink(self, event):
        obj = self.cb.GetClientData(self.cb.GetSelection())
        pumpdict = GetIngridentsPumpDict()
        pump_ml_to_s = 130/150          #150 ml in 130 sec
        
        print(f"You must be thirsty for {obj.name}")
        drinkzip = zip(obj.ingredients, obj.amounts)
        #print(set(drinkzip))
        drinkzip = sorted(set(drinkzip), key=lambda x:x[1])
        print(drinkzip)
        
        t = 0
        for i, drink in enumerate(drinkzip):
            ingredient = drink[0]
            volumen = drink[1]
            print(ingredient)
            for j in range(i,len(drinkzip)):
                print(f'Pump to led {pumpdict[drinkzip[j][0]][1]}')
                
            print(f'for {(volumen*pump_ml_to_s)-t} sec')
            t += volumen*pump_ml_to_s
        #print(f"{obj.ingredients}")
        #print(f"{obj.amounts}")



    #----------------------------------------------------------------------
    def widgetMaker(self, widget, objects):
        """"""
        for obj in objects:
            widget.Append(obj.name, obj)
        widget.Bind(wx.EVT_COMBOBOX, self.onSelect)

    #----------------------------------------------------------------------
    def onSelect(self, event):
        """"""
        print( "You selected: " + self.cb.GetStringSelection())
        obj = self.cb.GetClientData(self.cb.GetSelection())
        text = """
        The object's attributes are:
        %s  %s    %s  %s

        """ % (obj.id, obj.name, obj.ingredients, obj.amounts)
        print(text)



# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm(parent=None,id = -1)
    frame.Show()
    app.MainLoop()