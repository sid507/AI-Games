import sys, pygame,math,time,random
pygame.init()

def distance(pos,goal):
    dist=math.sqrt((pos[0]-goal[0])**2 +(pos[1]-goal[1])**2)
    return dist*100
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
playerrect=playerrect.move([55,325])

#--------------------------Init Logging Variables------------------------------
trials=0
min_ind=-1
feedback=[]
prev_choice=[]
for i in range (width):
    temp=[]
    for j in range (height):
        temp.append(0)
    feedback.append(temp)

#---------------------------------------Init Physics-------------------------------------------
g=1

direction=0
flag=0
sleeper=0
#--------------------------------------Loop of Trials---------------------------------------------------
while 1: 
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()
    trials+=1
    i=-1
    print("Trial Number : "+str(trials))
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render(str(trials), True, [0,0,0], [255,255,255])
    text_rect=text.get_rect()
    ai_event=0
    jump=0
    flag=0
    choice=[]
    if(trials!=1):
        
        playerrect = player.get_rect()
        playerrect=playerrect.move([55,325])
        
        
    #------------------------------------Game Loop-------------------------------------------------
    while 1:
        ai_event=0
        quit_flag=0
        direction=0
        bottom_sensor=[int(playerrect.centerx),int(playerrect.centery)+30]
        left_sensor=[int(playerrect.centerx- 35),int(playerrect.centery)]
        right_sensor=[int(playerrect.centerx+35),int(playerrect.centery)]
        up_sensor=[int(playerrect.centerx),int(playerrect.centery)-20]
        events = pygame.event.get()
        left_feed=feedback[int(playerrect.centerx- 5)][int(playerrect.centery+g - jump)]
        right_feed=feedback[int(playerrect.centerx+5)][int(playerrect.centery+g - jump)]
        
        if(level.get_at(bottom_sensor)==(0,0,0,255)):
            jump_feed=feedback[up_sensor[0]][up_sensor[1]]
        else:
            jump_feed=feedback[int(playerrect.centerx)][int(playerrect.centery + g - jump)]
        #print(jump_feed," ",right_feed," ",left_feed)
        if(right_feed==left_feed and left_feed==jump_feed): #all 3 equal
            #print("hey")
            ai_event=random.choice([1,2,3])
        #--------------------------2 equal and greater than 3rd-------------
        elif(right_feed==left_feed and right_feed>jump_feed):
            ai_event=random.choice([1,2])
        elif(right_feed==jump_feed and right_feed>left_feed):
            ai_event=random.choice([2,3])
        elif(jump_feed==left_feed and left_feed>right_feed):
            ai_event=random.choice([1,3])
        #--------------------------------------------------------------
        #--------------------1 greatest------------------------------------
        elif(right_feed>left_feed and right_feed>jump_feed):
            ai_event=2
        elif(left_feed>jump_feed and left_feed>right_feed):
            ai_event=1
        elif(jump_feed>right_feed and jump_feed>left_feed):
            ai_event=3
        #print(ai_event," ",left_feed," ",jump_feed," ",right_feed)
        """
        for event in events:
            if event.type == pygame.KEYDOWN: 
                #if event.key == pygame.K_LEFT:
                   # direction = -1
                #if event.key == pygame.K_RIGHT:
                    #direction = 1
                if event.key == pygame.K_SPACE :
                   if(level.get_at(bottom_sensor)==(0,0,0,255)): 
                        jump=20
        """
        if ai_event==3:
            if(level.get_at(bottom_sensor)==(0,0,0,255)): 
                jump=20
        keys=pygame.key.get_pressed()
        if ai_event==1:
            if(left_sensor[0]>0):
                direction=-1
            else:
                quit_flag=1
        if ai_event==2:
            if(right_sensor[0]<width):
                direction=1
            else:
                quit_flag=1
        
        if(level.get_at(bottom_sensor)!=(0,0,0,255)):
            g=2
        else:
            g=0
        speed=[direction*5,g-jump]
        if(jump>0):
            jump-=g
        original_pos=playerrect.center
        playerrect=playerrect.move(speed)
        #-----------------------------------------
        feedback[playerrect.centerx][playerrect.centery]+=(distance(original_pos,goalrect.center)-distance(playerrect.center,goalrect.center))
        choice.append([playerrect.centerx,playerrect.centery])
        if(quit_flag==1):
            break
        #print(feedback[playerrect.centerx][playerrect.centery])
        #----------------------------------------------
        #screen.fill("level.png")
        screen.blit(level,[0,0])
        screen.blit(goal,goalrect)
        screen.blit(player, playerrect)
        screen.blit(text,text_rect)
        if(playerrect.collidepoint([goalrect.centerx,goalrect.centery])):
            screen.blit(victory,[250,200])
            flag=1
        pygame.display.flip()
        time.sleep(sleeper)
        if(flag==1):
                for coord in choice:
                    feedback[coord[0]][coord[1]]*=2
                time.sleep(1)
                #flag=0
                sleeper=0.0001
                break
    #--------------------------------End Of Game Loop----------------------------
    if choice==prev_choice and flag!=1:
        for coord in choice:
                    feedback[coord[0]][coord[1]]/=2
        
    prev_choice=choice
    #write_list(feedback,choice)
#----------------------------------------End of All Trials-----------------------------------------------------    
 
