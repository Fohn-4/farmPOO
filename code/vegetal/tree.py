from .plants import Plant

class Tree(Plant):
    def __init__(self):
        super().__init__()
        self.amount = 1
        self.growthSpeed = 12
        self.wood = self.set_wood_amount()

    def set_wood_amount(self):
        wood: int
        if self.growthState == 0:
            wood = 0
        elif self.growthState == 1:
            wood = 10
        elif self.growthState == 2:
            wood = 100
        elif self.growthState == 3:
            wood = 500
        else:
            wood = 50
        return wood

    def update(self):
        super().update()
        self.wood = self.set_wood_amount()

