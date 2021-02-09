def merge(arr, l, mid, r):

    m = mid - l + 1
    n = r - mid

    left = [0]*m
    right = [0]*n

    for i in range(m):
        left[i] = arr[l + i]

    for j in range(n):
        right[j] = arr[mid + 1 + j]

    i = j = 0
    k = l

    while(i < m and j < n):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < m:
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < n:
        arr[k] = right[j]
        j += 1
        k += 1

    # return result


def mergeSort(arr, l, r):
    if l < r:
        mid = l + (r-l)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)



a = list(map(int, input().split()))
mergeSort(a, 0, len(a)-1)
print(a)