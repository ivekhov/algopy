from .sortblank import Sort

class HeapSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def down(self, size, root):
        X = root
        L = 2 * root + 1
        R = L + 1
        if size > L and self.array[L] > self.array[X]: X = L
        if size > R and self.array[R] > self.array[X]: X = R
        if X == root: return
        self.swap(root, X)
        self.down(size, X)

    def sort(self, size):
        for ix in range((int)(size/2) - 1, -1, -1):
            self.down(size, ix)
        for item in range(size-1, -1, -1):
            self.swap(item, 0)
            self.down(item, 0)

