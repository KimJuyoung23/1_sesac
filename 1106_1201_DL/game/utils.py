from character import *

class game_main:
    def __init__(self, character):
        char_param = [*character.__dict__.values()]
        self.char = Character(*char_param)
        
    def __call__(self):
        print('-------- 게임 시작 --------')
        while True:
            next_move = int(input('\n---- 캐릭터 액션 목록 ----\n'
                                    '1. 전투를 시작합니다.\n'
                                    '2. 휴식을 취합니다.\n'
                                    '3. 포션을 구매합니다.\n'
                                    '4. 캐릭터 정보 보기\n'
                                    '9. 저장 후 메인 화면으로 돌아갑니다.\n'
                                    '다음 행동을 선택하시오 > '))
            if next_move == 1:
                self.char.save_states()
                while True:
                    monster_pick = int(input('\n---- 몬스터 목록 ----\n'
                                                '1. 슬라임\n'
                                                '2. 슬라임 킹\n'
                                                '몬스터 선택 > '))
                    if monster_pick == 1:
                        mon = Slime()
                        break
                    elif monster_pick == 2:
                        mon = SlimeKing()
                        break
                    else:
                        print('입력 오류')
                
                print('전투를 시작합니다.')
                print('--- 몬스터 정보 ---')
                mon.print_states()
                while True:
                    battle_move = int(input('\n---- 전투 모드----\n'
                                            '1. 공격하기\n'
                                            '2. 포션 마시기\n'
                                            '3. 도망가기\n'
                                            '4. 캐릭터 정보 보기\n'
                                            '전투 행동 선태 > '))
                    if battle_move == 1:
                        self.char.attack_monster(mon)
                        if mon.get_HP() <= 0:
                            self.char.kill_monster(mon)
                            print('전투가 종료됩니다.')
                            break

                    elif battle_move == 2:
                        self.char.drink_potion()

                    elif battle_move == 3:
                        print('전투에서 도망갑니다.')
                        break

                    elif battle_move == 4:
                        self.char.print_states()
                        continue

                    else:
                        print('입력 오류')
                        continue

                    # 몬스터 공격 차례
                    mon.attack_char(self.char)
                    if self.char.get_HP() <= 0:
                        print('캐릭터가 사망했습니다.')
                        print('전투가 종료됩니다.')
                        self.char.restore()
                        break


            elif next_move == 2:
                self.char.restore()

            elif next_move == 3:
                self.char.buy_potions()

            elif next_move == 4:
                self.char.print_states()
            
            elif next_move == 9:
                print('저장 후 메인화면으로 돌아갑니다.')
                self.char.save_states()
                break

            else:
                print('입력 오류. 다시 선택하십시오')