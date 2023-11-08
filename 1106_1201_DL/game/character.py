import os
import csv
import json

class Character:
    save_file = os.path.join(os.path.dirname(__file__), 'save_file.csv')
    potion_price = 30
    potion_heal = 90
    exp_table = 100
    level_up_scale_ratio = 1.2

    def __init__(self, lv=1, exp=0, HP=100, max_HP=100, damage=40, money=500, potion=5) -> None:
        self.lv = lv
        self.exp = exp
        self.HP = HP
        self.max_HP = max_HP
        self.damage = damage
        self.money = money
        self.potion = potion

    def print_states(self):
        print(f'LV : {self.lv}')
        print(f'exp : {self.exp}')
        print(f'HP : {self.HP}')
        print(f'max_HP : {self.max_HP}')
        print(f'damage : {self.damage}')
        print(f'money : {self.money}')
        print(f'potion : {self.potion}')

    def save_states(self):
        with open(self.save_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # writer.writerow([self.lv, self.exp, self.HP, self.max_HP, self.damage, self.money, self.potion])
            writer.writerow([*self.__dict__.values()])

    def load_states(self):
        with open(self.save_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                self.lv = int(row[0])
                self.exp = int(row[1])
                self.HP = int(row[2])
                self.max_HP = int(row[3])
                self.damage = int(row[4])
                self.money = int(row[5])
                self.potion = int(row[6])

    def get_lv(self):
        return self.lv
    
    def set_lv(self, lv):
        self.lv = lv

    def get_HP(self):
        return self.HP
    
    def set_HP(self, HP):
        self.HP = HP
    
    def get_max_HP(self):
        return self.max_HP
    
    def set_max_HP(self, max_HP):
        self.max_HP = max_HP

    def get_exp(self):
        return self.exp

    def set_exp(self, exp):
        self.exp = exp

    def get_money(self):
        return self.money
    
    def set_money(self, money):
        self.money = money

    def attack_monster(self, monster):
        print('몬스터를 공격합니다.')
        monster.set_HP(monster.get_HP() - self.damage)
        monster.print_states()

    def kill_monster(self, monster):
        print('몬스터를 잡았습니다.')
        self.set_exp(self.get_exp() + monster.get_kill_exp())
        self.set_money(self.get_money() + monster.get_kill_money())
        self.check_lv()

    def check_lv(self):
        lv_over_lv = self.get_exp() // self.exp_table
        exp_over_lv = self.get_exp() % self.exp_table
        if lv_over_lv > 0:
            print(f'Level UP! {lv_over_lv}')
            self.set_lv(self.get_lv() + lv_over_lv)
            self.set_exp(exp_over_lv)
            for _ in range(lv_over_lv):
                self.level_up_scale_states()

    def level_up_scale_states(self):
        self.HP = round(self.HP * self.level_up_scale_ratio)
        self.max_HP = round(self.max_HP * self.level_up_scale_ratio)
        self.damage = round(self.damage * self.level_up_scale_ratio)

    def get_potion(self):
        return self.potion
    
    def set_potion(self, potion):
        self.potion = potion
    
    def drink_potion(self):
        if self.get_potion() >= 1:
            print('포션을 마십니다.')
            self.set_potion(self.get_potion() - 1)
            self.set_HP(self.get_HP() + self.potion_heal)
            if self.get_HP() > self.get_max_HP():
                self.set_HP(self.get_max_HP())
            self.print_states()
        else:
            print('포션이 부족합니다.\n')
        print(f'보유 포션 개수 : {self.get_potion()}\n')

    def buy_potions(self):
        can_buy_potions = self.get_money() // self.potion_price
        print(f'현재 소지금액은 {self.get_money()} 입니다.')
        print(f'포션 가격은 {self.potion_price} 입니다.')
        print(f'최대 구매 가능 포션 수는 {can_buy_potions} 입니다.')
        count_potions = int(input('구매할 개수를 입력하세요. > '))
        if count_potions > can_buy_potions or count_potions <= 0:
            print('입력 오류')
        else:
            self.set_money(self.get_money() - (self.potion_price * count_potions))
            self.set_potion(self.get_potion() + count_potions)
            print(f'포션 {count_potions}개 구매합니다.')
            print(f'보유 포션은 {self.get_potion()}개 입니다.')
            print(f'구매 후 소지금액은 {self.get_money()}입니다.')

    def restore(self):
        print('휴식을 취합니다.\n')
        self.set_HP(self.get_max_HP())
        self.print_states()

class Monster:
    def __init__(self, HP, damage, kill_exp, kill_money):
        self.HP = HP
        self.damage = damage
        self.kill_exp = kill_exp
        self.kill_money = kill_money

    def print_states(self):
        print(f'HP : {self.HP}')
        print(f'damage : {self.damage}')
        print(f'kill_exp : {self.kill_exp}')
        print(f'kill_money : {self.kill_money}')

    def get_HP(self):
        return self.HP
    
    def set_HP(self, HP):
        self.HP = HP

    def get_kill_exp(self):
        return self.kill_exp
    
    def get_kill_money(self):
        return self.kill_money
    
    def get_damage(self):
        return self.damage

    def attack_char(self, char):
        print('\n몬스터가 캐릭터를 공격합니다.')
        char.set_HP(char.get_HP() - self.get_damage())
        char.print_states()

class SlimeKing(Monster):
    def __init__(self):
        super().__init__(1543, 180, 900, 1500)

class Slime(Monster):
    def __init__(self):
        super().__init__(43, 60, 150, 231)

