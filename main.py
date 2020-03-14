from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort
from sorting.shellsort import ShellSort
from sorting.quickselect import quickselect, pick_pivot
from sorting.countingsort import CountingSort

def main():
    #arr = [1000, 42, 0, -99, 31, 17, 5, -2]
    arr = [11, 9, 0, 4, 3, 2, 1]
#    print(quickselect(arr, 2, pick_pivot));

    testsort = CountingSort(arr)
    testsort.myprint()
    testsort.sort()
    testsort.myprint()


if __name__ == "__main__":
    main()

