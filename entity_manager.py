import pygame as pg

class entityManager:
    def __init__(self):
        self.player = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.AllyBullets = pg.sprite.Group()
        self.EnemyBullets = pg.sprite.Group()
        self.PowerUps = pg.sprite.Group()
        self.Weapons = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ClassAbilities = pg.sprite.Group()

    def addEntity(self,entity,entityType):
        if entityType == "Player":
            self.player.add(entity)
        elif entityType == "Enemy":
            self.enemies.add(entity)
        elif entityType == "AllyBullets":
            self.AllyBullets.add(entity)
        elif entityType == "EnemyBullets":
            self.EnemyBullets.add(entity)
        elif entityType == "PowerUps":
            self.PowerUps.add(entity)
        elif entityType == "Weapons":
            self.Weapons.add(entity)
        elif entityType == "Buttons":
            self.buttons.add(entity)
        elif entityType == "Walls":
            self.walls.add(entity)
        elif entityType == "ClassAbility":
            print("grenade")
            self.ClassAbilities.add(entity)
    
    def removeEntity(self,entity,entityType):
        if entityType == "Player":
            self.player.remove(entity)
        elif entityType == "Enemy": 
            self.enemies.remove(entity)
        elif entityType == "AllyBullets":
            self.AllyBullets.remove(entity)
        elif entityType == "EnemyBullets":
            self.EnemyBullets.remove(entity)
        elif entityType == "PowerUps":
            self.PowerUps.remove(entity)
        elif entityType == "Weapons":
            self.Weapons.remove(entity)
        elif entityType == "Buttons":
            self.buttons.remove(entity)
        elif entityType == "Walls":
            self.walls.remove(entity)
        elif entityType == "ClassAbilities":
            print("Grenade")
            self.ClassAbilities.remove(entity)

    def updateAll(self,pause):
        if not pause:
            for entity in self.player:
                entity.update()
                if entity.ability:
                    print("grenade")
                    if entity.grenadeCD > 720: 
                        entity.grenadeCD = 0
                        grenade = entity.classAbility()
                        self.addEntity(grenade,"ClassAbility")
            for entity in self.enemies:
                entity.update()
                if entity.alert:
                    bullet = entity.gun()
                    self.addEntity(bullet,"EnemyBullets")
            for entity in self.AllyBullets:
                entity.update()
                if entity.delete:
                    self.removeEntity(entity,"AllyBullets")
            for entity in self.EnemyBullets:
                entity.update()
                if entity.delete:
                    self.removeEntity(entity,"EnemyBullets")
            for entity in self.PowerUps:
                entity.update()
            for entity in self.Weapons:
                entity.update()
            for entity in self.walls:
                entity.update()
            for entity in self.ClassAbilities:
                entity.update()
                if entity.delete:
                    self.removeEntity(entity,"ClassAbilities")
        else:
            for entity in self.buttons:
                entity.update()

    def renderAll(self,screen,pause):
        if not pause:
            for entity in self.player:
                entity.render(screen)
            for entity in self.enemies:
                entity.render(screen)
            for entity in self.AllyBullets:
                entity.render(screen)
            for entity in self.EnemyBullets:
                entity.render(screen)
            for entity in self.PowerUps:
                entity.render(screen)
            for entity in self.Weapons:
                entity.render(screen)
            for entity in self.walls:
                entity.render(screen)
            for entity in self.ClassAbilities:
                entity.render(screen)
        else:
            for entity in self.buttons:
                entity.render(screen)

    def checkCollisions(self):
        for bullets in self.AllyBullets:
            for walls in self.walls:
                if pg.sprite.collide_rect(bullets,walls):
                    self.removeEntity(bullets,"AllyBullets")
        for player in self.player:
            for walls in self.walls:
                if pg.sprite.collide_rect(player,walls):
                    if not player.jump:
                        player.kinem.revertX()
                        player.kinem.revertY()
        for enemies in self.enemies:
            for bullets in self.AllyBullets:
                if pg.sprite.collide_rect(bullets,enemies):
                    enemyDead = enemies.collisionBullet()
                    if enemyDead:
                        self.removeEntity(enemies,"Enemy")
                    self.removeEntity(bullets,"AllyBullets")
        for player in self.player:
            for bullets in self.EnemyBullets:
                if pg.sprite.collide_rect(bullets,player):
                    playerDead = player.collisionBullet()
                    if playerDead:
                        print(playerDead)
                        self.removeEntity(player,"Player")
                    self.removeEntity(bullets,"EnemyBullets")
        for player in self.player:
            for enemies in self.enemies:
                if pg.sprite.collide_rect(player.detectRange,enemies):
                    enemies.alert = True
                else:
                    enemies.alert = False
        for abilities in self.ClassAbilities:
            for player in self.player:
                if abilities.explode:
                    if pg.sprite.collide_rect(abilities,player):
                        player.rocketJump((abilities.rect.x,abilities.rect.x))
        for abilities in self.ClassAbilities:
            for enemies in self.enemies:
                if abilities.explode:
                    if pg.sprite.collide_rect(abilities,enemies):
                        enemyDead = enemies.explode()
                        if enemyDead:
                            self.removeEntity(enemies,"Enemy")        

    def loadLevel(self):#takes in all the data from the json file and adds every entity to the entity manager
        pass