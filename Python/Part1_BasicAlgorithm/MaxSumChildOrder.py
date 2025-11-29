# 和最大的子序列，注意未要求连续
def maxSubsequence(nums, k):
    # sorted返回一个新的列表
    # key，指定sorted按给出的方法排序：对每个下标i，按nums[i]的值比较
    # 所有下标按值从小到大排序
    idx = sorted(range(len(nums)), key=lambda i: nums[i])

    # 取最后也就是最大的
    # 取最大k个下标，再排一遍序以保证顺序
    idx = sorted(idx[-k:])

    return [nums[i] for i in idx]

nums = [-1,-2,3,4]
res = maxSubsequence(nums, 3)
for i in res:
    print(i)