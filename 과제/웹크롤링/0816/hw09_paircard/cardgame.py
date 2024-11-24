# 각 클래스의 객체 생성 및 게임 진행

from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 Player 객체 생성
    player1=Player('흥부')
    player2=Player('놀부')

    dealer=GameDealer()
    deck=dealer.make_deck()
    deck=dealer.shuffle_deck()

    # 카드게임 1단계
    
    
    p1,p2=dealer.give_card(10)
    player1.add_card_list(p1)
    player2.add_card_list(p2)
    dealer.deck_print()
    player1.open_card()
    player2.open_card()
    n=1

    while True:
        print('\n')
        n+=1
        input(f'[{n}]단계: 다음단계 진행을 위해 Enter 키를 누르세요')
        if n>=3:
            p1,p2=dealer.give_card(4)
            player1.add_card_list(p1)
            player2.add_card_list(p2)
            dealer.deck_print()
        
        print('='*50)
        print(f'[{player1.name}: 숫자가 같은 한쌍의 카드 검사]')
        player1.check_one_pair_card()
        player1.open_card()

        print('='*50)
        print(f'[{player2.name}: 숫자가 같은 한쌍의 카드 검사]')
        player2.check_one_pair_card()
        player2.open_card()

        if (len(dealer.deck)==0) or (len(player1.holding_card_list)==0) or (len(player2.holding_card_list)==0):
            break



       
    


if __name__=='__main__':
    play_game()