import math

def get_input_list(file_name):
    with open(file_name) as file:
        return [int(i) for i in file.readline().strip().split()]


def insertion_sort(arr, n, start, increment):
    count = 0
    for i in range(start + increment, n, increment):
        this_element = arr[i]
        index = i - increment

        while index >= start:
            count += 1
            if arr[index] > this_element:
                arr[index + increment] = arr[index]
                index -= increment
            else:
                break

        arr[index + increment] = this_element
    return count


def shell_sort_log2(arr):
    count = 0
    n = len(arr)
    s = max(math.floor(math.log2(n)) - 1, 0)
    increment = int(2 ** (s + 1) - 1)

    while s >= 0:
        for start in range(0, increment):
            count += insertion_sort(arr, n, start, increment)
        s -= 1
        increment = int((increment - 1) / 2)
    return count


def shell_sort_log3(arr):
    count = 0
    n = len(arr)
    s = max(math.floor(math.log(2 * n + 1, 3)) - 2, 0)
    increment = int((3 ** (s + 1) - 1) * 0.5)

    while s >= 0:
        for start in range(0, increment):
            count += insertion_sort(arr, n, start, increment)
        s -= 1
        increment = int((increment - 1) / 3)
    return count


input = "input.txt"
output = "output.txt"

arr = get_input_list(input)
count_log2 = shell_sort_log2(arr)

arr = get_input_list(input)
count_log3 = shell_sort_log3(arr)

with open(output, 'w') as output_file:
    print(*arr, file=output_file)
    print(count_log2, count_log3, file=output_file)
