import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
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

number1 = [55, 3132, 801, 4, 255]
number2 = [55, 3132, 801, 4, 255, 16789, 91, 333, 4587, 930]
number3 = [55, 3132, 801, 4, 255, 16789, 91, 333, 4587, 930, 555, 66, 1245, 5482, 43739]
number4 = [x for x in range(100)]
number4 = number4[::-1]
number5 = [x for x in range(300)]
number5 = number5[::-1]

print(f"  5 elements sorted by merge_sort in     {timeit.timeit('[merge_sort(number1)]', globals=globals())} sec")
print(f" 10 elements sorted by merge_sort in     {timeit.timeit('[merge_sort(number2)]', globals=globals())} sec")
print(f" 15 elements sorted by merge_sort in     {timeit.timeit('[merge_sort(number3)]', globals=globals())} sec")

print(f"  5 elements sorted by sorted in         {timeit.timeit('[sorted(number1)]', globals=globals())} sec")
print(f" 10 elements sorted by sorted in         {timeit.timeit('[sorted(number2)]', globals=globals())} sec")
print(f" 15 elements sorted by sorted in         {timeit.timeit('[sorted(number3)]', globals=globals())} sec")
print(f"100 elements sorted by sorted in         {timeit.timeit('[sorted(number4)]', globals=globals())} sec")
print(f"300 elements sorted by sorted in         {timeit.timeit('[sorted(number5)]', globals=globals())} sec")

print(f"  5 elements sorted by insertion_sort in {timeit.timeit('[insertion_sort(number1)]', globals=globals())} sec")
print(f" 10 elements sorted by insertion_sort in {timeit.timeit('[insertion_sort(number2)]', globals=globals())} sec")
print(f" 15 elements sorted by insertion_sort in {timeit.timeit('[insertion_sort(number3)]', globals=globals())} sec")
print(f"100 elements sorted by insertion_sort in {timeit.timeit('[insertion_sort(number4)]', globals=globals())} sec")
print(f"300 elements sorted by insertion_sort in {timeit.timeit('[insertion_sort(number5)]', globals=globals())} sec")
