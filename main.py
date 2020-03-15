from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort
from sorting.shellsort import ShellSort
from sorting.quickselect import quickselect, pick_pivot
from sorting.countingsort import CountingSort
from sorting.radixsort import RadixSort
from sorting.bucketsort import BucketSort


def main():
    #arr = [1000, 42, 0, -99, 31, 17, 5, -2]
    arr = [411, 329, 202, 104, 533,
           121, 311, 1, 4, 3,
           0, 12, 11, 53, 52,
           52, 252, 22, 1, 14]
#    print(quickselect(arr, 2, pick_pivot));

    testsort = BucketSort(arr)
    testsort.myprint()
    testsort.sort(4)
    testsort.myprint()


if __name__ == "__main__":
    main()

