class Solution:
    def stonks(self, prices):
            #type prices: list of int
            #return type: int
        least1 = 1000000
        max1 = 0
        least2 = 0
        maxprice2 = 0
        maxprofit2 = 0
        profit1 = []
        profit2=[0]*len(prices)
        for i in prices:
            if i < least1:
                least1 = i
            else: 
                max1 = (max(i-least1,max1))
            profit1.append(max1)
        for i in range(len(prices)-1,-1,-1):#backward
            x = prices[i]
            if x > maxprice2:
                maxprice2 = x
            else: 
                maxprofit2 = max(maxprofit2, maxprice2-x)
            profit2[i] = maxprofit2
        greatest = 0
        for i in range(len(prices)):
            sum = profit1[i]+profit2[i]
            if sum > greatest:
                greatest = sum
        return greatest
                    
                    

        pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()
