import random
import itertools

# find number in array, which is on k position
# in terms of ascending

def quickselect(lst, k, pivot_fn=random.choice):
    if len(lst) == 1:
        assert k == 0
        return lst[0]

    # define pivot point, here it is random choice
    pivot = pivot_fn(lst)

    lows = [el for el in lst if el < pivot]
    highs = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


def nlogn_median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return  lst[len(lst) // 2]
    else:
        return  0.5 * (lst[len(lst) // 2 - 1] + lst[len(lst) // 2])


def quickselect_median(lst, pivot_fn = random.choice):
    if len(lst) % 2 == 1:
        return quickselect(lst, len(lst) // 2, pivot_fn)
    else:
        return  0.5 * (quickselect(lst, len(lst) // 2 -1 , pivot_fn) +
                       quickselect(lst, len(lst) // 2, pivot_fn))


def chunked(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def pick_pivot(lst):
    assert len(lst) > 0
    if len(lst) < 5:
        return nlogn_median(lst)

    chunks = chunked(lst, 5)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]
    sorted_groups = [sorted(chunk) for chunk in full_chunks]
    medians = [chunk[2] for chunk in sorted_groups]
    median_of_medians = quickselect_median(medians, pick_pivot)
    return  median_of_medians


def main():
    lst = [-99, 1000, 42, 0 , 25, 44, 314, 14214, -141, 14, 55,433, 33, 232, 626, 267,-161]
    a = pick_pivot(lst)
    print(a)


if __name__ == "__main__":
    main()

