import os
import time
from datetime import datetime
from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort
from sorting.shellsort import ShellSort
from sorting.quickselect import quickselect, pick_pivot
from sorting.countingsort import CountingSort
from sorting.radixsort import RadixSort
from sorting.bucketsort import BucketSort


def main():
    arr = []
    with open("./tests/test.txt", 'r') as f:
        while True:
            temp = f.readline()
            if temp == "\n": break
            item = int( temp.rstrip())
            arr.append(item )

    start_time = time.perf_counter( )

    # test_sort = QuickSort(arr)
    # test_sort = MergeSort(arr)
    # test_sort = HeapSort(arr)
    test_sort = ShellSort(arr)
    # test_sort = BucketSort(arr)
    # test_sort = CountingSort(arr)
    # test_sort = RadixSort(arr)


    test_sort.myprint_first(10)
    test_sort.myprint_last(10)
    #test_sort.sort() #1000 for Bucket
    # test_sort.sort(0, 1000000) #1000000 for Quick
    test_sort.sort(2) #2 for Shell
    # test_sort.sort(len(arr)) # for Heap

    duration = time.perf_counter() - start_time
    print(duration)
    test_sort.myprint_first(10)
    test_sort.myprint_last(10)


if __name__ == "__main__":
    main()


'''
    #arr = [1000, 42, 0, -99, 31, 17, 5, -2]
    arr = [411, 329, 202, 104, 533,
           121, 311, 1, 4, 3,
           0, 12, 11, 53, 52,
           52, 252, 22, 1, 14]
#    print(quickselect(arr, 2, pick_pivot));

    print('counting: ')
    testsort = CountingSort(arr)
    testsort.myprint()
    testsort.sort()
    testsort.myprint()


    arr = [411, 329, 202, 104, 533,
           121, 311, 1, 4, 3,
           0, 12, 11, 53, 52,
           52, 252, 22, 1, 14]
    print('bucket: ')
    testsort = BucketSort(arr)
    testsort.myprint()
    testsort.sort(4)
    testsort.myprint()


    arr = [411, 329, 202, 104, 533,
           121, 311, 1, 4, 3,
           0, 12, 11, 53, 52,
           52, 252, 22, 1, 14]

    print('radix: ')
    testsort = RadixSort(arr)
    testsort.myprint()
    testsort.sort()
    testsort.myprint()
    '''


