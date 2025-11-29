# 2311. 小于等于 K 的最长二进制子序列
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # 贪心的删除最左侧的1
        N = len(s)
        tempValue = int(s, 2)
        while tempValue > k:
            index = s.find('1')
            s = s[:index] + s[index + 1:]
            tempValue = int(s, 2)
        return len(s)