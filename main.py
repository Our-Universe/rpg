import pygame
import math
import random
pygame.init()

display = pygame.display.set_mode((700,800))
pygame.display.set_caption("RPG")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 330
        self.y = 600
        self.width = 40
        self.height = 40
        self.vel = 5
        self.projlist = []
        self.image = pygame.image.load("player.png")
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.lasttick = 0
        self.health = 5
        self.hitbox = (self.x, self.y, 40, 40)
        self.rectplayer = self.image.get_rect()
        self.collideafterdeath = 0

    def var(self):
        pass

    def checkhit(self, projlist):
        if self.collideafterdeath == 0:
            try:
                for i in projlist:
                    if self.x - 10 <= i.x and (self.x + 40) >= i.x and self.y - 10 <= i.y and (self.y + 40) >= i.y:
                        projlist.remove(i)
                        self.health -= 1
                        self.healthlvl += 1
                    if enemy.health <= 0:
                        self.collideafterdeath += 1
                        projlist.remove(i) #removes all enemy projectiles once enemy is dead
            except:
                pass #no error message for non game breaking bug

    def draw(self):
        if self.health > 0:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
            player.move()
            player.checkhit(enemy.getprojlist())
            self.healthbar = self.health * (40/5)
            pygame.draw.rect(display, (255, 0, 0), (self.x, self.y - 20, 40, 10))
            pygame.draw.rect(display, (0, 255, 0), (self.x, self.y - 20, self.healthbar, 10))
            self.randNumLabel = self.myFont.render(str(self.health), 1, (255, 0, 0))
            display.blit(self.randNumLabel, (self.x, self.y - 40))
            display.blit(self.image, (self.x,self.y))
            for i in self.projlist:
                i.move1()

    def move(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_a] and self.x > 14:
            self.x -= self.vel
        if self.keys[pygame.K_d] and self.x < 646:
            self.x += self.vel
        if self.keys[pygame.K_w] and self.y > 14:
            self.y -= self.vel
        if self.keys[pygame.K_s] and self.y < 646:
            self.y += self.vel
        if self.keys[pygame.K_p]:
            drop.havehealthpot += 1
        try:
            if self.keys[pygame.K_SPACE] and (self.lasttick + 80) < pygame.time.get_ticks(): #last tick for player projectile fire rate
                self.projlist.append(Projectile(self.x + 15,self.y + 15))
                self.lasttick = pygame.time.get_ticks()
        except:
            pass #if curser is on exact pixel in center of character and shoots, error is given

    def getprojlist(self):
        return self.projlist

def removeproj(dellist):
    try:
        for i in range(0, len(dellist)-1):
            if dellist[i].x < 20 or dellist[i].x > 670 or dellist[i].y < 20 or dellist[i].y > 670:
                del dellist[i]

    except:
        pass

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x1, y1):
        self.image1 = pygame.image.load("playerbullet.png")
        self.glow = pygame.image.load("glow.png")
        self.image4 = pygame.image.load("enemybullet1.png")
        self.x = x1
        self.y = y1
        self.hitbox = (self.x, self.y, 50, 50)
        self.originalmouse_x = pygame.mouse.get_pos()[0] - self.x
        self.originalmouse_y = pygame.mouse.get_pos()[1] - self.y
        self.xval = 0
        self.yval = 0

        try:
            self.mouse_x = (self.originalmouse_x - 5) / math.sqrt((self.originalmouse_x)**2 + (self.originalmouse_y)**2) #calculation for
            self.mouse_y = (self.originalmouse_y - 5) / math.sqrt((self.originalmouse_x)**2 + (self.originalmouse_y)**2)
        except:
            pass
        self.completed = False

    def move1(self):
        self.x += self.mouse_x * 10 #Player projectile speed
        self.y += self.mouse_y * 10
        self.bullet = display.blit(self .image1, (self.x,self.y))
        display.blit(self.glow, (self.x - 5, self.y - 5))
        # self.hitbox = (self.x, self.y, 10, 10)
        # pygame.draw.rect(display, (255,255,0), self.hitbox,2)

    def moveE(self, x, y):
        if not self.completed:
            self.xval = self.x - x
            self.yval = self.y - y
            self.xval = self.xval / math.sqrt((self.x - x)**2 + (self.y - y)**2)
            self.yval = self.yval / math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            self.completed = True
        self.bullet = display.blit(self.image4, (self.x - 5, self.y - 5))
        display.blit(self.glow, (self.x - 10, self.y - 10))
        self.x += self.xval * 5
        self.y += self.yval * 5

    def moveE1(self, x, y):
        if not self.completed:
            self.xval = self.x - x - 20
            self.yval = self.y - y - 20
            self.xval = self.xval / math.sqrt((self.x - x)**2 + (self.y - y)**2)
            self.yval = self.yval / math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            self.completed = True
        self.bullet = display.blit(self.image4, (self.x - 5, self.y - 5))
        display.blit(self.glow, (self.x - 10, self.y - 10))
        self.x += self.xval * -8
        self.y += self.yval * -8

