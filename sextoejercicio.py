#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 6
from machine import Pin as pin
from utime import sleep as stop, sleep_ms as para,sleep_us as pausa
posipines=[13,12,14,27,26,25,33,32,18,4]
luces=[]
for i in posipines:
    luces.append  (pin(i,pin.OUT))
#print(luces)
inicial=1
final=11
def derecha(inicio,fin):
    for i in luces[inicio:fin]:
        for j in range (2):
            i.value(not i.value())
            para(150)   
def izquierda():
    for i in reversed (luces[inicio:fin]):
        for j in range (2):
            i.value(not i.value())
            para(150)
inicial-=1
#print(final)         
while True:
 derecha(inicial,final)
 #izquierda(inicial,final)
 