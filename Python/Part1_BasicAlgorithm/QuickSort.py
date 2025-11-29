def QuickSort(arr, left, right):
    if left > right:
        return 0
    pivot = arr[(left + right) >> 1]
    i, j = left, right
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if i < right:
        QuickSort(arr, i, right)
    if j > left:
        QuickSort(arr, left, j)

N = int(input())
arr = [int(temp) for temp in input().split()]
QuickSort(arr, 0, N - 1)
for i in arr:
    print(i, end=" ")