class Key():
    def __init__(self):
        self.key1x = enemy.x
        self.key1y = enemy.y
        self.key1 = pygame.image.load("key1.png")
        self.keyshadow = pygame.image.load("keyshadow.png")
        self.movement = random.uniform(1.0, 3.0)
        self.movement1 = random.uniform(1.0, 3.0)
        self.movement3 = 1
        self.movement3y = 1
        self.havekey = 0
        self.health = 1

    def keylvl1(self):
        if enemy.health <= 0:
            if key.health > 0:
                if not (player.x - 10 <= enemy.xkey and (player.x + 40) >= enemy.xkey and player.y - 10 <= enemy.ykey and (player.y + 40) >= enemy.ykey): #picks up key from middle of character to have nice overlapping
                    for event in pygame.event.get():
                        if event.type == PARTICLE_EVENT:
                            particle1.add_particles1()
                    display.blit(self.keyshadow, (enemy.xkey - 5, enemy.ykey + 23))
                    display.blit(self.key1, (enemy.xkey,enemy.ykey))
                    enemy.xkey += self.movement
                    enemy.ykey += self.movement1
                    if enemy.xkey <= 10:
                        self.movement = self.movement * -1
                    elif enemy.xkey >= 645:
                        self.movement = self.movement * -1
                    elif enemy.ykey <= 10:
                        self.movement1 = self.movement1 * -1
                    elif enemy.ykey >= 670:
                        self.movement1 = self.movement1 * -1
                else:
                    self.havekey += 1
                    self.health -= 1

    def keylvl1chest(self):
        if enemy.chesthealth <= 0:
            if key.health > 0:
                if not (player.x - 10 <= enemy.xkey and (player.x + 40) >= enemy.xkey and player.y - 10 <= enemy.ykey + 285 and (player.y + 40) >= enemy.ykey + 285): #picks up key from middle of character to have nice overlapping
                    for event in pygame.event.get():
                        if event.type == PARTICLE_EVENT:
                            particle1.add_particles()
                    display.blit(self.keyshadow, (enemy.xkey - 5, enemy.ykey + 23 + 285))
                    display.blit(self.key1, (enemy.xkey,enemy.ykey + 285))
                    enemy.xkey += self.movement
                    enemy.ykey += self.movement1
                    if enemy.xkey <= 10:
                        self.movement = self.movement * -1
                    elif enemy.xkey >= 645:
                        self.movement = self.movement * -1
                    elif enemy.ykey <= 10 - 285:
                        self.movement1 = self.movement1 * -1
                    elif enemy.ykey >= 670 - 285:
                        self.movement1 = self.movement1 * -1
                else:
                    self.havekey += 1
                    self.health -= 1

    def key1lvl1char(self):
        if self.havekey >= 1 and doors.keypedestal <= 1:
            display.blit(self.key1, (player.x + 10, player.y + 20))

