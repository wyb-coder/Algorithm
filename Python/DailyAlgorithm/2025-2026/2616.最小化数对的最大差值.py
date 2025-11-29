"""2616.最小化数对的最大差值

给你一个下标从 0 开始的整数数组 nums 和一个整数 p 。请你从 nums 中找到 p 个下标对，每个下
标对对应数值取差值，你需要使得这 p 个差值的 最大值 最小。同时，你需要确保每个下标在这 p 个下
标对中最多出现一次。

对于一个下标对 i 和 j ，这一对的差值为 |nums[i] - nums[j]| ，其中 |x| 表示 x 的 绝对值。

请你返回 p 个下标对对应数值 最大差值 的 最小值 。我们定义空集的最大值为零。


逆向思考，枚举最大差值的，自最大差值的最大值向下枚举，检查是否能选出足够的 p 个下标对
"""
from typing import List

def minimizeMax(self, nums: List[int], p: int) -> int:
    # 要求最大差值最小，排序后数组有最大/最小差值
    # 有单调性，因此二分，每次检查 mid 的条件下，能否选出 p 对
    # 如何检查：排序后相邻的差值总是最小，贪心的选取每个相邻的
    nums.sort()

    def check(x):
        count = i = 0
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= x:
                count += 1
                i += 2  # 这两个下标都不能再用了
            else:
                i += 1
        return count >= p

    left, right = 0, (nums[-1] - nums[0])
    # 最大的差值必然符合
    ans = right
    while left <= right:
        mid = (left + right) >> 1
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
