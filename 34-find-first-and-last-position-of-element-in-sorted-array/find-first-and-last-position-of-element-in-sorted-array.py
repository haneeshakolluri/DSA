class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        a=[]*2
        for i in range(n):
            if nums[i]==target:
                a.append(i)
            else:
                continue
        if len(a)==0:
            return [-1,-1]
        return [a[0], a[-1]]
        