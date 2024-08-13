from common import Drink

def add_menu(item_list):
    print('========== Add Menu ==========')
    print('1.아메리카노: 4500')
    print('2.카페라떼: 5000')
    print('3.콜드브루: 4900')
    print('4.에스프레소: 4000')
    print('5.아이스티: 5900')
    print('6.말차라떼: 6100')
    print('10. 동작 취소')
    
    choice = int(input("선택: "))
    print("\n\n")
    
    if choice == Drink.Americano.value:
        item_list.beverage.append("Americano")
        item_list.total_price += 4500
        print("Americano 추가")
        print("\n\n")
    elif choice == Drink.Cafelatte.value:
        item_list.total_price += 5000
        item_list.beverage.append("Cafelatte")
        print("Cafelatte 추가")
        print("\n\n")
    elif choice == Drink.Coldbrew.value:
        item_list.beverage.append("Coldbrew")
        item_list.total_price += 4900
        print("Coldbrew 추가")
        print("\n\n")
    elif choice == Drink.Espresso.value:
        item_list.beverage.append("Espresso")
        item_list.total_price += 4000
        print("Espresso 추가")
        print("\n\n")
    elif choice == Drink.Icetea.value:
        item_list.beverage.append("Icetea")
        item_list.total_price += 5900
        print("Icetea 추가")
        print("\n\n")
    elif choice == Drink.Matchalatte.value:
        item_list.beverage.append("Matchalatte")
        item_list.total_price += 6100
        print("Matchalatte 추가")
        print("\n\n")

    elif choice == Drink.Cancelaction.value:
        print("Cancelaction 추가")
        print("\n\n")

    print(item_list.beverage)
    print(item_list.total_price)