import timeit
import random
import tracemalloc

# злиттям
def sort_merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return sort_merge_sort(sort_merge(left_half), sort_merge(right_half))

def sort_merge_sort(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# вставками 
def sort_insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Timsort
def sort_timsort_sort(lst):
    result = lst.sort()
    return result

def sort_timsort_sorted(lst):
    result = list(sorted(tuple(lst)))
    return result

def main():
    data = [
        [random.randint(0, 1_000) for _ in range(10)],
        [random.randint(0, 1_000) for _ in range(100)],
        [random.randint(0, 1_000) for _ in range(1_000)],
        [random.randint(0, 10_000) for _ in range(10_000)]
    ]

    sorting_functions = [
        sort_merge,
        sort_insertion,
        sort_timsort_sort,
        sort_timsort_sorted,
    ]

    for sort_func in sorting_functions:
        print(f"Sorting function: {sort_func.__name__}")
        data_set_count = 1
        for datum in data:
            print(f"Data set: {data_set_count}")
            tracemalloc.start()
            start_time = timeit.default_timer()
            sort_func(datum)
            execution_time = timeit.default_timer() - start_time
            print(f"Used memory: {tracemalloc.get_traced_memory()}")
            tracemalloc.stop()
            print(f"Execution time: {execution_time}")
            data_set_count +=1

if __name__ == "__main__":
    main()