class enemydrops():
    def __init__(self):
        self.heart = pygame.image.load("heart.png")
        self.healthpot = 1
        self.havehealthpot = 0
        self.movement1 = random.uniform(-3.0, -1.0)
        self.movement2 = random.uniform(1.0, 3.0)

    def var(self): #all var defs are to reinstantiate variables per level
        self.movement1 = random.uniform(-3.0, -1.0)
        self.movement2 = random.uniform(1.0, 3.0)
        self.heartx = enemy.x
        self.hearty = enemy.y
        self.healthpot = 1

    def healthpotion(self):
        if enemy.health <= 0:
            if self.healthpot > 0:
                if not (player.x - 10 <= enemy.x and (player.x + 40) >= enemy.x and player.y - 10 <= enemy.y and (player.y + 40) >= enemy.y):
                    display.blit(self.heart, (enemy.x ,enemy.y))
                    enemy.x += self.movement1
                    enemy.y += self.movement2
                    if enemy.x <= 10:
                        self.movement1 = self.movement1 * -1
                    elif enemy.x >= 645:
                        self.movement1 = self.movement1 * -1
                    elif enemy.y <= 10:
                        self.movement2 = self.movement2 * -1
                    elif enemy.y >= 670:
                        self.movement2 = self.movement2 * -1
                else:
                    self.havehealthpot += 1
                    self.healthpot -= 1

    def healthpotionchest(self):
        if enemy.chesthealth <= 0:
            if self.healthpot > 0:
                if not (player.x - 10 <= enemy.x and (player.x + 40) >= enemy.x and player.y - 10 <= enemy.y + 285 and (player.y + 40) >= enemy.y + 285):
                    display.blit(self.heart, (enemy.x ,enemy.y + 285))
                    enemy.x += self.movement1
                    enemy.y += self.movement2
                    if enemy.x <= 10:
                        self.movement1 = self.movement1 * -1
                    elif enemy.x >= 645:
                        self.movement1 = self.movement1 * -1
                    elif enemy.y <= 10 - 285:
                        self.movement2 = self.movement2 * -1
                    elif enemy.y >= 670 - 285:
                        self.movement2 = self.movement2 * -1
                else:
                    self.havehealthpot += 1
                    self.healthpot -= 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 350
        self.y = 50
        self.x1 = 0
        self.y1 = 0
        self.tick = 0
        self.projlist = []
        self.health = 150
        self.chesthealth = 20
        self.healthbar = self.health / 10
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.firerate = 45
        self.direction = 10
        self.movement = 1
        self.movementy = 1
        self.sprites = []
        self.enemy2 = pygame.image.load("enemy2_1.png")
        self.sprites.append(pygame.image.load("enemy1.png"))
        self.sprites.append(pygame.image.load("enemy2.png"))
        self.sprites.append(pygame.image.load("enemy3.png"))
        self.sprites.append(pygame.image.load("enemy4.png"))
        self.sprites.append(pygame.image.load("enemyhit1.png"))
        self.hands = pygame.image.load("enemyhands.png")
        self.current_sprite = 0
        self.image3 = self.sprites[self.current_sprite]
        self.handx = 350
        self.handy = 48
        self.handmovement = 0.1
        self.rect = self.image3.get_rect()
        self.rect.topleft = [self.x, self.y]
        self.knockbackx = 0
        self.knockbacky = 0
        self.shadow = pygame.image.load("enemy1shadow.png")
        self.handshadow = pygame.image.load("enemy1hands_shadow.png")
        self.chest = pygame.image.load("chestclosed.png")

    def update(self):
        if self.current_sprite <= 2:
            self.current_sprite += 0.05
        elif self.current_sprite > 2:
            self.current_sprite += 0.1
        if self.current_sprite >= 3.5 and self.current_sprite <= 3.9:
            self.current_sprite = 0
        if self.current_sprite >= 4:
            self.currentsprite = 5
        if self.current_sprite >= 5:
            self.current_sprite = 0

        self.image3 = self.sprites[int(self.current_sprite)]

    def getprojlist(self):
        return self.projlist

    def checkhit(self, projlist):
        for i in projlist:
            if self.x - 10 <= i.x and (self.x + 50) >= i.x and self.y - 10 <= i.y and (self.y + 50) >= i.y:
                self.current_sprite = 4
                projlist.remove(i)
                self.health -= 20
                particle1.add_particlesp()

    def checkhitchest(self, projlist):
        for i in projlist:
            if self.x - 40 <= i.x and (self.x + 25) >= i.x and self.y + 285 - 10 <= i.y and (self.y + 285 + 30) >= i.y:
                projlist.remove(i)
                self.chesthealth -= 1

    def pattern1(self): #basic enemy patter back and forth shooting
        self.firerate = 25
        self.x1 += self.direction
        if self.x1 == 750:
            self.direction = self.direction * -1
        elif self.x1 == 0:
            self.direction = self.direction * -1

    def pattern2(self):
        self.firerate = 15
        self.x1 += 40
        if self.x1 >= 600:
            self.x1 = 10

    def pattern3(self):
        self.firerate = 250
        proj.xval = proj.xval * -1
        proj.yval = proj.yval * -1
        self.x1 = player.x
        self.y1 = player.y

    def pattern4(self):
        self.firerate = 50
        self.x1 = player.x
        self.y1 = player.y
        proj.x += proj.xval * -1
        proj.y += proj.yval * -1

    def pattern5(self):
        self.firerate = random.randint(1,25)
        self.x1 = 320

    def movement1(self):
        self.x += self.movement
        if self.x == 400:
            self.movement = self.movement * -1
        elif self.x == 200:
            self.movement = self.movement * -1

        self.handy += self.handmovement
        if self.handy <= 48:
            self.handmovement = self.handmovement * -1
        elif self.handy >= 52:
            self.handmovement = self.handmovement * -1

    def movement2(self):
        self.x += self.movement * 2
        self.y += self.movementy * 2
        if self.x >= 636:
            self.movement = self.movement * -1
        elif self.x <= 15:
            self.movement = self.movement * -1
        elif self.y >= 626:
            self.movementy = self.movementy * -1
        elif self.y <= 15:
            self.movementy = self.movementy * -1

    def movement3(self):
        self.x += self.movement * 13
        if self.x >= 640:
            self.movement = self.movement * -1
        elif self.x <= 20:
            self.movement = self.movement * -1

    def draw(self):
        if self.health > 0:
            self.xkey = self.x
            self.ykey = self.y
            self.healthbar = self.health / (150/50)
            pygame.draw.rect(display, (255, 0, 0), (self.x, self.y - 20, 50, 10))
            pygame.draw.rect(display, (0, 255, 0), (self.x, self.y - 20, self.healthbar, 10))
            self.randNumLabel = self.myFont.render(str(self.health), 1, (255, 0, 0))
            display.blit(self.shadow, (self.x, self.y + 35))
            display.blit(self.handshadow, (self.x, self.handy + 50))
            display.blit(self.randNumLabel, (self.x, self.y - 40))
            self.enemy1 = display.blit(self.image3, (self.x,self.y))
            display.blit(self.hands, (self.x + 5, self.handy + 38))
            enemy.checkhit(player.getprojlist())
            for i in self.projlist:
                i.moveE(self.x1, self.y1)
            if self.health > 75:
                enemy.pattern1()
            else:
                enemy.pattern2()
            enemy.movement1()

    def draw2(self):
        if self.health > 0:
            self.xkey = self.x
            self.ykey = self.y
            self.healthbar = self.health / (150/50)
            pygame.draw.rect(display, (255, 0, 0), (self.x, self.y - 20, 50, 10))
            pygame.draw.rect(display, (0, 255, 0), (self.x, self.y - 20, self.healthbar, 10))
            self.randNumLabel = self.myFont.render(str(self.health), 1, (255, 0, 0))
            display.blit(self.shadow, (self.x, self.y + 35))
            display.blit(self.randNumLabel, (self.x, self.y - 40))
            display.blit(self.enemy2, (self.x,self.y))
            display.blit(self.hands, (self.x + 5, self.y + 38))
            enemy.checkhit(player.getprojlist())
            for i in self.projlist:
                i.moveE1(self.x1, self.y1)
            if self.health > 20:
                enemy.pattern3()
            else:
                enemy.pattern4()
            enemy.movement2()

    def draw3(self):
        if self.health > 0:
            self.xkey = self.x
            self.ykey = self.y
            self.healthbar = self.health / (150/50)
            pygame.draw.rect(display, (255, 0, 0), (self.x, self.y - 20, 50, 10))
            pygame.draw.rect(display, (0, 255, 0), (self.x, self.y - 20, self.healthbar, 10))
            self.randNumLabel = self.myFont.render(str(self.health), 1, (255, 0, 0))
            display.blit(self.shadow, (self.x, self.y + 35))
            display.blit(self.randNumLabel, (self.x, self.y - 40))
            display.blit(self.enemy2, (self.x,self.y))
            display.blit(self.hands, (self.x + 5, self.y + 38))
            enemy.checkhit(player.getprojlist())
            for i in self.projlist:
                i.moveE(self.x1, self.y1)
            enemy.pattern5()
            enemy.movement3()

    def drawchest(self):
        if self.chesthealth > 0:
            self.xkey = self.x
            self.ykey = self.y
            self.healthbar = self.chesthealth * 2.5
            pygame.draw.rect(display, (255, 0, 0), (self.x -25, self.y + 260, 50, 10))
            pygame.draw.rect(display, (0, 255, 0), (self.x -25, self.y + 260, self.healthbar, 10))
            self.randNumLabel = self.myFont.render(str(self.health), 1, (255, 0, 0))
            display.blit(self.chest, (self.x - 30, self.y + 285))
            enemy.checkhitchest(player.getprojlist())

    def shoot(self):
        if (self.tick + self.firerate) < pygame.time.get_ticks():
            self.projlist.append(Projectile(self.x + 25, self.y + 55))
            self.tick = pygame.time.get_ticks()

