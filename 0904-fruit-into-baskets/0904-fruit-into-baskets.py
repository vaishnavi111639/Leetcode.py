class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left,right=0,0
        n=len(fruits)
        maxlen=0
        mpp={}
        while right<n:
            if fruits[right] in mpp:
                mpp[fruits[right]]+=1
            else:
                mpp[fruits[right]] =1
            while len(mpp)>2:
                mpp[fruits[left]]-=1
                if mpp[fruits[left]]==0:
                    del mpp[fruits[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
