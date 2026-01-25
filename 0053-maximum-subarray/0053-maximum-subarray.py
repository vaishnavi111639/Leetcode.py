class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxi=nums[0]
        for num in nums:
            currsum+=num
            maxi=max(currsum,maxi)
            currsum=max(currsum,0)
        return maxi
        