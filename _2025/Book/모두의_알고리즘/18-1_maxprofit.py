# 주어진 주식 가격을 보고 얻을 수 있는 최대 수익을 구하는 알고리즘
# 입력: 주식 가격의 변화 값(리스트: prices)
# 출력: 한 주를 한 번 사고팔아 얻을 수 있는 최대 수익 값
# 1. 모든 경우를 비교해서 가장 큰 이익을 내는 경우 찾기
def max_profit(prices):
    N = len(prices)
    max_pro = 0
    for i in range(N-1):
        for j in range(i+1, N):
            profit = prices[j] - prices[i]
            if profit > max_pro:
                max_pro = profit
    return max_pro


stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))
