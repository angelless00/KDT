class VendingMachine:
    def __init__(self,input_dict,money):
        # 초기자판기재고량 dict형태
        self.input_money=money
        self.inventory=input_dict
        
            
    def run(self):
        # 메뉴호출함수
        print('-'*30)
        print(f' 커피 자판기 잔액:({self.input_money}원)')
        print('-'*30)
        print(' 1. 블랙 커피')
        print(' 2. 프림 커피')
        print(' 3. 설탕 프림 커피')
        print(' 4. 재료 현황')
        print(' 5. 종료')

    def inventory_print(self):
        print('-'*80)
        print(f"재료현황: coffee: {self.inventory['coffee']}",end=' ') 
        print(f"cream: {self.inventory['cream']}",end=' ') 
        print(f"sugar: {self.inventory['sugar']}",end=' ')
        print(f"water: {self.inventory['water']}",end=' ') 
        print(f"cup: {self.inventory['cup']}",end=' ') 
        print(f"change: {self.inventory['change']}")  
        print('-'*80)

# 블랙커피
    def black(self):
        self.inventory['change']+=300
        self.input_money-=300
        print(f"블랙 커피를 선택하셨습니다. 잔액: {self.input_money}")
        self.inventory['coffee']-=30
        self.inventory['water']-=100
        self.inventory['cup']-=1
        self.inventory_print()
   
# 프림커피
    def prim(self):
        self.inventory['change']+=300
        self.input_money-=300
        print(f'설탕 프림 커피를 선택하셨습니다. 잔액: {self.input_money}')
        self.inventory['coffee']-=15
        self.inventory['cream']-=15
        self.inventory['water']-=100
        self.inventory['cup']-=1
        self.inventory_print()


#설탕프림커피
    def sugar_prim(self): 
        self.inventory['change']+=300
        self.input_money-=300
        print(f'설탕 프림 커피를 선택하셨습니다. 잔액: {self.input_money}')
        self.inventory['coffee']-=10
        self.inventory['cream']-=10
        self.inventory['sugar']-=10
        self.inventory['water']-=100
        self.inventory['cup']-=1
        self.inventory_print()




    def exit(self):
        print('-'*30)
        print('커피 자판기 동작을 종료합니다.')
        print('-'*30)
        # 종료 할것!
    
    def main(self):
         while self.input_money>=300:
            self.run()
            menu=int(input('메뉴를 선택하세요: '))
            if menu==1:
                if (self.inventory['coffee']>=30) & (self.inventory['water']>=100)&(self.inventory['cup']>=1):
                    self.black()
                else:
                    print('재료가 부족합니다.')
                    self.inventory_print()
                    print(f"{self.input_money}원을 반환합니다.")   
                    self.exit() 
                    break  
            elif menu==2:
                if (self.inventory['coffee']>=15) & (self.inventory['cream']>=15) &(self.inventory['water']>=100)&(self.inventory['cup']>=1):
                    self.prim()
                else:
                    print('재료가 부족합니다.')
                    self.inventory_print()
                    print(f"{self.input_money}원을 반환합니다.")   
                    self.exit()
                    break
            elif menu==3:
                if (self.inventory['coffee']>=10) & (self.inventory['cream']>=10) &(self.inventory['sugar']>=10) & (self.inventory['water']>=100)&(self.inventory['cup']>=1):
                    self.sugar_prim()
                else:
                    print('재료가 부족합니다.')
                    self.inventory_print()
                    print(f"{self.input_money}원을 반환합니다.")   
                    self.exit()
                    break
            elif menu==4:
                self.inventory_print()
            elif menu==5:
                print(f'종료를 선택했습니다. {self.input_money}원이 반환됩니다.')
                self.exit()
                break
            if self.input_money<300:
                print(f"잔액이 ({self.input_money}원)이 300원 보다 작습니다.")
                print(f"{self.input_money}원이 반환됩니다.")    
                self.exit()






# VendingMachine 객체생성
inventory_dict={'coffee':100,'cream':100,'sugar':100,'water':500,'cup':5,'change':0}

money=int(input('동전을 투입하세요: '))
coffee_machine=VendingMachine(inventory_dict,money)
if money<300:
    print(f'투입된 돈({money}원)이 300원보다 작습니다.')    
    print(f'{money}원을 반환합니다.')
    coffee_machine.exit()
else: 
    coffee_machine.main()