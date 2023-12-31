import time
import random
import os
from tutorial import tutorial
from game import run
 
def game_start():
    os.system('cls')
    print("""
            =====================================================
              ____    ____     ____ 
             |  _ \  |  _ \   / ___|
             | |_) | | |_) | | |  _ 
             |  _ <  |  __/  | |_| |
             |_| \_\ |_|      \____|
            =====================================================                                                                 
    """)
    time.sleep(2)
    os.system("cls")
    print("Jun RPG에 오신 것을 환영합니다.")
    while(1):
        print("원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요.")
        print("1.게임시작")
        print("2.게임설명")
        print("3.게임종료")
        command = input(">>")
        if command =='1':
            run()
        elif command =='2':
            tutorial()
            os.system("cls")
        elif command == '3':
            print("이용해주셔서 감사합니다.")
            time.sleep(1.5)
            break
        else:
            os.system("cls")
            print("잘못 누르셨습니다.")
            print()

if __name__ == "__main__":
    game_start()