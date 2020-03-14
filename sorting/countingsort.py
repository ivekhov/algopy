from .sortblank import Sort


class CountingSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def sort(self):
        k = max(self.array)
        C = [0 for el in range(0, k+1)]
        for item in  self.array:
            C[item] += 1
        b = 0
        for outer in range(0, k+1):
            for inner in range(0, C[outer]):
                self.array[b] = outer
                b += 1

