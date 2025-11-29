# 327. 区间和的个数
# 区间和的个数，使用归并排序优化O(NlogN)
class Solution:
    def countRangeSum(self, nums, lower: int, upper: int) -> int:

        def mergeSort(left, right):
            if right - left <= 1:
                 return 0
            mid = (left + right) >> 1
            count = mergeSort(left, mid) + mergeSort(mid, right)
            i = j = t = mid
            temp = []
            # 对每个左半区做枚举，判断右半区中符合的
            for k in range(left, mid):
                # i: 找到右边第一个满足 preSum[i] - preSum[l] ≥ lower 的位置
                while i < right and preSum[i] - preSum[k] < lower:
                    i += 1
                # j: 找到右边第一个满足 preSum[j] - preSum[l] > upper 的位置
                while j < right and preSum[j] - preSum[k] <= upper:
                    j += 1
                count += j - i
                # 归并排序，也要保证正常的合并，对每一个k，找到其左边，其右边是下一次的左边
                while t < right and preSum[t] < preSum[k]:
                    temp.append(preSum[t])
                    t += 1
                # k本身
                temp.append(preSum[k])
            # 最后剩余的
            while t < right:
                temp.append(preSum[t])
                t += 1
            preSum[left:left + len(temp)] = temp
            return count

        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        return mergeSort(0, len(preSum))

