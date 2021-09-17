import pygame, random

ANCHO = 900
ALTO = 585
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

def texto(texto, tam=20, color=(0, 0, 0)):
    fuente = pygame.font.Font(None, tam)
    return fuente.render(texto, True, color)


class Laser(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/Aless/OneDrive/Escritorio/laser2.png").convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.yy = 2
        self.image = pygame.image.load('C:/Users/Aless/OneDrive/Escritorio/tie pr.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.x -= 2
        
        if self.rect.x < 0:
            self.rect.x = 900 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('C:/Users/Aless/OneDrive/Escritorio/milenario3.png').convert()
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
    
    def  update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = 0
        self.rect.y = mouse_pos[1]

    
negro = 0,0,0
blanco = 255,255,255

def main():
    pygame.init()
    screen = pygame.display.set_mode([900,585])

    clock = pygame.time.Clock()
    run = True
    score = 0
    
    width = 900
    height = 585
    i = 0

    fondo = pygame.image.load('C:/Users/Aless/OneDrive/Escritorio/Space.jpg')
    fondorect = fondo.get_rect();
    bg = pygame.transform.scale(fondo, (900,585) )

    all_sprite_list = pygame.sprite.Group()
    meteor_list = pygame.sprite.Group()
    laser_list = pygame.sprite.Group()

    for i in range(20):
        meteor = Meteor()
        meteor.rect.x = random.randrange(800)
        meteor.rect.y = random.randrange(540)

        meteor_list.add(meteor)
        all_sprite_list.add(meteor)

    player = Player()
    all_sprite_list.add(player)
    
    sound = pygame.mixer.Sound('C:/Users/Aless/OneDrive/Escritorio/XWing fire.mp3')
    pygame.mixer.music.load('C:/Users/Aless/OneDrive/Escritorio/Music  Asteroid chase.mp3')
    pygame.mixer.music.play(3) #el 3 es el número de veces que se reproduce el archivo

    while run:
        for event in pygame.event.get(): #se captura el evento que se produce
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                laser = Laser()
                laser.rect.x = player.rect.x + 88
                laser.rect.y = player.rect.y + 39
         

                all_sprite_list.add(laser)
                laser_list.add(laser)
                sound.play()
    
        all_sprite_list.update() #actualiza el movimiento de los sprite
        #se definen las colisiones
        for laser in laser_list:
            meteor_hit_list = pygame.sprite.spritecollide(laser, meteor_list, True) # el true es para que desaparezcan
            #para eliminar el laser en las colisiones
            for meteor in meteor_hit_list:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
                score += 1
                print(score)
            if laser.rect.y < 0:
                all_sprite_list.remove(laser)
                laser_list.remove(laser)
        
        #screen.fill(blanco)
        #screen.blit(fondo, fondorect)
        
          
        #screen.fill(blanco)
        #screen.blit(fondo, fondorect)
        
        screen.fill((0,0,0))
        screen.blit(bg, (i,0))
        #screen.blit(bg, (0,i))
        screen.blit(bg, (width+i,0))
        #screen.blit(bg, (0,height+i))

        if i == -width:
        #if i == -height:
            screen.blit(bg, (width+i, 0))
            #screen.blit(bg, (0, height+i))
            i = 0

        i -= 1
        
        all_sprite_list.draw(screen) #se pintan todos los sprites
        screen.blit(texto("Score:", 60, BLANCO), (ANCHO / 3, 10))
        screen.blit(texto(str(score), 60, BLANCO), (ANCHO / 2, 10))


        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()


if __name__ == "__main__":
    main()