def binarySearchUtil(arr, left, right, item):

    if left >= right:
        return -1
    mid = (left + (right - left)//2)

    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binarySearchUtil(arr, left, mid, item)
    elif arr[mid] < item:
        return binarySearchUtil(arr, mid+1, right, item)


def binarySearch(arr, item):
    return binarySearchUtil(arr, 0, len(arr), item)


a = list(map(int, input().split()))
t = int(input())

while(t > 0):
    i = int(input())
    print(binarySearch(a, i))
    t -= 1