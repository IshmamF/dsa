from typing import List

def bookShop(n:int, max_price: int, book_prices: List[int], num_pages: List[int]) -> int:
    '''
    Do you include the current book or not include the current book
    '''
    memo = {}
    def tryBookComb(curr_price, index):
        if index >= n:
            return 0
        if (curr_price, index) in memo:
            return memo[(curr_price, index)]
        
        withCurrentBook = 0
        if curr_price + book_prices[index] <= max_price:
            withCurrentBook = num_pages[index] + tryBookComb(curr_price + book_prices[index], index + 1)
        withoutCurrentBook = tryBookComb(curr_price, index + 1)
        memo[(curr_price, index)] = max(withCurrentBook, withoutCurrentBook)
        return max(withCurrentBook, withoutCurrentBook)
    return tryBookComb(0, 0)

n = 100
max_price = 10000
book_prices = [4] * n
num_pages = [4] * n
print(bookShop(n, max_price, book_prices, num_pages))

n = 4
max_price = 10
book_prices = [4,8,5,3]
num_pages = [5,12,8,1]
print(bookShop(n, max_price, book_prices, num_pages))