class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=c_sum=nums[0]
        for n in nums[1:]:
            c_sum=max(n,c_sum+n)
            max_sum=max(max_sum,c_sum)
        return max_sum
        
        