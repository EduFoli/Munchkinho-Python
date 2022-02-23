import pygame

#inicializando o Pygame e criando a janela
pygame.init()
display = pygame.display.set_mode([800, 600])
pygame.display.set_caption("MUNCHKINHO")

#
drawGroup = pygame.sprite.Group()
guy = pygame.sprite.Sprite(drawGroup)
guy.image = pygame.image.load("data/mapa.png")
guy.rect = pygame.Rect(50,50,100,100)



gameLoop = True
if __name__ == "__main__":
    while gameLoop :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            print("Segurando W!")

        #Draw:
        display.fill([224, 146, 49])
        drawGroup.draw(display)



        #player = pygame.Rect(50, 50, 100, 100)
        #pygame.draw.rect(display, [65, 74, 64, 255], player)

        pygame.display.update()
