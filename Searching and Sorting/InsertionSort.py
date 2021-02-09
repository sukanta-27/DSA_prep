def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return

a = [10, 3 , 2, 5, 1, 2, 7]
insertionsort(a)
print(a)