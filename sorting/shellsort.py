from .sortblank import Sort

class ShellSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def sort(self, param):
        h = 1
        size = len(self.array)
        while h < (size / param):
            h = h * param + 1
        while h >= 1:
            for outer in range(h, size, 1):
                for inner in range(outer, h-1, -h):
                    if self.array[inner] <= self.array[inner-h]:
                        self.swap(inner, (inner - h))
            h = (int)(h / param)

