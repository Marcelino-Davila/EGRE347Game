import pygame as pg
import PlayerClass
import enemies
import actor
import LevelManager
import json

class entityManager:
    def __init__(self):
        self.enemyCount = 0
        self.PlayerDead = False
        self.player = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.AllyBullets = pg.sprite.Group()
        self.EnemyBullets = pg.sprite.Group()
        self.PowerUps = pg.sprite.Group()
        self.Weapons = pg.sprite.Group()
        self.buttons = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.ClassAbilities = pg.sprite.Group()
        self.map = pg.sprite.Group()

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
            self.ClassAbilities.add(entity)
        elif entityType == "map":
            self.map.add(entity)
    
    def removeEntity(self,entity,entityType):
        if entityType == "Player":
            self.PlayerDead = True
            self.player.remove(entity)
        elif entityType == "Enemy": 
            self.enemyCount-=1
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
            self.ClassAbilities.remove(entity)     

    def updateAll(self,pause):
        if not pause:
            for entity in self.player:
                entity.update()
                entity.processInput(pg.key.get_pressed())
                bullet = entity.processMouse(pg.mouse.get_pressed())
                if bullet:
                    self.addEntity(bullet,"AllyBullets")
                if entity.ability:
                    if entity.grenadeCD > 720: 
                        entity.grenadeCD = 0
                        grenade = entity.classAbility()
                        self.addEntity(grenade,"ClassAbility")
            for entity in self.enemies:
                entity.update()
                if entity.alert:
                    bullet = entity.gun()
                    if bullet:
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
            for entity in self.map:
                entity.render(screen)
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
                    enemyDead = enemies.collisionBullet(bullets.damage)
                    if enemyDead:
                        self.removeEntity(enemies,"Enemy")
                    self.removeEntity(bullets,"AllyBullets")
        for player in self.player:
            for bullets in self.EnemyBullets:
                if pg.sprite.collide_rect(bullets,player):
                    playerDead = player.collisionBullet(bullets.damage)
                    if playerDead:
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

    def loadLevel(self,levelSelect):#takes in all the data from the json file and adds every entity to the entity manager
        self.enemyCount = 0
        JSONPath = "Levels/Levels.JSON"
        with open(JSONPath,'r') as JSONFile:
            LevelDictionary = json.load(JSONFile)
        for level in LevelDictionary:
            if level["Name"] == levelSelect:
                image = level["Image"]
                playerData = level["Player"]
                enemyList= level["enemies"]
                wallData = level["walls"]
        mapImage = LevelManager.map(pg.image.load(image))
        self.addEntity(mapImage,"map")
        if playerData["class"] == "soldier":
            player = PlayerClass.soldier(playerData["x"],playerData["y"])
        elif playerData["class"] == "Gojira":
            player = PlayerClass.Gojira(playerData["x"],playerData["y"])
        self.addEntity(player,"Player")
        enemyCount = 0
        for enemy in enemyList:
            self.enemyCount+=1
            enemyx = enemyList[enemy]["x"]
            enemyy = enemyList[enemy] ["y"]
            patroll = []
            for targetpoint in enemyList[enemy]["Patroll"]:
                target = enemyList[enemy]["Patroll"][targetpoint]
                patroll.append(target)
            self.addEntity(enemies.enemies(enemyx,enemyy,player,patroll),"Enemy")
        for wall in wallData:
            self.addEntity(actor.coliders(wallData[wall]["x"],wallData[wall]["y"],wallData[wall]["width"],wallData[wall]["height"]),"Walls")

    def unloadLevel(self):
        for entity in self.player:
            self.player.remove(entity)
        for entity in self.enemies:
            self.enemies.remove(entity)
        for entity in self.AllyBullets:
            self.AllyBullets.remove(entity)
        for entity in self.EnemyBullets:
            self.EnemyBullets.remove(entity)
        for entity in self.PowerUps:
            self.PowerUps.remove(entity)
        for entity in self.Weapons:
            self.Weapons.remove(entity)
        for entity in self.walls:
            self.walls.remove(entity)
        for entity in self.ClassAbilities:
            self.ClassAbilities.remove(entity)
        for entity in self.map:
            self.map.remove(entity)
