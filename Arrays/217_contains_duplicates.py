class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        s=set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
solution=Solution()