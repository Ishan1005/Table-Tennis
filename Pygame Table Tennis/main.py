import pygame
import random 
import sys
pygame.init()
w,h = 500,500
screen = pygame.display.set_mode((w,h))

#Colors
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)


#Player
pw = 100
ph = 20
px = w//2 -h//2
py = h - ph - 10
ps=10
 #Object
o0r = 15
ox = random.randint(0,w - o0r)
oy = 0 - o0r
os = 5

#score
score = 0
font = pygame.font.Font(None,36)


#Game Clock
clock = pygame.time.Clock()


#Loop
running = True
while running:
    screen.fill(White)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and px > 0:
        px-=ps
    if key[pygame.K_RIGHT] and px < w - pw:
        px+=ps
    oy+=os
    if(px<ox<px+pw or px<ox+o0r*2<px+pw) and py<oy+o0r<py+ph:
        score = score +1
        ox = random.randint(0,w - o0r)
        oy = 0 - o0r
        os = os + 0.2
    if oy>h:
        running = False
    pygame.draw.rect(screen,Blue,(px,py,pw,ph))
    pygame.draw.circle(screen,Red,(ox,oy),o0r)

    st = font.render(f"Score:{score}",True,Green)
    screen.blit(st,(10,10))

    pygame.display.flip()

    clock.tick(30)

print("Round over you got",score)
pygame.quit()
sys.exit()
















   