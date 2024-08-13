def remove_menu(item_list):
    print('========== Remove Menu ==========')
    for i in range(len(item_list.beverage)):
        print(f'{i+1}.{item_list.beverage[i]}')
    
    choice = int(input("선택: "))
    print("\n\n")
    
    for i in range(len(item_list.beverage)):
        if choice == i+1:
            item_list.beverage.remove(item_list.beverage[i])
            item_list.total_price -= 4500
            print(f'{item_list.beverage[i]}주문이 취소되었습니다.')
            print("\n\n")
            print(item_list.beverage)
            print(item_list.total_price)
            return

        else:
            print('다시 입력해주세요')


# 선택 음료 확인 상태에서 음료 삭제를 선택해 잘못 추가한 음료를 삭제

# ========== Remove Menu ==========
# ~
# ~

# 선택: Enter
# ~ 주문이 취소되었습니다.

# 잘못된 음료 삭제 후 다시 선택 음료 확인 메뉴를 선택하면 한 잔이 삭제되어야 함