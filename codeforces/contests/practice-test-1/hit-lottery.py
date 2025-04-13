n = int(input())
bills = [100,20,10,5,1]

numBillsNeeded = 0
for bill in bills:
    if bill > n:
        continue
    numBillsNeeded += n//bill 
    n = n % bill
print(numBillsNeeded)