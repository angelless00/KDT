# 1벌의 카드 덱 생성 기능 :리스트로 구현
# 각 play들에게 카드를 나누어주는 기능
#       => 자신이 가진 deck 에서 제거하여 다른 선수들에게 제공

from card import Card
import random

class GameDealer:
    
    def __init__(self):
        self.deck=list()
        self.suit_number=13

    def deck_print(self):
        print('-'*50)
        print(f'[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}')
        for i in range(len(self.deck)):
            print(self.deck[i],end='')
            if (i+1)%13==0:
                print()
        print()


    def make_deck(self):
        card_suits=["♠",'♥','♣','◆']
        card_number=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for suits in card_suits:
            for number in card_number:
                self.deck.append(Card(suits,number))
        print(f'[GameDealer] 초기 카드 생성')
        self.deck_print()

    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        print(f'[GameDealer] 카드 랜덤하게 섞기')
        self.deck_print()

    
    def give_card(self,num):
        print('='*50)
        print(f'카드 나누어 주기 : {num}장')
        p1=random.sample(self.deck,num)
        for i in p1:
            self.deck.remove(i)
        p2=random.sample(self.deck,num)
        for i in p2:
            self.deck.remove(i)
        return p1,p2
    

    
