import pygame,time,random,sys
check_error =pygame.init()
if check_error[1]>0:
    print("!{0}had initializing errors,".format(check_error[1]))
    sys.exit(-1)

else:
    
    print("(+)python game initialized!")   
playSurface = pygame.display.set_mode((720,460))    
pygame.display.set_caption("Snake Game!")
# time.sleep(3)

##colors

red =pygame.Color(255,0,0)#gameover
green =pygame.Color(0,255,0)#snake
black =pygame.Color(0,0,0)#score
white =pygame.Color(255,255,255)#background
brown =pygame.Color(42,42,42)#food

score = 0
fpsController = pygame.time.Clock()

sPosition =[100,50]
sBody =[[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,36)*10]
foodSpawn = True
direction ="RIGHT"
changeto = direction

def GameOver():
    mFont =pygame.font.SysFont('monaco',72)
    GoSurf=mFont.render('Game Over!',True,red)
    GoRect=GoSurf.get_rect()
    GoRect.midtop=(360,15)
    playSurface.blit(GoSurf,GoRect)
    scoreBoard(0)
    pygame.display.flip()
#    GameOver()
    time.sleep(4)
    pygame.quit()#for pygame
    sys.exit()#for console


def scoreBoard(choice =1):
    sFont = pygame.font.SysFont('monaco',24)
    ssurf = sFont.render('Score:{0}'.format(score),True,red)
    srect =ssurf.get_rect()
    if choice ==1:
        srect.midtop=(80,10)
    else:
        srect.midtop=(360,120)
    playSurface.blit(ssurf,srect)  
    #pygame.display.flip()
    
while True:

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.KEYDOWN:

                    if event.key==pygame.K_RIGHT or event.key == ord('d'):
                        changeto ="RIGHT"
                    if event.key==pygame.K_LEFT or event.key == ord('a'):
                        changeto ="LEFT"
                    if event.key==pygame.K_UP or event.key == ord('w'):
                        changeto ="UP"
                    if event.key==pygame.K_DOWN or event.key == ord('s'):
                        changeto ="DOWN"
                    if event.key==pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT)
                            )
    if changeto == "RIGHT" and not direction=="LEFT":
        direction ="RIGHT"
    if changeto == "LEFT" and not direction=="RIGHT":
        direction ="LEFT"
    if changeto == "DOWN" and not direction=="UP":
        direction ="DOWN"
    if changeto == "UP" and not direction=="DOWN":
        direction ="UP"

    if direction == "RIGHT":
        sPosition[0] += 10
    if direction == "LEFT":
        sPosition[0] -= 10
    if direction == "UP":
        sPosition[1] -= 10
    if direction == "DOWN":
        sPosition[1] += 10    

    sBody.insert(0,list(sPosition))
    if sPosition[0]==foodPos[0] and sPosition[1] ==foodPos[1]:
        score +=1
        foodSpawn =False
    
    else :
        sBody.pop()

    #foodSpawn
    if foodSpawn==False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True

    playSurface.fill(white)

    for pos in sBody:
        pygame.draw.rect(playSurface,green,pygame.Rect(pos[0],pos[1],10,10))

    pygame.draw.rect(playSurface,brown,
        pygame.Rect(foodPos[0],foodPos[1],10,10))


    if sPosition[0]>710 or sPosition[0]<0:
        GameOver()
    if sPosition[1]>450 or sPosition[1]<0:
        GameOver()
    for block in sBody[1:]:
        if sPosition[0]==block[0] and sPosition[1]==block[1]:

            GameOver()



    scoreBoard()
    pygame.display.flip() 
    fpsController.tick(23)












                



                
                
                
                
                
                
                
                
                








