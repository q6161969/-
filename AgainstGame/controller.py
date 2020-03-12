import player,monster

hero = player.Player('小明')
m = monster.Manster()
combatdial = {'1':'战斗','2':'技能','3':'逃跑'}


class Controller:

    def main(self):
        
        print('进入战斗-------\n')
        
        while True:
            print(combatdial)
            i=input('请输入你想要进行的操作：')
            if i in combatdial:
                
                if i == '1':
                    self.combat()
                
                elif i == '2':
                    self.combat()

                else :
                    break
            
            else :
                i=input('输入错误，请从新输入：')




    def combat(self):
        
        monster_attribute=hero.damages(m)
            