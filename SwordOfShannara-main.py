from microbit import *
import random
score = 0
lives = 5

def start():
    display.show(Image('88088:'
                       '88088:'
                       '08880:'
                       '08880:'
                       '08880:'))
    
    sleep(1000)
    display.show(Image.SWORD)
    sleep(1000)
   # display.scroll('Retrieve the Sword!')
def BldForest():
    land = []
    skulls = []
    for i in range(100):
        land.append(random.randrange(3))
        if random.randrange(100) < 33:
            skulls.append(1)
        else:
            skulls.append(0)
    sword = 33 + random.randrange(33)
    land [sword] = 3 # set location of the Sword of Shannara
    return (land,skulls)

    
def dispWrld(loc,land,skulls):
    global score
    global lives
    display.clear()
    
    for i in range(5):
        spot = (100 + (loc + i))%100
        if skulls[spot]== 1:
            display.set_pixel(i,0,8) #skullbearer
        if land[spot]>0:
            if land[spot] == 2:
                display.set_pixel(i,3,6)
            display.set_pixel(i,4,6)
            if land[spot]==3: #display sword
                display.set_pixel(i,2,9)
                display.set_pixel(i,3,9)
                display.set_pixel(i,4,9)
                if i == 1: #game over
                    score = score + 1000
                    lives = 0
                    display.show(Image.SWORD)
            display.set_pixel(1,4,9)
    display.set_pixel(1,3,9)
    
    
def ElfStones(loc,land,skulls):
    global score
    spot = (100 + (loc +1))%100
    if skulls[spot]==1: #skullbearer above
        skulls[spot] = 0 #zap, it is gone
        score = score + random.randrange(7)*5+5
        display.clear()
        display.show(Image.DIAMOND_SMALL)
        sleep(250)
        display.show(Image.DIAMOND)
        sleep(250)
        dispWrld(loc,land,skulls)

def SkullHit(loc,land,skulls):
    global lives
    spot = (100 + (loc +1))%100
    if skulls[spot]==1: #skullbearer above
        lives = lives - 1
        display.clear()
        display.show(Image.SKULL)
        sleep(500)
        dispWrld(loc,land,skulls)


    
start()
(land,skulls) = BldForest()

loc = 0
Done = False
while not Done:    
    dispWrld(loc,land,skulls)

    if button_a.was_pressed():
        if button_b.was_pressed():
            ElfStones(loc,land,skulls)
        else:
            loc = (100 + loc -1)%100 
    if button_b.was_pressed():
        if button_a.was_pressed():
            ElfStones(loc,land,skulls)
        else:
            loc = (100 + loc +1)%100 
    if accelerometer.was_gesture('shake'):
            ElfStones(loc,land,skulls)    
    if random.randrange(20)>17:
        SkullHit(loc,land,skulls)
    sleep(200)
    if lives <= 0 :
        Done = True
while True:
    display.scroll("Game Over")   
    display.scroll("Score: " + str(score) )