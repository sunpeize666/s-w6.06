'''
202195057
손패택
카페 주문 관리 시스템

: 당신은 작은 카페의 주인입니다.
하루 동안 받은 주문을 관리하고 싶습니다. 
문제:
1. 손님이 주문을 할 때마다 주문을 기록하는 함수를 작성하세요. 
각 주문은 메뉴 항목(예: "아메리카노")과 수량(예: 2)으로 구성됩니다. 
2. 하루 동안의 주문 목록을 반복문을 사용하여 출력하는 기능을 작성하세요.
3. 특정 메뉴 항목의 총 주문 수량을 계산하는 함수를 작성하세요.
'''
# 비어 있는 주문 목록 정의
orders = []

# 함수는 손님 주문을 여러 번 입력할 때 사용합니다
def input_orders():
    while True:
        item = input("메뉴명을 입력해주세요：")
        quantity = int(input("수량을 입력하세요："))
        record_order(item, quantity)
        continue_input = input("주문을 계속 기록하시겠습니까?(y/n): ")
        if continue_input.lower() == 'n':
            break

# 함수는 매번 손님의 주문을 기록하는 데 사용됩니다.
def record_order(item, quantity):
    orders.append({'item': item, 'quantity': quantity})

# 함수는 일일 주문 목록을 인쇄하는 데 사용됩니다.
def print_daily_orders():
    if not orders:
        print("오늘은 주문이 없습니다.。")
    else:
        print("오늘의 주문：")
        for order in orders:
            print(f"요리 메뉴：{order['item']}，수량：{order['quantity']}")

# 함수는 모든 주문의 이름과 수량을 출력하는 데 사용됩니다.
def print_all_orders():
    if not orders:
        print("오늘은 주문이 없습니다.")
    else:
        print("모든 주문서：")
        for order in orders:
            print(f"요리 메뉴：{order['item']}，수량：{order['quantity']}")


# 함수는 특정 메뉴 항목의 총 주문 수량을 계산하는 데 사용됩니다
def total_orders(item):
    total = 0
    for order in orders:
        if order['item'] == item:
            total += order['quantity']
    return total


input_orders()
print_daily_orders()

# 모든 주문서의 이름과 수량을 출력합니다
print_all_orders()

# 특정 메뉴 항목의 총 주문 수량 계산
menu_item = input("총 주문 수량을 조회할 메뉴명을 입력해주세요：")
print(f"{menu_item}총주문수량：{total_orders(menu_item)}")
