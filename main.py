from sorting.quicksort import QuickSort


def main():
    testsort = QuickSort(arr)
    arr = [1000, 42, 0, -99, 31, 17, 5, -2]
   
    testsort.myprint()
    testsort.sort(0, len(arr)-1)
    testsort.myprint()


if __name__ == "__main__":
    main()
