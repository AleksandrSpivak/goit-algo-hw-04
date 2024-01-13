import timeit
import random


def insertion_sort(lst):
    lst = lst[:]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    data_tiny = [random.randint(0, 100) for _ in range(100)]
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]

    time_tiny_merge = timeit.timeit(lambda: merge_sort(data_tiny[:]), number=10)
    time_tiny_insertion = timeit.timeit(lambda: insertion_sort(data_tiny[:]), number=10)
    time_tiny_timsort = timeit.timeit(lambda: sorted(data_tiny[:]), number=10)

    time_small_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time_small_insertion = timeit.timeit(
        lambda: insertion_sort(data_small[:]), number=10
    )
    time_small_timsort = timeit.timeit(lambda: sorted(data_small[:]), number=10)

    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time_medium_insertion = timeit.timeit(
        lambda: insertion_sort(data_medium[:]), number=10
    )
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium[:]), number=10)

    print(
        f"{'| Algorithm': <20} | {'Time tiny data': <20} | {'Time small data': <20} | {'Time medium data': <20}"
    )
    print(f":{'-'*19} | :{'-'*19} | :{'-'*19}| :{'-'*19}")

    print(
        f"{'| Merge sort': <20} | {time_tiny_merge:<20.5f} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}"
    )
    print(
        f"{'| Insertion sort': <20} | {time_tiny_insertion:<20.5f} | {time_small_insertion:<20.5f} | {time_medium_insertion:<20.5f}"
    )
    print(
        f"{'| Tim sort': <20} | {time_tiny_timsort:<20.5f} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}"
    )
