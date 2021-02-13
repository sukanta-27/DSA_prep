def partition(arr, p, r):
    if p < r:
        pivot = arr[p]
        # Current index of pivot
        i = p
        j = i+1

        while j < r and i < r:
            if arr[j] < pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
            j += 1

        arr[p], arr[i] = arr[i], arr[p]

        return i



def quickSortUtil(arr, p, r):
    if p < r:
        pivotIndex = partition(arr, p, r)
        quickSortUtil(arr, p, pivotIndex)
        quickSortUtil(arr, pivotIndex+1, r)

def quickSort(arr):
    quickSortUtil(arr, 0, len(arr))

a = list(map(int, input().split()))
quickSort(a)
print(a)
