from .sortblank import Sort


class RadixSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def sort(self, num):
        #R = [0 for item in range(0, len(self.array))]
        for cycle in range(0, num):
            R = [0 for item in range(0, len(self.array))]
            N = [0 for item in range(0, 10)]

            if cycle == 0:
                calc = self.find_eigens
            elif cycle == 1:
                calc = self.find_tens
            elif cycle == 2:
                calc = self.find_hunds
            for item in self.array:
                N[calc(item)] += 1

            for item in range(1, 10):
                N[item] = N[item] + N[item - 1]

            for item in range(len(self.array) - 1, -1, -1):
                temp = calc(self.array[item])
                R[N[temp] - 1] = self.array[item]
                N[temp] -= 1

            self.array = R

    def find_hunds(self, num):
        return num // 100

    def find_tens(self, num):
        return num % 100 // 10

    def find_eigens(self, num):
        return num % 100 % 10

