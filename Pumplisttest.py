from gpiozero import LED
from pumpconfig import GetIngridentsPumpDict

pumpdict = GetIngridentsPumpDict()
print(pumpdict)
pumpleddict = {}
for pumpname, led in pumpdict.values():
    print(pumpname)
    print(led)
    temp = LED(led)
    temp.on()
    pumpleddict[pumpname] = temp
    
print(pumpleddict)