#RP2
from machine import Pin, PWM
import time 
pwm0 = PWM(Pin(0))      # create PWM object from a pin
pwm0.freq(50)         # set frequency

while True : 
    pwm0.duty_u16(7500)         # get current duty cycle, range 0-65535
    time.sleep(4)           
    pwm0.duty_u16(2000)         # get current duty cycle, range 0-65535
    time.sleep(4)        


'''
#ESP32
from machine import Pin, PWM
import time 
pwm0 = PWM(Pin(15))      # create PWM object from a pin 15
pwm0.freq(50)                   # set frequency

while True :
    pwm0.duty_u16(7500)
    time.sleep(4)           
    pwm0.duty_u16(2000)
    time.sleep(4)        
'''
