class Plot:
    def __init__(self):
        self.slotLimit = 7
        self.plantList = []

    def addPlant(self, plant):
        self.plantList.append(plant)

    def display_plantList(self):
        for _ in self.plantList:
            print(_)


    def updatePlantList(self):
        for plant in self.plantList:
            plant.update()



