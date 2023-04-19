#RP2 + objet servo 
import servo   #duty_cycle min = 800 duty_cycle_max = 3100
servo0 = servo.servo(0,0,180,800,3100)      # create servo  : broche0 vitesse par defaut =0 
servo1 = servo.servo(1,0,180,800,3100,100)      # create servo  : broche1 vitesse = 100 

valeur_angle = 150     
servo0.rotation(valeur_angle)

valeur_angle = 0  
servo1.rotation(valeur_angle)