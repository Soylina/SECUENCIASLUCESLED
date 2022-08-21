#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 3
from machine import Pin as pin
import utime
led1=pin(13,pin.OUT)
led2=pin(12,pin.OUT)
led3=pin(14,pin.OUT)
led4=pin(27,pin.OUT)
led5=pin(26,pin.OUT)
led6=pin(25,pin.OUT)
led7=pin(33,pin.OUT)
led8=pin(32,pin.OUT)
led9=pin(18,pin.OUT)
led10=pin(4,pin.OUT)
luces=[led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]

def derecha():
    for elemento in luces:
        elemento.value(1)
        utime.sleep_ms(300)
        elemento.value(0)
        utime.sleep(0.5)
def izquierda():
    for elemento in reversed (luces):
        elemento.value(1)
        utime.sleep(0.5)
        elemento.value(0)
        utime.sleep(0.5)
while True:
  izquierda()
  derecha()

