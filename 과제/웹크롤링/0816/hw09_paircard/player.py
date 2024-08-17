# 자신이 가지고 있는 카드 관리
# 두 장의 동일한 카드를 제거하는 기능


class Player:
    def __init__(self,name):
        self.name=name
        self.holding_card_list=list()
        self.open_card_list=list()

    def add_card_list(self,card_list):
        self.holding_card_list.extend(card_list)

    def display_two_card_lists(self):
        pass
        


    def check_one_pair_card(self):
        pair_card_list=[]
        for i in range(len(self.holding_card_list)-1):
            for j in range(i+1,len(self.holding_card_list)):
                if self.holding_card_list[i].number==self.holding_card_list[j].number:
                    if self.holding_card_list[i] in pair_card_list:
                        continue
                    else:
                        pair_card_list.extend([self.holding_card_list[i],self.holding_card_list[j]])
        self.open_card_list.extend(pair_card_list)
        for drop_card in pair_card_list:
            self.holding_card_list.remove(drop_card)
            
            

                    

    def print_card(self,card_list):
        for i in range(len(card_list)):
            print(card_list[i],end='')
            if (i+1)%13==0:
                print()

    def open_card(self):
        print('='*50)
        print(f'[{self.name}] Open card list: {len(self.open_card_list)}')
        self.print_card(self.open_card_list)
        print('\n\n')
        print(f'[{self.name}] Holding card list: {len(self.holding_card_list)}')
        self.print_card(self.holding_card_list)
        print('\n')