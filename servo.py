'''
Objet servo 
paramètre vitesse de déplacement
tempo(ms) entre chaque degre lors du déplacement
angle de départ = 0

import servo 
servo0 = servo.servo (0,-90,90,800,3100,10)  #broche,angle_min,angle_max,duty_cycle_min,duty_cycle_max,vitesse=0

'''


from machine import Pin, PWM , ADC
import time 
def map_range(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

class servo() :
    def __init__(self,broche,angle_min,angle_max,duty_cycle_min,duty_cycle_max,vitesse=0) :
        self.servo = PWM(Pin(broche))        
        self.servo.freq(20)
        self.duty_cycle_min = duty_cycle_min
        self.duty_cycle_max = duty_cycle_max
        self.angle_min = angle_min
        self.angle_max = angle_max
        self.vitesse = vitesse
        self.angle_init = 0
        
         
    def rotation(self, angle) :
        if angle > self.angle_init :
            for i in range (self.angle_init,angle,1) :
                val_duty_cycle = map_range(i,self.angle_min,self.angle_max,self.duty_cycle_min,self.duty_cycle_max)
                self.servo.duty_u16(val_duty_cycle)
                time.sleep_ms(self.vitesse)
        else :
            for i in range (self.angle_init,angle,-1) :
                val_duty_cycle = map_range(i,self.angle_min,self.angle_max,self.duty_cycle_min,self.duty_cycle_max)
                self.servo.duty_u16(val_duty_cycle)
                time.sleep_ms(self.vitesse)
        self.angle_init = angle
