import os
from character import *
from utils import *


while True:
    print('======== 메인 화면 ========')
    next_move = int(input('\nGO-AI 온라인에 오신 것을 환영합니다.\n\n'
                  '1. 새로운 게임 시작하기\n'
                  '2. 지난 게임 불러오기\n'
                  '3. 게임 종료하기\n'
                  '다음 중 어떤 것을 하시겠습니까? > '))
    if next_move == 1:
        print('\n새로운 캐릭터를 생성합니다.')
        new_char = Character()
        new_game = game_main(new_char)
        new_game()

    elif next_move == 2:
        save_file = os.path.join(os.path.dirname(__file__), 'save_file.csv')
        if os.path.exists(save_file):
            print('\n저장된 파일을 불러옵니다.')
            my_char = Character()
            my_char.load_states()
            my_char.print_states()
            my_game = game_main(my_char)
            my_game()

        else:
            print('\n저장된 파일이 없습니다.\n'
                  '메인 화면으로 돌아갑니다.\n')
            continue
    
    elif next_move == 3: 
        print('게임을 종료합니다.')
        break
    else:
        print('입력 오류. 다시 선택하시오.')