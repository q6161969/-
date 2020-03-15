import player,monster

hero = player.Player('小明')
m = monster.Manster()
combatdial = {'1':'战斗','2':'技能','3':'逃跑'}
result = None

class Controller:

    def main(self):
        
        print('进入战斗-------\n')
        
        while True:
            print(combatdial)
            i=input('请输入你想要进行的操作：')
            if i in combatdial:
                
                if i == '1':
                    result=hero.damages(m)
                
                elif i == '2':
                    result=hero.damages(m)

                else :
                    break
                    
                if result == True:
                    #print('你赢了！')
                    break
                elif result == False:
                    #print('你输了!')
                    break

            else :
                i=input('输入错误，请从新输入：')




    #def combat(self):
        
        #monster_attribute=
            