from .sortblank import Sort


class MergeSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def merge(self, left, center, right):
        a = left
        b = center + 1
        s = 0
        S = [None for ix in range(right - left + 1)]
        while (a <= center and b <= right):
            if self.array[a]  < self.array[b]:
                S[s] = self.array[a]
                a += 1
                s += 1
            else:
                S[s] = self.array[b]
                s+=1
                b+=1
        while a <= center:
            S[s] = self.array[a]
            s+=1
            a+=1
        while b <= right:
            S[s] = self.array[b]
            s+=1
            b+=1
        for i in range(left, right+1):
            self.array[i] = S[i - left]

    def sort(self, left, right):
        if left >= right: return
        center = left + (int) ((right - left)/2)
        self.sort(left, center)
        self.sort(center+1, right)
        self.merge(left, center, right)

