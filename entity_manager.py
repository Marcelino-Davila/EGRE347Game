class entityManager:
    def __init__(self):
        self.entities = dict()
        self.entities["Player"] = []
        self.entities["enemy"] = []
        self.entities["bullet"] = []

    def addEntity(self,entity,entityType):
        self.entities[entityType].append(entity)
    
    def removeEntity(self,entity,entityType):
        self.entities[entityType].remove(entity)

    def updateAll(self):
        for entity in self.entities["Player"]:
            entity.update()

    def renderAll(self,screen):
        for entity in self.entities["Player"]:
            entity.render(screen)
            