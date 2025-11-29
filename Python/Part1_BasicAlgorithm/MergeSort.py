def MergeSort(arr, left, right):
    if left >= right:
        return 0
    mid = (left + right) >> 1
    MergeSort(arr, left, mid)
    MergeSort(arr, mid + 1, right)
    # 归并
    i, j, tempArr = left, mid + 1, []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tempArr.append(arr[i])
            i += 1
        else:
            tempArr.append(arr[j])
            j += 1
            # 全局变量
            global reverseNum
            reverseNum += mid - i + 1

    while i <= mid:
        tempArr.append(arr[i])
        i += 1
    while j <= right:
        tempArr.append(arr[j])
        j += 1
    # 切片赋值
    arr[left: right + 1] = tempArr

N = int(input())
arr = [int(temp) for temp in input().split()]
# 计算逆序对
reverseNum = 0
MergeSort(arr, 0, N - 1)
for i in arr:
    print(i, end = " ")
# print(reverseNum)

