import random

manster_name = ['苦力怕','小白','僵尸']

class Manster:
    
    def __init__(self):
        self.name = random.choice(manster_name)
        self.hp = random.randint(50,120)
        self.damage = random.randint(10,35)