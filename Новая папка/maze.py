from pygame import *
window = display.set_mode((700, 500))
display.set_caption('Лаберинт')
background = transform.scale(image.load('background.jpg'), (700, 500))
window.blit(background, (0,0))
spritel = transform.scale(image.load('cyborg.png'), (100, 100))
window.blit(spritel, (50, 450))
spritel = transform.scale(image.load('hero.png'), (100, 100))
window.blit(spritel, (600, 250))
spritel = transform.scale(image.load('treasure.png'), (100, 100))
window.blit(spritel, (650, 450))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (40, 40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 700:
            self.rect.y += self.speed
    def updote(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= -80:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player = GameSprite('hero.png', 80, 80, 4)
wall1 = Wall(211, 52, 235, 100, 50, 350, 5)
wall2 = Wall(211, 52, 235, 100, 50, 5, 250)
wall3 = Wall(211, 52, 235, 100, 300, 125, 5)
wall4 = Wall(211, 52, 235, 100, 375, 125, 5)
wall5 = Wall(211, 52, 235, 100, 450, 550, 5)
wall6 = Wall(211, 52, 235, 550, 50, 100, 5)
wall7 = Wall(211, 52, 235, 650, 50, 5, 405)
wall8 = Wall(211, 52, 235, 650, 50, 5, 405)
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0, 0))
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    player.reset()
    player.update()
    '''player1.updote()'''
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()