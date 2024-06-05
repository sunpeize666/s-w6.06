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

# 함수는 주문을 기록하는 데 사용됩니다.
def record_order(item, quantity):
    orders.append({'item': item, 'quantity': quantity})

# 함수는 주문 목록을 인쇄하는 데 사용됩니다.
def print_orders():
    for order in orders:
        print(f"주문: {order['item']}, 수량: {order['quantity']}")

# 함수는 특정 메뉴 항목의 총 주문 수량을 계산합니다
def total_orders(item):
    total = 0
    for order in orders:
        if order['item'] == item:
            total += order['quantity']
    return total

# 테스트 한번 해봐
record_order("아메리카노", 2)
record_order("라떼", 1)
record_order("아메리카노", 1)

print("오늘의 주문：")
print_orders()

print("아메리카노 총 주문 수량\n：", total_orders("아메리카노"))
