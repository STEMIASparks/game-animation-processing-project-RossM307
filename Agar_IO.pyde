import random
x = 250
y = 250
diameter = 50
highscore = 0
speed = 2
aispeed = 1.5
spawn = 25
pos = []
aispawn = 0
aix = 0
aiy = 0
aisize = 0
n = 0
ain = 0
gameover = True
played = True
matchingpositions = False
aimatchingpositions = False
aispawned = False
spawnpointset = False 
reset = False
def setup():
    fullScreen()
    background(255,255,255)
def draw():
    global grid,x,y,diameter,highscore,speed,aispeed,spawn,pos,aispawn,aix,aiy,aisize,n,ain,gameover,played,matchingpositions,aimatchingpositions,aispawned,spawnpointset,reset
    background(255)
    msx = mouseX
    msy = mouseY
    # Resets variables at the beggining of each game
    if reset == True:
        x = 250
        y = 250
        diameter = 50
        speed = 2
        aispeed = 1.5
        spawn = 25
        pos = []
        aispawn = 0
        aix = 0
        aiy = 0
        aisize = 0
        n = 0
        ain = 0
        matchingpositions = False
        aimatchingpositions = False
        aispawned = False
        spawnpointset = False
        reset = False
    noStroke()
    # Fills the position array with x coordinates, y coordinates and rgb values for each orb
    while len(pos) < spawn:
        pos.append([random.randint(50,1500),random.randint(50,750),random.randint(0,255),random.randint(0,255),random.randint(0,255)])
    # Draws each orb
    for po in pos:
        fill(po[2],po[3],po[4])
        circle(po[0],po[1],10)
    fill(20,20,255)
    # Makes the player follow the cursor
    if gameover == False:
        if msy > y:
            y += speed
            circle(x,y,diameter)
        if msy < y:
            y -= speed
            circle(x,y,diameter)
        if msx > x:
            x += speed
            circle(x,y,diameter)
        if msx < x:
            x -= speed
            circle(x,y,diameter)
    if msx == x and msy == y:
        circle(x,y,diameter)
    # Checks if the player is in range of any of the orbs in the array
    for po in pos:
        if po[0] in range(x-diameter/2,x+diameter/2) and po[1] in range(y-diameter/2,y+diameter/2):
            matchingpositions = True
    # If the player is in range of an orb it will increase your diameter by 2 and remove that orb from the spawning array
    if matchingpositions == True:
        n = 0
        while n < len(pos):
            if pos[n][0] in range(x-diameter/2,x+diameter/2) and pos[n][1] in range(y-diameter/2,y+diameter/2):
                pos.pop(n)
                matchingpositions = False
                diameter += 2
            else:
                n +=1
    # Starts the AI spawning process when you reach a certain diameter
    if diameter >= (55 + aispawn * 10) and aispawned == False:
        aispawn += 1
        aispawned = True
        spawnpointset = False
        print("working")
    # Randomly sets the AI position and size
    if aispawned == True and spawnpointset == False:
        aix = random.randint(0,1) * 1000
        print(aix)
        aiy = random.randint(0,1) * 1000
        print(aiy)
        aisize = diameter + random.randint(2 * aispawn,20 * aispawn)
        spawnpointset = True
    # Makes the Ai follow the players position.
    if aispawned == True:
        fill(255,0,0)
        if aiy > y:
            aiy -= aispeed
            circle(aix,aiy,aisize)
        if aiy < y:
            aiy += aispeed
            circle(aix,aiy,aisize)
        if aix > x:
            aix -= aispeed
            circle(aix,aiy,aisize)
        if aix < x:
            aix += aispeed
            circle(aix,aiy,aisize)
        if aix == x and aiy == y:
            circle(aix,aiy,aisize)
    # Checks if the AI is in range of one of the orbs.
    for po in pos:
        if po[0] in range(int(aix)-aisize/2,int(aix)+aisize/2) and po[1] in range(int(aiy)-aisize/2,int(aiy)+aisize/2):
            aimatchingpositions = True
    # If the AI is in range removes the orb from the array
    if aimatchingpositions == True:
        ain = 0
        while ain < len(pos):
            if pos[ain][0] in range(int(aix)-aisize/2,int(aix)+aisize/2) and pos[ain][1] in range(int(aiy)-aisize/2,int(aiy)+aisize/2):
                pos.pop(ain)
                aimatchingpositions = False
                if aisize <= 500:
                    aisize += 2
            else:
                ain +=1
    # If the AI and player get in range of eachother it either removes the AI or gives player Game over screen
    if aix in range(x-diameter/2,x+diameter/2) and aiy in range (y-diameter/2,y+diameter/2):
        print("working")
        if diameter >= aisize:
            diameter += aisize/4
            aispawned = False
        else:
            gameover = True
    # Shows the current score and the highscore of the session 
    if gameover == False:
        textSize(52)
        fill(0,0,0)
        text(str(diameter-50),650,100)
        text("Highscore: " + str(highscore),750,100)
    # Creates the game over screen
    if gameover == True:
        if diameter > highscore:
            highscore = diameter-50
        textSize(300)
        fill(0,0,0)
        text("AGAR.IO",25,200)
        textSize(50)
        text("Your blob moves by follwing the mouse \n Consume orbs to increase your size \n Avoid the red blob unitl your big enough to consume them", 25, 400)
        textSize(100)
        text("Press Space To Start", 25, 800)
    if diameter >= 1000:
        textSize(300)
        text("SINGULARITY ACHIEVED",25,650)   
# Resets the game when space is pressed.
def keyPressed():
    global gameover,reset,speed,diameter
    if key == " ":
        if gameover == True:
            gameover = False
            reset = True
