from enum import Enum

class ItemList:
    def __init__(self):
        self.beverage = []
        self.total_price = 0
        
class Menu(Enum):
    ADD = 1
    REMOVE = 2
    CHECK = 3
    ORDER = 4
    END = 5

class Drink(Enum):
    Americano = 1
    Cafelatte = 2
    Coldbrew = 3
    Espresso = 4
    Icetea = 5
    Matchalatte = 6
    Cancelaction = 10

def select():
    print('========== What Do You Want =========')
    print('1. 음료추가')
    print('2. 음료 삭제')
    print('3. 선택 음료 확인')
    print('4. 선택 음료 주문')
    print('5. 프로그램 종료')
