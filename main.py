import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація масивів для тестування
def generate_arrays(size):
    random_array = [random.randint(0, 10000) for _ in range(size)]
    sorted_array = sorted(random_array)
    almost_sorted_array = sorted_array[:]
    if size > 1:
        almost_sorted_array[size // 2], almost_sorted_array[size // 2 + 1] = almost_sorted_array[size // 2 + 1], almost_sorted_array[size // 2]
    return random_array, sorted_array, almost_sorted_array

# Вимірювання часу виконання
def measure_time(sort_function, arr):
    start_time = timeit.default_timer()
    sort_function(arr)
    return timeit.default_timer() - start_time

def main():
    sizes = [100, 1000, 10000]
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Timsort (Python's sorted)": sorted
    }

    for size in sizes:
        print(f"\nArray size: {size}")
        random_array, sorted_array, almost_sorted_array = generate_arrays(size)

        for name, sort_function in algorithms.items():
            print(f"\n{name}:")
            for arr_type, arr in [("Random array", random_array[:]), ("Sorted array", sorted_array[:]), ("Almost sorted array", almost_sorted_array[:])]:
                time_taken = measure_time(sort_function, arr)
                print(f"{arr_type}: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
