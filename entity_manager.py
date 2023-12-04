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

    def updateAll(self,pause):
        if not pause:
            for entity in self.player:
                entity.update()
            for entity in self.enemies:
                entity.update()
            for entity in self.AllyBullets:
                entity.update()
                if entity.delete:
                    self.removeEntity(entity,"AllyBullets")
            for entity in self.EnemyBullets:
                entity.update()
            for entity in self.PowerUps:
                entity.update()
            for entity in self.Weapons:
                entity.update()
            for entity in self.walls:
                entity.update()
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
            for enemies in self.enemies:
                if pg.sprite.collide_rect(player.detectRange,enemies):
                    enemies.alert = True
                else:
                    enemies.alert = False

    def loadLevel(self):#takes in all the data from the json file and adds every entity to the entity manager
        pass