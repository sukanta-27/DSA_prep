class MaxHeap:
    
    def __init__(self, size):
        self.heap = [0]*size
        self.heapSize = 0

    def insert(self, val):
        if self.heapSize >= len(self.heap):
            print("Heap is already full")
            return

        self.heap[self.heapSize] = val
        self.heapSize += 1

        if self.heapSize > 1:
            i = self.heapSize -1
            while i > 0:
                parent = (i-1)//2
                if parent < 0:
                    break

                if self.heap[i] > self.heap[parent]:
                    self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
                

    def delete(self):
        _max = self.heap[0]
        self.heap[0], self.heap[self.heapSize-1] = self.heap[self.heapSize-1], self.heap[0]
        self.heapSize -= 1

        i = 0
        while i < self.heapSize:
            child = 2*i + 1
            if child >= self.heapSize:
                break

            if child < self.heapSize -1 and self.heap[child] < self.heap[child + 1]:
                child += 1

            if self.heap[child] > self.heap[i]:
                self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child
        
        return _max

    def heapify(self, index):
        
        left = 2*index + 1
        right = 2*index + 2
        larger = None

        if left >= self.heapSize and right >= self.heapSize:
            return
        elif left >= self.heapSize:
            larger = right
        elif right >= self.heapSize:
            larger = left
        else:
            if self.heap[left] >= self.heap[right]:
                larger = left
            else:
                larger = right

        if self.heap[larger] > self.heap[index]:
            self.heap[larger], self.heap[index] = self.heap[index], self.heap[larger]
            self.heapify(larger)
        else:
            return
        
    def buildHeap(self, vals):
        self.heap = vals
        self.heapSize = len(vals)

        for i in range((self.heapSize)//2, -1, -1):
            self.heapify(i)

    def __repr__(self):
        res = ""
        for i in range(self.heapSize):
            res += str(self.heap[i]) + " "

        return res


if __name__ == '__main__':
    n = int(input("Enter the number of elements to be added: "))
    heap = MaxHeap(n)


    arr = list(map(int, input("Enter values to heapify: ").split()))
    # for i in range(n):
    #     heap.insert(arr[i])

    heap.buildHeap(arr)
    print(heap)

    k = int(input("Enter number of items to be deleted: "))
    for _ in range(k):
        print("Deleted: ", heap.delete())
        print(heap)

    print(heap.heap)
