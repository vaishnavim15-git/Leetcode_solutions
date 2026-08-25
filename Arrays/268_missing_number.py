class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=0
        for i in range(0,n):
            total=total+nums[i]
        return n*(n+1)//2 - total
solution=Solution()
print(solution.missingNumber([3,0,1]))        
        