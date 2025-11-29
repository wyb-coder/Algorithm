class Solution:
    def maxSubsequence(self, nums, k: int):
        # 生成下标数组
        idx = sorted(range(len(nums)), key=lambda i: nums[i])
        idx = sorted(idx[-k:])
        return [nums[i] for i in idx]