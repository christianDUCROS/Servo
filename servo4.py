#RP2 + angle + fonction map_range  

from machine import Pin, PWM , ADC
import time 
servo0 = PWM(Pin(0))      # create PWM object from a pin
servo0.freq(20)         # set frequency

adc = ADC(Pin(26))     # create ADC object on ADC pin

def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


valeur_angle = 30    
val_duty_cycle = map_range(valeur_angle,-90,90,800,3100)  #duty_cycle min = 800 duty_cycle_max = 3100
servo0.duty_u16(val_duty_cycle)     


