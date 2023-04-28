#RP2 + potentiometre + fonction map_range  
from machine import Pin, PWM , ADC
import time 
servo0 = PWM(Pin(0))      # create PWM object from a pin
servo0.freq(50)         # set frequency

adc = ADC(Pin(26))     # create ADC object on ADC pin

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True :
    valeur_pot = adc.read_u16()    # read value, 0-65535 
    val_duty_cycle = map_range(valeur_pot,0,65535,2000,7500)   #duty_cycle min = 800 duty_cycle_max = 3100
    servo0.duty_u16(val_duty_cycle)     
    time.sleep_ms(20)




