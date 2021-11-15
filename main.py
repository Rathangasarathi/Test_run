import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((900, 900))
sky = pygame.image.load("sky.png")
ground = pygame.image.load("ground.png")
b1 = pygame.image.load("bird1.png")
pipe = pygame.image.load("pipe.png")
ground = pygame.transform.scale(ground, (200000, 100))
pipe = pygame.transform.scale(pipe, (50, 300))


class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()


x = 0
r = 800
y = 350
speed = 4
s2 = 2
run = True
while run:

    screen.blit(sky, (0, 0))
    screen.blit(ground, (x, 800))
    screen.blit(pipe, (r, 500))
    screen.blit(pipe, (r, 0))
    x -= speed
    r -= s2
    if r == 0:
        r = 800
    screen.blit(b1, (350, y))
    y += 3

    if y > 765 or y == 765:
        y = 765
        x = 0
        run = False
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        y -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(120)
