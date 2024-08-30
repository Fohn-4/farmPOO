from abc import ABC, abstractmethod
from globals import G_turn

class Plant(ABC):
    def __init__(self):
        self.name: str
        self.amount: int = 0
        self.growthSpeed: int = 0
        self.growthState: int = 0 # 0:Sprout 1:Young 2:Adult 3:Old 4:rotten

    def growth(self):
        if G_turn % self.growthSpeed == 0:
            self.growthState += 1


    def update(self):
        self.growth()