class Levels():
    def __init__(self):
        self.bg1 = pygame.image.load("room1-1.png")
        self.bg1lighting = pygame.image.load("level1lighting.png")
        self.x = 0
        self.y = 0

    def intro(self):
        display.blit(self.bg1, (self.x, self.y))

    def level1(self):
        display.blit(self.bg1, (self.x, self.y))

    def level1lighting(self):
        display.blit(self.bg1lighting,(self.x, self.y))

class doors():
    def __init__(self):
        self.doorx = 317.5
        self.doory = 10
        self.door = pygame.image.load("doorclosed.png")
        self.doorface = pygame.image.load("opendoors.png")
        self.pedestal = pygame.image.load("pedestal.png")
        self.rectdoor = self.door.get_rect()
        self.placed = 0
        self.keypedestal = 0
        self.pedestalx = self.doorx + 150
        self.pedestaly = self.doory

    def displaydoor(self):
        display.blit(self.door, (self.doorx, self.doory))

    def displaypedestal(self):
        display.blit(self.pedestal, (self.doorx + 150, self.doory)) # so the player can overlap the pedestal but not the door

    def pedestalcoll(self):
        if key.havekey >= 1:
            if (player.x - 30 <= self.pedestalx and (player.x + 40) >= self.pedestalx and player.y - 30 <= self.pedestaly and (player.y + 40) >= self.pedestaly):
                self.keypedestal += 1

    def doorstate(self):
        if doors.keypedestal >= 1:
            self.door = pygame.image.load("dooropen.png")
            self.pedestal = pygame.image.load("pedestalkey.png")
            display.blit(self.doorface, (self.doorx - 17, self.doory + 10))
        else:
            self.door = pygame.image.load("doorclosed.png")
            self.pedestal = pygame.image.load("pedestal.png")

