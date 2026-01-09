# 주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 입력: 주식 가격의 변화 값(리스트: prices)
# 출력: 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값
# 한 번 반복으로 최대 수익 찾기
def max_profit(prices):
    N = len(prices)
    max_pro = 0
    # 첫째 날의 주가를 주가의 최솟값으로 기억
    min_price = prices[0]
    for i in range(1, N):
        # 지금까지의 최솟값에 주식을 사서, i날에 팔 때의 수익
        profit = prices[i] - min_price
        if profit > max_pro:
            max_pro = profit
        # i날의 주가가 최솟값보다 작으면 저장
        if prices[i] < min_price:
            min_price = prices[i]

    return max_pro


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
