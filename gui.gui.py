import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
myfont = pygame.font.SysFont("Fixedsys", 25)
label = myfont.render("Some text!", 1, (255,255,0))
screen.blit(label, (100, 100))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()