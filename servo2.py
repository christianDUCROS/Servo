#RP2 + potentiometre
from machine import Pin, PWM , ADC
import time 
servo0 = PWM(Pin(0))      # create PWM object from a pin
servo0.freq(50)         # set frequency

adc = ADC(Pin(26))     # create ADC object on ADC pin

while True :
    valeur_pot = adc.read_u16()    # read value, 0-65535 
    servo0.duty_u16(int(5500*valeur_pot/65535 + 2000))    #duty_cycle min = 800 duty_cycle_max = 3100
    time.sleep_ms(20)
