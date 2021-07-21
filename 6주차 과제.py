# STEP 1
# Q1. 코드 3
# Q2. 
class Pokemon:
    def __init__(self, name, type, attack, hp):
        self.name = name
        self.type = type
        self.attack = attack
        self.hp = hp
    def normalattack(self):
        print("{0}의 차례다!".format(self.name))
        print("{0} 피해를 입혔다!".format(self.attack))
    def hit(self, dmg):
        self.hp -= dmg
        print("{0}은(는) {1} 피해를 입었다!".format(self.name, dmg))
        print()
        if self.hp <= 0:
            print("{0}은(는) 쓰러졌다!".format(self.name))
            print()
jiu_pokemon = Pokemon("피카츄", "전기", 55, 120)
# Q3. 코드 4
# Q4. 
jiu_pokemon.clothes = "idol"
# Q5. self.name, self.attack
# Q6. self.hp -= dmg, self.name, dmg, self.name

# STEP 2
class Electric:
    def __init__(self, skill_name, skill_dmg):
        self.skill_name = skill_name
        self.skill_dmg = skill_dmg
    def skill(self):
        print("{0} 스킬로 공격! {1} 피해를 입혔다!".format(self.skill_name, self.skill_dmg))

# STEP 3
# Q1. 코드 4
# Q2. 코드 3
# Q3.
class Pikachu(Pokemon, Electric):
    def __init__(self, name, type, attack, hp, skill_name, skill_dmg, clothes):
        Pokemon.__init__(self, name, type, attack, hp)
        Electric.__init__(self, skill_name, skill_dmg)
        self.clothes = clothes
    def skillattack(self):
        print("{0}의 차례다!".format(self.name))
        self.skill()
jiu_pikachu = Pikachu("피카츄", "전기", 55, 120, "백만볼트", 80, "doctor")
rocket_pikachu = Pikachu("로켓단", "전기", 45, 140, "볼트태클", 100, "idol")
# Q4. 
jiu_pikachu.normalattack()
rocket_pikachu.hit(jiu_pikachu.attack)
rocket_pikachu.normalattack()
jiu_pikachu.hit(rocket_pikachu.attack)
# Q5. 
#로켓단의 차례다!
#45 피해를 입혔다!
#피카츄은(는) 45 피해를 입었다!
# Q6. ???