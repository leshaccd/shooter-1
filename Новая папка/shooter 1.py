#Создай собственный Шуте
from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
window.blit(background, (0,0))
spritel = transform.scale(image.load('rocket.png'), (500, 100))
window.blit(spritel, (50, 450))
score = 0
lost = 0
font.init()
font1 = font.Font(None, 36)
font2 = font.Font(None, 36)
monsters = sprite.Group()
bullets = sprite.Group()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (70, 70))
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
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.y, 10)
        bullets.add(bullet)

class Monsters(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(25, 675)
            lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

for i in range(5):
    monster = Monsters('ufo.png', randint(50, 650), 0, randint(2, 5))
    monsters.add(monster)

player = GameSprite('rocket.png', 0, 400, 4)
clock = time.Clock()
FPS = 60
game = True
while game:
    window.blit(background, (0, 0))
    player.reset()
    player.update()
    monsters.draw(window)
    monsters.update()
    player.reset()
    text_lose = font1.render('Пропушено:' + str(lost), True, (255, 255, 255))
    text_win = font2.render('Счет:' + str(score), True, (255, 255, 255))
    window.blit(text_lose,(0,0))
    window.blit(text_win,(0,0))
    bullets.draw(window)
    bullets.update()
    kp = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
        if kp[K_SPACE]:
            player.fire()
    if sprite.groupcollide(monsters, bullets, True, True):
        score = score + 1
        monster = GameSprite('ufo.png', randint(80, 620), -40, randint(1, 5))
        monsters.add(monster)
    clock.tick(FPS)
    display.update()
