import sys, pygame,math,time
pygame.init()

#-----------------Init Graphics-----------------------------
size = width, height = 700, 500
speed = 5
angle=-90
black = 0, 0, 0

screen = pygame.display.set_mode(size)
victory=pygame.image.load("victory.png")
#goal=pygame.image.load("goal.png")
og_goal=pygame.image.load("goal.png")
goal=og_goal.copy()
goalrect=goal.get_rect()
goalrect=goalrect.move([650,125])
level=pygame.image.load("level.png").convert()
og_player = pygame.image.load("player.png")
player=og_player.copy()
#player=pygame.transform.rotate(player, -180)
playerrect = player.get_rect()
playerrect=playerrect.move([50,325])

#--------------------------Init Logging Variables------------------------------
trials=0
min_ind=-1
feedback=[]
for i in range (height):
    temp=[]
    for j in range (width):
        temp.append(0)
    feedback.append(temp)
#choice=[]
#---------------------------------------Init Physics-------------------------------------------
g=1
jump=0
direction=0
flag=0
#--------------------------------------Loop of Trials---------------------------------------------------
while 1: 
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()
    trials+=1
    i=-1
    print("Trial Number : "+str(trials))
    
    if(trials!=1):
        
        playerrect = player.get_rect()
        playerrect=playerrect.move([50,325])
        
        
    #------------------------------------Game Loop-------------------------------------------------
    while 1:
        direction=0
        bottom_sensor=[int(playerrect.centerx),int(playerrect.centery)+35]
        left_sensor=[int(playerrect.centerx- 35),int(playerrect.centery)]
        right_sensor=[int(playerrect.centerx+35),int(playerrect.centery)]
        up_sensor=[int(playerrect.centerx),int(playerrect.centery)-20]
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                   # direction = -1
                #if event.key == pygame.K_RIGHT:
                    #direction = 1
                if event.key == pygame.K_SPACE:
                   if(level.get_at(bottom_sensor)==(0,0,0,255)): 
                        jump=20
       
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if(left_sensor[0]>0):
                direction=-1
        if keys[pygame.K_RIGHT]:
            if(right_sensor[0]<width):
                direction=1
        
        if(level.get_at(bottom_sensor)!=(0,0,0,255)):
            g=2
        else:
            g=0
        speed=[direction*3,g-jump]
        if(jump>0):
            jump-=g
        playerrect=playerrect.move(speed)
        
        #screen.fill("level.png")
        screen.blit(level,[0,0])
        screen.blit(goal,goalrect)
        screen.blit(player, playerrect)
        if(playerrect.collidepoint([goalrect.centerx,goalrect.centery])):
            screen.blit(victory,[250,200])
            flag=1
        pygame.display.flip()
        time.sleep(0.01)
        if(flag==1):
                time.sleep(1)
                flag=0
                break
    #--------------------------------End Of Game Loop----------------------------
    #write_list(feedback,choice)
#----------------------------------------End of All Trials-----------------------------------------------------    
 
