from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort
from sorting.shellsort import ShellSort


def main():
    arr = [1000, 42, 0, -99, 31, 17, 5, -2]
    testsort = ShellSort(arr)
    testsort.myprint()
    testsort.sort(2)
    testsort.myprint()


if __name__ == "__main__":
    main()

