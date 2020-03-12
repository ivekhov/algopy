from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort


def main():
    arr = [1000, 42, 0, -99, 31, 17, 5, -2]
    testsort = HeapSort(arr)
    testsort.myprint()
    testsort.sort(len(arr))
    testsort.myprint()


if __name__ == "__main__":
    main()

