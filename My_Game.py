import pygame
import random
import time
import os

pygame.init()
pygame.mixer.init()
#Local variable
window_width=800
window_height=400
white = [255, 255, 255]
pink = [255, 77, 90]
black = [0, 0, 0]
red = (255, 0, 0)
fps = 80
#Display
window_screen=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("RK_Nanda")
#clock
clock=pygame.time.Clock()


def text_screen(text, color,x,y):
    font = pygame.font.SysFont(None, 40)
    screen_text = font.render(text, True, color)
    window_screen.blit(screen_text, [x,y])


def crash(x1,x2,X1,X2,y1,y2,Y1,Y2):
    a=max(0,min(x2,X2)-max(x1,X1))
    A=max(0,min(y2,Y2)-max(y1,Y1))
    if a!=0 and A!=0:
        return True
    else:
        return False

#Game loop
def gameloop():
    heli_x = window_width / 4
    heli_y = window_height / 2
    velocity_x = -5
    velocity_y = 0.5
    white = [255, 255, 255]
    pink = [255, 77, 90]
    black = [0, 0, 0]
    red = (255, 0, 0)
    fps = 60
    stone_x = window_width / 1.2
    stone_y = 100
    stone_size_x = 200
    stone_size_y = 100
    stone1_size_x = 150
    stone1_size_y = 50
    stone1_x = window_width / 1.2
    stone1_y = 350
    score = 0
    game_over = False


    run=True
    while run:
        if game_over:
            # with open("hiscore.txt", "w") as f:
            #     f.write(str(hiscore))
            img_crash = pygame.image.load("heli_crash.jpg")
            img_crash = pygame.transform.scale(img_crash, (window_width, window_height)).convert_alpha()
            window_screen.fill(white)
            window_screen.blit(img_crash, (0, 0))
            text_screen("Game Over! Press Enter To Continue", red, window_width/7+50, 180)
            text_screen("Your Score: " + str(score), red, window_width/2-100, 230)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  exit(1)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        heli_x = window_width / 4
                        heli_y = window_height / 2
                        welcome()

        else:
            # Helicoupter
            img_heli= pygame.image.load("heli.jpg")
            img_heli = pygame.transform.scale(img_heli, (90, 40)).convert_alpha()
            window_screen.fill(white)
            window_screen.blit(img_heli, (heli_x, heli_y))

            # stone
            img_stone = pygame.image.load("stone.jpg")
            img_stone = pygame.transform.scale(img_stone, (stone_size_x,stone_size_y)).convert_alpha()
            window_screen.blit(img_stone, (stone_x, stone_y))
            if stone_x<=-stone_size_x:
                stone_size_x=random.randint(70,200)
                stone_size_y=random.randint(50,window_height-150)
                stone_x = random.randint(700,800)
                stone_y = random.randint(0,300)

            # stone 1
            img_stone1 = pygame.image.load("stone1.jpg")
            if stone1_x<=-stone1_size_x:
                stone1_size_x=random.randint(70,200)
                stone1_size_y=random.randint(50,window_height-150)
                stone1_x =900
                stone1_y = random.randint(0,200)
            a1=stone1_x-20
            a2=a1+stone1_size_x+40
            b1=stone1_y-20
            b2=b1+stone1_size_y+40
            X1 = stone_x+5
            X2 = stone_x + stone_size_x-10
            Y1 = stone_y+5
            Y2 = stone_y + stone_size_y-10
            if not crash(a1,a2,X1,X2,b1,b2,Y1,Y2):
                img_stone1 = pygame.transform.scale(img_stone1, (stone1_size_x, stone1_size_y)).convert_alpha()
                window_screen.blit(img_stone1, (stone1_x, stone1_y))

            # action
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit(1)
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        heli_y = heli_y -15
                        pygame.mixer.music.load('heli_forward.mp3')
                        pygame.mixer.music.play()
                    if event.key == pygame.K_UP:
                        heli_y = heli_y - 15
                        pygame.mixer.music.load('heli_forward.mp3')
                        pygame.mixer.music.play()
                    if event.key == pygame.K_DOWN:
                        heli_y = heli_y +15
                        pygame.mixer.music.load('heli_down.mp3')
                        pygame.mixer.music.play()
                    if event.key == pygame.K_LEFT:
                        heli_x = heli_x - 15
                        pygame.mixer.music.load('heli_down.mp3')
                        pygame.mixer.music.play()
                    if event.key == pygame.K_RIGHT:
                        heli_x = heli_x + 15
                        pygame.mixer.music.load('heli_up.mp3')
                        pygame.mixer.music.play()


            # crash
            if heli_y+10 <0 or (heli_y + 40) > window_height:
                pygame.mixer.music.load('heli_crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                game_over = True
            x1=heli_x-5
            x2=heli_x+90-5
            X1=stone_x
            X2=stone_x+stone_size_x
            y1=heli_y-5
            y2=heli_y + 40-5
            Y1=stone_y
            Y2=stone_y + stone_size_y
            if crash(x1,x2,X1,X2,y1,y2,Y1,Y2) or  crash(x1,x2,a1+25,a2-45,y1,y2,b1+25,b2-45) :
                pygame.mixer.music.load('heli_crush.mp3')
                pygame.mixer.music.play()
                time.sleep(2)
                game_over = True

            # score
            if  abs(stone_x-heli_x)<2or abs(stone1_x-heli_x)<2:
                 score=(score+5)
                 pygame.mixer.music.load('point.mp3')
                 pygame.mixer.music.play()
            text_screen("Score: " + str(score), red, window_width / 2-50, 5)

            stone_x=stone_x+velocity_x
            stone1_x=stone1_x+velocity_x
            heli_y=heli_y + velocity_y
        pygame.display.update()
        clock.tick(fps)


def welcome():
    run= True
    pygame.mixer.music.load('heli_welcome.mp3')
    pygame.mixer.music.play()
    while run:
        bgimg3 = pygame.image.load("heli_welcome.jpg")
        bgimg3 = pygame.transform.scale(bgimg3, (window_width, window_height)).convert_alpha()
        window_screen.fill(white)
        window_screen.blit(bgimg3, (0, 0))
        text_screen("Press Space Bar To Play", black, window_width / 3 - 40, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('heli_start.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)



"""main function"""
welcome()

