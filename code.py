from roboid import *


hamster = Hamster()

while True:
    key = str(Keyboard.read())
    LEFT=0
    RIGHT=0
    key=key.lower()
    SPEED=100
    status="idle"
    if key:
        if(key=='w'):
            hamster.wheels(SPEED,SPEED)
            status='forward'
        if(key=='s'):
            hamster.wheels(-100,-100)
            status='backward'
        if(key=='d'):
            hamster.wheels(100,-100)
            status='right'
        if(key=='a'):
            hamster.wheels(-100,100)
            status='left'
        if(key=="q"):
            hamster.wheels(0,0)
            status='idle'
        if(key=='65'):
            SPEED+=10
            match status:
                case "forward":
                    hamster.wheels(SPEED,SPEED)
                case "backward":
                    hamster.wheels(SPEED,SPEED)
        if(key=='66'):
            SPEED-=10

        
        
        