class statbar():
    def __init__(self):
        self.bg = pygame.image.load("statsheet.png")
        self.heartpotion = pygame.image.load("heartpotioninv.png")
        self.heartpotionx = 345
        self.heartpotiony = 765
        self.heartpotionempty = pygame.image.load("heartpotioninvempty.png")
        self.use = pygame.image.load("use.png")
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.myFont2 = pygame.font.SysFont("Times New Roman", 16)
        self.myFont3 = pygame.font.SysFont("Times New Roman", 12)
        self.num = 0
        self.potionnum = self.myFont.render("x" + str(drop.havehealthpot), True, (230, 230, 230))
        self.mousedown = 0

    def draw(self):
        pygame.mouse.get_pos()
        display.blit(self.bg, (0, 700))
        self.healthpotion()
        self.mouseclick()
        self.level = self.myFont.render((f'level: {levelnum.state}'), True, (230, 230, 230))
        self.randNumLabel = self.myFont.render(str("INVENTORY:"), True, (230, 230, 230))
        display.blit(self.randNumLabel, (345, 730))
        display.blit(self.level, (20, 703))
        self.click = True
        self.mouse_x = pygame.mouse.get_pos()[0]
        self.mouse_y = pygame.mouse.get_pos()[1]
        player.healthbar = player.health * (90 / 5)
        pygame.draw.rect(display, (255, 0, 0), (75, 770 - 20, 90, 10))
        pygame.draw.rect(display, (0, 255, 0), (75, 770 - 20, player.healthbar, 10))
        self.playerhealth = self.myFont.render((f'Player:'), True, (230, 230, 230))
        display.blit(self.playerhealth, (15, 743))
        enemy.healthbar = enemy.health * 0.6
        pygame.draw.rect(display, (255, 0, 0), (75, 795 - 20, 90, 10))
        pygame.draw.rect(display, (0, 255, 0), (75, 795 - 20, enemy.healthbar, 10))
        self.enemyhealth = self.myFont.render((f'Enemy:'), True, (230, 230, 230))
        display.blit(self.enemyhealth, (15, 767))
        self.health = self.myFont2.render((f'-=HEALTH=-'), True, (230, 230, 230))
        display.blit(self.health, (45, 728))
        self.shoot = self.myFont3.render(("Shoot - SPACE"), True, (230, 230, 230)) #\n does not work with this command so I have to repeat statments
        self.aim = self.myFont3.render(("Aim - Mouse"), True, (230, 230, 230))
        self.move = self.myFont3.render(("Move - W,A,S,D"), True, (230, 230, 230))
        self.controls = self.myFont2.render(("-=Controls=-"), True, (230, 230, 230))
        display.blit(self.controls, (590, 728))
        display.blit(self.shoot, (593, 750))
        display.blit(self.aim, (598, 765))
        display.blit(self.move, (591, 780))


        self.mouseclick()

    def healthpotion(self):
        display.blit(self.use, (self.heartpotionx + 55, self.heartpotiony))
        if drop.havehealthpot >= 1:
            self.potionnum = self.myFont.render("x" + str(drop.havehealthpot), True, (230, 230, 230))
            display.blit(self.heartpotion, (self.heartpotionx, self.heartpotiony))
            display.blit(self.potionnum, (375, 765))
        else:
            display.blit(self.heartpotionempty, (self.heartpotionx, self.heartpotiony))
            display.blit(self.potionnum, (375, 765))

    def mouseclick(self):
        self.val = 0
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if drop.havehealthpot >= 1 and player.health > 0:
                    if self.mouse_x > (self.heartpotionx + 55) and self.mouse_x < ((self.heartpotionx + 55) + 40) and self.mouse_y > self.heartpotiony and self.mouse_y < (self.heartpotiony + 20):
                        if self.click == True:
                            player.health = 5
                            drop.havehealthpot -= 1
                            self.potionnum = self.myFont.render("x" + str(drop.havehealthpot), True, (230, 230, 230))
            elif event.type == pygame.MOUSEBUTTONUP:
                self.click = True

