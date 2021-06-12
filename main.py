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
        #yo

class Key():
    def __init__(self):
        self.key1x = enemy.x
        self.key1y = enemy.y
        self.key1 = pygame.image.load("key1.png")
        self.movement = random.uniform(1.0, 3.0)
        self.movement1 = random.uniform(1.0, 3.0)
        self.movement3 = 1
        self.movement3y = 1
        self.havekey = 0
        self.health = 1

    def keylvl1(self):
        if enemy.health > 0:
            self.key1x += self.movement3 #to spawn on enemy death location
            if self.key1x == 400:
                self.movement3 = self.movement3 * -1
            elif self.key1x == 200:
                self.movement3 = self.movement3 * -1
        elif enemy.health <= 0:
            if key.health > 0:
                if not ((player.x + 20) > key.key1x and (player.x + 20) < (key.key1x + 50) and (player.y + 20) < (key.key1y + 20) and (player.y + 20) > (key.key1y)): #picks up key from middle of character to have nice overlapping
                    display.blit(self.key1, (self.key1x,self.key1y))
                    self.key1x += self.movement
                    self.key1y += self.movement1
                    if self.key1x <= 10:
                        self.movement = self.movement * -1
                    elif self.key1x >= 645:
                        self.movement = self.movement * -1
                    elif self.key1y <= 10:
                        self.movement1 = self.movement1 * -1
                    elif self.key1y >= 670:
                        self.movement1 = self.movement1 * -1
                else:
                    self.havekey += 1
                    self.health -= 1

    def key1lvl1char(self):
        if self.havekey >= 1 and doors.keypedestal <= 1:
            display.blit(self.key1, (player.x + 10, player.y + 30))

class enemydrops():
    def __init__(self):
        self.heart = pygame.image.load("heart.png")
        self.healthpot = 1
        self.havehealthpot = 0

    def var(self): #all var defs are to reinstantiate variables per level
        self.movement1 = random.uniform(-3.0, -1.0)
        self.movement2 = random.uniform(1.0, 3.0)
        self.heartx = enemy.x
        self.hearty = enemy.y
        self.healthpot = 1

    def healthpotion(self):
        if enemy.health > 0:
            self.heartx += key.movement3
            if self.heartx == 400:
                key.movement3 = key.movement3 * -1
            elif self.heartx == 200:
                key.movement3 = key.movement3 * -1
        elif enemy.health <= 0:
            if self.healthpot > 0:
                if not (player.x - 10 <= self.heartx and (player.x + 40) >= self.heartx and player.y - 10 <= self.hearty and (player.y + 40) >= self.hearty):
                    display.blit(self.heart, (self.heartx ,self.hearty))
                    self.heartx += self.movement1
                    self.hearty += self.movement2
                    if self.heartx <= 10:
                        self.movement1 = self.movement1 * -1
                    elif self.heartx >= 645:
                        self.movement1 = self.movement1 * -1
                    elif self.hearty <= 10:
                        self.movement2 = self.movement2 * -1
                    elif self.hearty >= 670:
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
                self.health -= 1

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

    def draw(self):
        if self.health > 0:
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
        key.havekey += 1

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

    def door_collision(self):
        if doors.keypedestal >= 1:
            if (player.x - 65 <= doors.doorx and (player.x + 40) >= doors.doorx and player.y <= doors.doory and (player.y + 40) >= doors.doory):
                self.state += 1
                player.__init__() # resets all enemy and player variables
                enemy.__init__()
                key.__init__()
                doors.__init__()
                level.__init__()
                drop.var()

    def intro(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        doors.keypedestal = 1

        level.intro()
        removeproj(player.getprojlist())
        doors.displaypedestal()
        player.draw()
        doors.doorstate()
        doors.pedestalcoll()
        doors.displaydoor()
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
                run = False
        level.level1()
        doors.displaypedestal()
        player.draw()
        key.key1lvl1char()
        doors.pedestalcoll()
        doors.doorstate()
        doors.displaydoor()
        enemy.shoot()
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

class statbar():
    def __init__(self):
        self.bg = pygame.image.load("statsheet.png")
        self.heartpotion = pygame.image.load("heartpotioninv.png")
        self.heartpotionx = 345
        self.heartpotiony = 765
        self.heartpotionempty = pygame.image.load("heartpotioninvempty.png")
        self.myFont = pygame.font.SysFont("Times New Roman", 18)
        self.num = 0
        self.potionnum = self.myFont.render("x" + str(drop.havehealthpot), True, (230, 230, 230))
        self.mousedown = 0

    def draw(self):
        pygame.mouse.get_pos()
        display.blit(self.bg, (0, 700))
        self.healthpotion()
        self.mouseclick()
        self.randNumLabel = self.myFont.render(str("INVENTORY:"), True, (230, 230, 230))
        display.blit(self.randNumLabel, (345, 730))
        self.click = True
        self.mouse_x = pygame.mouse.get_pos()[0]
        self.mouse_y = pygame.mouse.get_pos()[1]
        self.mouseclick()

    def healthpotion(self):
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
                    if self.mouse_x > self.heartpotionx and self.mouse_x < (self.heartpotionx + 20) and self.mouse_y > self.heartpotiony and self.mouse_y < (self.heartpotiony + 20):
                        if self.click == True:
                            player.health = 5
                            drop.havehealthpot -= 1
                            self.potionnum = self.myFont.render("x" + str(drop.havehealthpot), True, (230, 230, 230))
            elif event.type == pygame.MOUSEBUTTONUP:
                self.click = True

clock = pygame.time.Clock()

doors = doors()
player = Player()
enemy = Enemy()
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

#hi