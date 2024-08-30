from animals import *
from vegetal import *
from zones import *

Verger = Plot()

Chene = Tree()
Hetre = Tree()
Cerisier = Tree()

Verger.addPlant(Chene)
Verger.addPlant(Hetre)
Verger.addPlant(Cerisier)

Verger.display_plantList()