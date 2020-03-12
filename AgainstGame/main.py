import player,monster

hero = player.Player('小明')
godzilla = monster.Manster()

print('进入战斗-------\n')

while True:
    
    monster_attribute=hero.damages(godzilla.name,godzilla.hp,godzilla.damage)
    godzilla.hp = monster_attribute[0]
    godzilla.damage = monster_attribute[1]
    if hero.hp <= 0 or godzilla.hp <= 0:
        if hero.hp <= 0:
            print('你阵亡了！')
            break
        else :
            print('你胜利了!')
            break