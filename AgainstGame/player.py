class Player:

#   hp=200
#   damage=30

    def __init__(self,name):
        self.name = name
        self.hp = 200
        self.damage = 30

    def damages(self,monster_name,monster_hp,monster_damage):
        self.hp = self.hp - monster_damage
        monster_hp = monster_hp - self.damage
        print('你对%s造成了%d点血量.%s还剩%d点血量'%(monster_name,self.damage,monster_name,monster_hp))
        print('%s对你造成了%d点血量.你还剩%d点血量'%(monster_name,monster_damage,self.hp))
        print('-----')
        return (monster_hp,monster_damage)
    
#p=Player()
#p.damage(100,20)