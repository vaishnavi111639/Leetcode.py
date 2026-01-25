class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        n=len(arr)
        left=0
        right=k-1
        Sum=sum(arr[0:k])
        maxSum=Sum
        j=n-1
        for i in range(k-1,-1,-1):
            Sum-=arr[i]
            Sum+=arr[j]
            maxSum=max(maxSum,Sum)
            j-=1
        return maxSum