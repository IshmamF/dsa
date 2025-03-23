import sys
n, max_price = map(int, sys.stdin.readline().split())
book_prices = list(map(int, sys.stdin.readline().split()))
num_pages = list(map(int, sys.stdin.readline().split()))

dp = [0] * (max_price + 1)
for i in range(n):
    book_price = book_prices[i]
    num_page = num_pages[i]
    for curr_price in range(max_price, book_price - 1, -1):
        dp[curr_price] = max(dp[curr_price], dp[curr_price - book_price] + num_page)

print(dp[-1])
    