class Gamestate():
    def __init__(self):
        self.run = True
        self.state = 'maingame'
        self.state = 1
        # self.col = pygame.sprite.collide_rect(player.image, self.door)

    def state_manager(self):
        if self.state == 1:
            self.intro()
        if self.state == 2:
            self.level1()
        if self.state == 3:
            self.level2()
        if self.state == 4:
            self.level3()

    def door_collision(self):
        if doors.keypedestal >= 1:
            if (player.x - 65 <= doors.doorx and (player.x + 40) >= doors.doorx and player.y <= doors.doory and (player.y + 40) >= doors.doory):
                self.state += 1
                player.__init__() # resets all enemy and player variables
                enemy.__init__()
                key.__init__()
                doors.__init__()
                level.__init__()
                particle1.__init__()
                drop.var()

    def intro(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        level.intro()
        removeproj(player.getprojlist())
        doors.displaypedestal()
        player.draw()
        particle1.emit()
        key.key1lvl1char()
        doors.doorstate()
        doors.pedestalcoll()
        doors.displaydoor()
        enemy.drawchest()
        drop.healthpotionchest()
        key.keylvl1chest()
        level.level1lighting()
        stats.draw()
        levelnum.door_collision()
        self.keys = pygame.key.get_pressed()
        pygame.display.update()

        # self.doorx - 10 <= Player.x and (self.doorx + 40) >= Player.x and self.doory - 10 <= Player.y and (self.doory + 40) >= player.y:

    def level1(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        level.level1()
        doors.displaypedestal()
        player.draw()
        key.key1lvl1char()
        doors.pedestalcoll()
        doors.doorstate()
        doors.displaydoor()
        enemy.shoot()
        particle1.emit()
        enemy.draw()
        enemy.update()
        removeproj(player.getprojlist())
        removeproj(enemy.getprojlist())
        levelnum.door_collision()
        drop.healthpotion()
        key.keylvl1()
        level.level1lighting()
        stats.draw()
        pygame.display.update()

    def level2(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        level.level1()
        doors.displaypedestal()
        player.draw()
        particle1.emit()
        key.key1lvl1char()
        doors.pedestalcoll()
        doors.doorstate()
        doors.displaydoor()
        enemy.shoot()
        enemy.draw2()
        enemy.update()
        removeproj(player.getprojlist())
        removeproj(enemy.getprojlist())
        levelnum.door_collision()
        drop.healthpotion()
        key.keylvl1()
        level.level1lighting()
        stats.draw()
        pygame.display.update()

    def level3(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        level.level1()
        doors.displaypedestal()
        player.draw()
        particle1.emit()
        key.key1lvl1char()
        doors.pedestalcoll()
        doors.doorstate()
        doors.displaydoor()
        enemy.shoot()
        enemy.draw3()
        enemy.update()
        removeproj(player.getprojlist())
        removeproj(enemy.getprojlist())
        levelnum.door_collision()
        drop.healthpotion()
        key.keylvl1()
        level.level1lighting()
        stats.draw()
        pygame.display.update()

class ParticlePrinciple:
    def __init__(self):
        self.particles = []
        self.particles2 = []

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(display, (225,225,225),particle[0],int(particle[1]))

    def add_particles(self):
        self.pos_x = enemy.xkey + 15
        self.pos_y = enemy.ykey + 285 + 10
        self.radius = 7
        self.direction_x = random.randint(-2, 2)
        self.direction_y = random.randint(-2, 2)
        self.particle_circle = [[self.pos_x, self.pos_y], self.radius, [self.direction_x, self.direction_y]]
        self.particles.append(self.particle_circle)

    def add_particles1(self):
        self.pos_x = enemy.xkey + 15
        self.pos_y = enemy.ykey + 10
        self.radius = 7
        self.direction_x = random.randint(-2, 2)
        self.direction_y = random.randint(-2, 2)
        self.particle_circle = [[self.pos_x, self.pos_y], self.radius, [self.direction_x, self.direction_y]]
        self.particles.append(self.particle_circle)

    def add_particlesp(self):
        self.pos_x = enemy.x + 25
        self.pos_y = enemy.y + 25
        self.radius = 7
        self.direction_x = random.randint(-3, 3)
        self.direction_y = random.randint(-3, 3)
        self.particle_circle = [[self.pos_x, self.pos_y], self.radius, [self.direction_x, self.direction_y]]
        self.particles.append(self.particle_circle)

    def delete_particles(self):
        self.particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = self.particle_copy


PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT,30)

particle1 = ParticlePrinciple()
particle2 = ParticlePrinciple()

clock = pygame.time.Clock()

doors = doors()
player = Player()
enemy = Enemy()
enemy1 = Enemy()
level = Levels()
levelnum = Gamestate()
keys = pygame.key.get_pressed()
key = Key()
drop = enemydrops()
stats = statbar()
proj = Projectile(0, 0)

run = True

while run:
        levelnum.state_manager()

pygame.quit
