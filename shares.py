
def maxProfit(prices, n, k):

 profit = [[0 for i in range(k + 1)]
    for j in range(n)]

 for i in range(1, n):
  
  for j in range(1, k + 1):
   max_so_far = 0
   
   for l in range(i):
    max_so_far = max(max_so_far, prices[i] -
       prices[l] + profit[l][j - 1])
       
   profit[i][j] = max(profit[i - 1][j], max_so_far)
 
 return profit[n - 1][k]
prices = []
k = int(input("enter the k :"))
for i in range(1,k+1):
    a = int(input())
    prices.append(a)
n = len(prices)

print("Maximum profit is:",
 maxProfit(prices, n, k))


