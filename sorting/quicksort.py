class QuickSort:

    def __init__(self, arr):
        self.array = arr
    
    def swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp
    
    def myprint(self):
        for item in self.array:
            print('{}'.format(item), end=" ")
        print("\n")

    def partition(self, left, right):
        pivot = self.array[right]
        index = left - 1
        for j in range(left, right + 1):
            if self.array[j] <= pivot:
                index += 1
                self.swap(index, j)
        return index

    def sort(self, left, right):
        if left >= right: return
        center = self.partition(left, right)
        self.sort(left, center-1);
        self.sort(center+1, right)
