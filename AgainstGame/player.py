class Player:

#   hp=200
#   damage=30

    def __init__(self,name):
        self.name = name
        self.hp = 200
        self.damage = 30

    def damages(self,monster):
        self.hp = self.hp - monster.damage
        monster.hp = monster.hp - self.damage
        print('你对%s造成了%d点血量.%s还剩%d点血量'%(monster.name,self.damage,monster.name,monster.hp))
        print('%s对你造成了%d点血量.你还剩%d点血量'%(monster.name,monster.damage,self.hp))
        print('-----')
        if self.hp <= 0 or monster.hp <= 0:
                if self.hp <= 0:
                    print('你阵亡了！')
                    
                    #return False
                else :
                    print('你胜利了!')
                    #return False
        
        #return True
    
#p=Player()
#p.damage(100,20)