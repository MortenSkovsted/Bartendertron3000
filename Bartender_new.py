import guizero
from gpiozero import LED
import ReadDrinksTXT as MyDrinks
from pumpconfig import GetIngridentsPumpDict

pumpdict = GetIngridentsPumpDict()
pumpleddict = {}
for pumpname, led in pumpdict.values():
    temp = LED(led)
    temp.on()
    pumpleddict[pumpname] = temp


def unpackstring(string):
    #'[0, 'Gin&Tonic', ['Gin', 'Tonic'], [50, 25]]'
    #To [0, 'Gin&Tonic', ['Gin', 'Tonic'], [50, 25]]
    string = string[1:-1]
<<<<<<< HEAD
    
print(unpackstring("[0, 'Gin&Tonic', ['Gin', 'Tonic'], [50, 25]]"))

def PressDrinkButton():
    
    guizero.info("Dear Sir/Madam", "Your drink will be ready soon")
=======

print(unpackstring("[0, 'Gin&Tonic', ['Gin', 'Tonic'], [50, 25]]"))

def PressDrinkButton():

    guizero.info("Dear Sir/Madam", "You'er drink will be ready soon")
>>>>>>> e1856f4529bc40e669bdbe2a7f00bc1255faaf09
    #pumpdict = GetIngridentsPumpDict()
    #ingredients = drink_choice.value.split(',')[2]
    print(drink_choice.value)
    MyDrinks.PourDrink(drink_choice.value, pumpleddict)
<<<<<<< HEAD
    
    #amounts = int(drink_choice.value.split(',')[3])
    #print(amounts)
    #drinkzip = zip(ingredients,amounts)
    
    #print(set(drinkzip))
    #drinkzip = sorted(set(drinkzip), key=lambda x:x[1])
    #print(drinkzip)
        
=======

    #amounts = int(drink_choice.value.split(',')[3])
    #print(amounts)
    #drinkzip = zip(ingredients,amounts)

    #print(set(drinkzip))
    #drinkzip = sorted(set(drinkzip), key=lambda x:x[1])
    #print(drinkzip)

>>>>>>> e1856f4529bc40e669bdbe2a7f00bc1255faaf09
    #t = 0
    #for i, drink in enumerate(drinkzip):
    #    ingredient = drink[0]
    #    volumen = drink[1]
    #    print(ingredient)
    #    print(volumen)
    #    for j in range(i,len(drinkzip)):
    #        print(drinkzip[j][0])
    #        print('Pump to led ' + pumpdict[drinkzip[j][0]][1])
<<<<<<< HEAD
                
    #    print('for ' + (volumen*pump_ml_to_s)-t + ' sec')
    #    t += volumen*pump_ml_to_s
    #print(ingredients)
    
    
=======

    #    print('for ' + (volumen*pump_ml_to_s)-t + ' sec')
    #    t += volumen*pump_ml_to_s
    #print(ingredients)

>>>>>>> e1856f4529bc40e669bdbe2a7f00bc1255faaf09



drinks = MyDrinks.FinalDrinksList()
#print(drinks)

drinknames = [drinkid[1] for drinkid in drinks]

<<<<<<< HEAD
app = guizero.App(title="BartenderTron 3000")
=======
app = guizero.App(title="Bartendertron3000")
>>>>>>> e1856f4529bc40e669bdbe2a7f00bc1255faaf09

drink_choice = guizero.Combo(app, options=drinknames, grid=[1,0], align="left")

choice_drink = guizero.PushButton(app, command=PressDrinkButton, text="Pour drink", grid=[1,3], align="left")

app.display()
