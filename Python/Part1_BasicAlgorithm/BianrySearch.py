def BinarySearchLeft(arr, left, right, num):
    while left < right:
        mid = (left + right) >> 1
        if arr[mid] >= num:
            right = mid
        else:
            left = mid + 1
    return left

def BinarySearchRight(arr, left, right, num):
    while left < right:
        mid = (left + right + 1) >> 1
        if arr[mid] <= num:
            left = mid
        else:
            right = mid - 1
    return left

N, K = [int(temp) for temp in input().split() ]
arr = [int(temp) for temp in input().split() ]
for i in range(K):
    temp = int(input())
    index = BinarySearchLeft(arr, 0, N - 1, temp)
    if arr[index] != temp:
        print("-1 -1\n")
    else:
        left = BinarySearchLeft(arr, 0, N - 1, temp)
        right = BinarySearchRight(arr, 0, N - 1, temp)
        print(left, right)

