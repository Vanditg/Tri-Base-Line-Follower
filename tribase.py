import RPi.GPIO as GPIO
#import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
#IR SENSOR INPUTS

GPIO.setup(3,GPIO.IN)	#i                            
GPIO.setup(5,GPIO.IN)	#j
GPIO.setup(7,GPIO.IN)	#k
GPIO.setup(8,GPIO.IN)	#l
GPIO.setup(10,GPIO.IN)	#m
GPIO.setup(21,GPIO.IN)  #n
#MOTORS

#MOTOR A
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)    #PWM PIN
PWM=GPIO.PWM(38,100)
GPIO.setup(40,GPIO.OUT)

#MOTOR B
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)	   #PWM PIN
Left_pwm=GPIO.PWM(13,100)
GPIO.setup(15,GPIO.OUT)
#MOTOR C
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)    #PWM PIN
Right_pwm=GPIO.PWM(16,100)
GPIO.setup(18,GPIO.OUT)

#MOTOR OUTPUTS

GPIO.output(36,0)
GPIO.output(40,0)
GPIO.output(15,0)
GPIO.output(11,0)
GPIO.output(12,0)
GPIO.output(18,0)

#CONDITIONS

while True:

          i=GPIO.input(3)                         
          j=GPIO.input(5)
	  k=GPIO.input(7)
	  l=GPIO.input(8)
	  m=GPIO.input(10)
	  n=GPIO.input(21)

	  if i==1 and j==1 and k==0 and l==0 and m==1 and n==1:
         
	       print  "Forward",i,j,k,l,m,n      
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,1)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
	       Left_pwm.start(50)
#motorC
	       GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(50)
	  
	  elif i==1 and j==1 and k==0 and l==0 and m==0 and n==1:

               print  "little bit right",i,j,k,l,m,n
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,0)
	       PWM.start(10)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(50)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(50)

	  elif i==1 and j==0 and k==0 and l==0 and m==1 and n==1:

               print  "little bit left",i,j,k,l,m,n
#motorA        
               GPIO.output(36,0)
               GPIO.output(40,1)
               PWM.start(10)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(50)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(50)

	  elif i==1 and j==1 and k==1 and l==0 and m==0 and n==1:

               print  "little right",i,j,k,l,m,n
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,0)
               PWM.start(15)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(45)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(45)

	  elif i==1 and j==0 and k==0 and l==1 and m==1 and n==1:

               print  "little left",i,j,k,l,m,n
#motorA        
               GPIO.output(36,0)
               GPIO.output(40,1)
               PWM.start(15)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(45)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(45)

	  elif i==1 and j==1 and k==1 and l==1 and m==0 and n==0:

               print  "Right",i,j,k,l,m,n
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,0)
               PWM.start(25)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(40)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(40)

	  elif i==0 and j==0 and k==1 and l==1 and m==1 and n==1:

               print  "left",i,j,k,l,m,n
#motorA        
               GPIO.output(36,0)
               GPIO.output(40,1)
               PWM.start(25)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(40)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(40)

	  elif i==1 and j==1 and k==1 and l==1 and m==1 and n==0:

               print  "sharp right",i,j,k,l,m,n
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,0)
               PWM.start(30)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(40)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(40)

	  elif i==0 and j==1 and k==1 and l==1 and m==1 and n==1:

               print  "sharp left",i,j,k,l,m,n
#motorA        
               GPIO.output(36,0)
               GPIO.output(40,1)
               PWM.start(30)
#motorB
               GPIO.output(11,0)
               GPIO.output(15,1)
               Left_pwm.start(40)
#motorC
               GPIO.output(12,1)
               GPIO.output(18,0)
               Right_pwm.start(40)

	  elif i==1 and j==1 and k==1 and l==1 and m==1 and n==1:

               print  "backward",i,j,k,l,m,n
#motorA        
               GPIO.output(36,1)
               GPIO.output(40,1)
               
#motorB
               GPIO.output(11,1)
               GPIO.output(15,0)
               Left_pwm.start(70)
#motorC
               GPIO.output(12,0)
               GPIO.output(18,1)
               Right_pwm.start(70)

GPIO.Cleanup()
