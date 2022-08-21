#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 5
from machine import Pin as pin
from utime import sleep as stop, sleep_ms as para,sleep_us as pausa
posipines=[13,12,14,27,26,25,33,32,18,4]
luces=[]
for i in posipines:
    luces.append  (pin(i,pin.OUT))
   # print(luces)
def derecha():
    for i in luces:
        for j in range (2):
            i.value(not i.value())
            para(150)   
def izquierda():
    for i in reversed (luces):
        for j in range (2):
            i.value(not i.value())
            para(150) 
while True:
 derecha()
 izquierda()