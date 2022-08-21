#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 1
from machine import Pin as pin
from utime import sleep, sleep_ms
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

para=0.01
while True:
        #led 1
    led1.value(1)
    sleep(para)
    led1.value(0)
    sleep(para)
        #Led 2
    led2.value(1)
    sleep(para)
    led2.value(0)
    sleep(para)
        #Led 3
    led3.value(1)
    sleep(para)
    led3.value(0)
    sleep(para)
        #Led 4
    led4.value(1)
    sleep(para)
    led4.value(0)
    sleep(para)
        #Led 5
    led5.value(1)
    sleep(para)
    led5.value(0)
    sleep(para)
        #Led 6
    led6.value(1)
    sleep(para)
    led6.value(0)
    sleep(para)
        #Led 7
    led7.value(1)
    sleep(para)
    led7.value(0)
    sleep(para)
        #Led 8
    led8.value(1)
    sleep(para)
    led8.value(0)
    sleep(para)
       #Led 9
    led9.value(1)
    sleep(para)
    led9.value(0)
    sleep(para)
       #Led 10
    led10.value(1)
    sleep(para)
    led10.value(0)
    sleep(para)

    