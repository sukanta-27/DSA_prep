class MinHeap:

    def __init__(self, size):
        self.heap = [0]*size
        self.heapSize = 0

    def insert(self, val):
        if self.heapSize >= len(self.heap):
            return "Heap is already full"

        self.heap[self.heapSize] = val
        self.heapSize += 1
        if self.heapSize > 1:
            i = self.heapSize - 1
            while i > 0:
                parent = (i-1)//2

                if self.heap[parent] > self.heap[i]:
                    self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                
                i = parent
        return

    def delete(self):
        # Retrieve the element to be deleted
        _min = self.heap[0]
        self.heap[self.heapSize-1], self.heap[0] = self.heap[0], self.heap[self.heapSize-1]
        self.heapSize -= 1
        
        i = 0
        while i < self.heapSize:
            child = 2*i + 1

            if child >= self.heapSize:
                break
    
            if child < self.heapSize - 1 and self.heap[child] > self.heap[child+1]:
                child += 1
            
            if self.heap[child] < self.heap[i]:
                self.heap[child], self.heap[i] = self.heap[i], self.heap[child]

            i = child

        return _min

    def heapify(self, index):
        # Two base conditions:
        # 1. If the element is the root element and doesn't have a child
        # 2. If the element is smaller than both its children
        left = 2*index + 1
        right = 2*index + 2
        smaller = None
        if left >= self.heapSize and right >= self.heapSize:
            # Leaf node
            return
        elif left >= self.heapSize:
            smaller = right
        elif right >= self.heapSize:
            smaller = left
        else:
            if self.heap[left] <= self.heap[right]:
                smaller = left
            else:
                smaller = right
        
        if self.heap[index] > self.heap[smaller] :
            self.heap[index], self.heap[smaller] = self.heap[smaller], self.heap[index]
            self.heapify(smaller)
        else:
            return

    def buildHeap(self, vals):
        if not isinstance(vals, list):
            return
        
        self.heapSize = len(vals)
        self.heap = vals
        for i in range(len(vals)//2, -1, -1):
            self.heapify(i)

    def __repr__(self):
        res = ""
        for i in range(0, self.heapSize):
            res += str(self.heap[i])+" "
        return res


if __name__ == '__main__':
    n = int(input("Enter the number of elements to be added: "))
    heap = MinHeap(n)


    arr = list(map(int, input("Enter values to heapify: ").split()))
    # for i in range(n):
    #     heap.insert(arr[i])
    heap.buildHeap(arr)
    print(heap)

    k = int(input("Enter number of items to be deleted: "))
    for _ in range(k):
        heap.delete()
        print(heap)

    print(heap.heap)
    