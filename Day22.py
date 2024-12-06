#Find H-Index

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] < i + 1:
                return i
        return len(citations)



if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

