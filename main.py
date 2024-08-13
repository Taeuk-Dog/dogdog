# Main function
from common import Menu, ItemList, select
from feature1 import add_menu
from feature2 import remove_menu
from check import check_menu

def main():
    item_list = ItemList()
    while True:
        select()
        choice = int(input("선택: "))
        print("\n\n")

        if choice == Menu.ADD.value:
            add_menu(item_list)
            print("\n\n")
        elif choice == Menu.REMOVE.value:
            remove_menu(item_list)
            print("\n\n")
        elif choice == Menu.CHECK.value:
            check_menu(item_list)
            print("\n\n")
        # elif choice == Menu.ORDER.value:
            # if order(item_list):
                # print("주문 완료. 프로그램을 종료합니다.")
                # break
            # else:
                # print("주문 보류!")
                # print("\n\n")
        # elif choice == Menu.END.value:
        #     print("프로그램을 종료합니다")
        #     break
        else:
            print("잘못된 입력입니다. 동작을 취소합니다.")
            break

if __name__ == "__main__":
    main()