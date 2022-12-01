import matplotlib.pyplot as plt
import numpy as np
import random
import time

amount = 10
random.seed("ABC")
x = np.arange(0, amount, 1)
count = 0

# Bubble sorting
def bubble_sort():
    """Basic bubble sort which will also show graph of values"""
    count = 0
    lst = np.random.randint(0, 100, amount)

    ptime = time.perf_counter()
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            plt.subplot(2,1,1)
            plt.bar(list(range(amount)), lst)
            plt.subplot(2,1,2)
            plt.plot(lst)
            plt.pause(0.000001)
            plt.clf()
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            count += 1
    
    ptime2 = time.perf_counter()

    plt.subplot(2,1,1)
    plt.bar(list(range(amount)), lst)
    plt.subplot(2,1,2)
    plt.plot(lst)
    plt.pause(0.000001)
    plt.clf()

    return ptime2 - ptime - (count * 0.001)

# Merge Sort
def merge_sort(numbers_list, left, right):
    """Merge sort which will also show graph of values"""
    
    if left >= right:
        return

    mid = (left + right) // 2

    plt.subplot(2,1,1)
    plt.bar(list(range(amount)), numbers_list)
    plt.subplot(2,1,2)
    plt.plot(numbers_list)
    plt.pause(0.000001)
    plt.clf()

    merge_sort(numbers_list, left, mid)
    merge_sort(numbers_list, mid + 1, right)

    merge(numbers_list, left, right, mid)


def merge(numbers_list, left, right, mid):
    """Second portion of merge sort recursion"""

    left_cpy = numbers_list[left:mid + 1]
    right_cpy = numbers_list[mid + 1:right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    # While both sides have values
    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            numbers_list[sorted_counter] = left_cpy[l_counter]
            l_counter += 1
        else:
            numbers_list[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    # Finish left side
    while l_counter < len(left_cpy):
        numbers_list[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1

    # Finish right side
    while r_counter < len(right_cpy):
        numbers_list[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1

def merge_sort_graph():
    """Sets up merge sort and timings"""
    numbers = [random.randint(0, 1000) for _ in range(amount)]
    ptime = time.perf_counter()
    merge_sort(numbers, 0, len(numbers) - 1)
    ptime2 = time.perf_counter()
    
    plt.subplot(2,1,1)
    plt.bar(x, numbers)
    plt.subplot(2,1,2)
    plt.plot(numbers)
    plt.pause(0.000001)
    plt.clf()

    return ptime2 - ptime

# Selection Sort High values first
def high_selection_sort():
    """Selection sort that puts the highest numbers at the top"""
    list = [random.randint(0, 1000) for _ in range(amount)]
    count = 0

    size = len(list)

    ptime = time.perf_counter()
    if size > 0:
        for iPivot in range(size - 1, -1, -1):
            index = iPivot
            biggest = list[iPivot]
            for jPivot in range(0, iPivot):
                if list[jPivot] > biggest:
                    biggest = list[jPivot]
                    index = jPivot

                plt.subplot(2,1,1)
                plt.bar(x, list)
                plt.subplot(2,1,2)
                plt.plot(list)
                plt.pause(0.000001)
                plt.clf()
            
            count += 1
            
            list[index] = list[iPivot]
            list[iPivot] = biggest
        
    else:
        print('The list is empty')

    ptime2 = time.perf_counter()

    plt.subplot(2,1,1)
    plt.bar(x, list)
    plt.subplot(2,1,2)
    plt.plot(list)
    plt.pause(0.000001)
    plt.clf()

    return ptime2 - ptime - (count * 0.001)


# Segregation Sort
def sort():
    '''Array, beginning, and end sent for recursion'''
    array = [random.randint(0, 1000) for _ in range(amount)]
    ptime = time.perf_counter()
    sort_recursive(array, 0, len(array) - 1)
    previous = 0
    for num in array:
        if previous > num:
            sort_recursive(array, 0, len(array) - 1)
        previous = num
    ptime2 = time.perf_counter()

    return ptime2 - ptime
    
def sort_recursive(array, i_begin, i_end):
    '''Function to perform recursion on list to sort array'''
    if i_end - i_begin <= 1 or i_end < 0:
        return
    
    i_pivot = segregate(array, i_begin, i_end)

    plt.subplot(2,1,1)
    plt.bar(list(range(amount)), array)
    plt.subplot(2,1,2)
    plt.plot(array)
    plt.pause(0.000001)
    plt.clf()
    
    sort_recursive(array, i_begin, i_pivot - 1)
    sort_recursive(array, i_pivot + 1, i_end)
    
def segregate(array, i_begin, i_end):
    '''Sorts the array by segregation method'''
    if i_begin == i_end:
        return i_begin
    
    i_pivot = (i_begin + i_end) // 2
    i_up = i_begin
    i_down = i_end
    
    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
            plt.subplot(2,1,1)
            plt.bar(list(range(amount)), array)
            plt.subplot(2,1,2)
            plt.plot(array)
            plt.pause(0.000001)
            plt.clf()


        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
            plt.subplot(2,1,1)
            plt.bar(list(range(amount)), array)
            plt.subplot(2,1,2)
            plt.plot(array)
            plt.pause(0.000001)
            plt.clf()
        
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_down] = array[i_down], array[i_up]

        plt.subplot(2,1,1)
        plt.bar(list(range(amount)), array)
        plt.subplot(2,1,2)
        plt.plot(array)
        plt.pause(0.000001)
        plt.clf()
    
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up

def main():
    """Runs each sort that will graph and tell timing"""
    sort_times = 2

    perf_time = 0
    best_perf_time = 0
    for i in range(sort_times):
        if perf_time < best_perf_time or best_perf_time < 0.001:
            best_perf_time = perf_time
        perf_time += bubble_sort()
    print(f"Average Bubble Sort Time: {perf_time/sort_times:0.4f} seconds")
    print(f"Best Bubble Sort Time: {best_perf_time:0.4f} seconds")

    perf_time = 0
    best_perf_time = 0
    for i in range(sort_times):
        if perf_time < best_perf_time or best_perf_time < 0.001:
            best_perf_time = perf_time
        perf_time += merge_sort_graph()
    print(f"Average Merge Sort Time: {perf_time/sort_times:0.4f} seconds")
    print(f"Best Merge Sort Time: {best_perf_time:0.4f} seconds")

    perf_time = 0
    best_perf_time = 0
    for i in range(sort_times):
        if perf_time < best_perf_time or best_perf_time < 0.001:
            best_perf_time = perf_time
        perf_time += high_selection_sort()
    print(f"Average Selection Sort Time: {perf_time/sort_times:0.4f} seconds")
    print(f"Best Selection Sort Time: {best_perf_time:0.4f} seconds")

    # perf_time = 0
    # best_perf_time = 0
    # for i in range(sort_times):
    #     if perf_time < best_perf_time or best_perf_time < 0.001:
    #         best_perf_time = perf_time
    #     perf_time += sort()
    # print(f"Average Segregation Sort Time: {perf_time/sort_times:0.4f} seconds")
    # print(f"Best Segregation Sort Time: {best_perf_time:0.4f} seconds")
    

if __name__ == "__main__":
    main()