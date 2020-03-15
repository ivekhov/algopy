from math import floor
from .sortblank import Sort


class BucketSort(Sort):

    def __init__(self, arr):
        self.array = arr

    def sort(self, count_buckets):
        coef = count_buckets / max(self.array)
        bundle = []
        for i in range(0, count_buckets+1):
            bundle.append([])
        for item in self.array:
            bundle[floor(item * coef)].append(item)
        final_array = [0 for item in self.array]

        counter = 0
        for bucket in bundle:
            bucket = sorted(bucket)
            for item in bucket:
                final_array[counter] = item
                counter += 1
        self.array = final_array

