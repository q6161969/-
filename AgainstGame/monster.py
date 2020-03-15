import random

manster_name = ['苦力怕','小白','僵尸']

class Manster:
    
    def __init__(self):
        self.name = random.choice(manster_name)
        self.hp = random.randint(100,220)
        self.damage = random.randint(10,35)