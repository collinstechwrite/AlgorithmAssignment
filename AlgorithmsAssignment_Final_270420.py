"""This application should include implementations of the five sorting algorithms, along with a main method which tests each of them.
Note that it is fine to reuse or adapt code for sorting algorithms from books, online resources or the lecture notes, as long as you add
your own comments to the code and acknowledge the source. 
 
To benchmark the algorithms, you should use arrays of randomly generated integers with different input sizes n.
You should use a variety of different input sizes, e.g. n=10,n=100,n=500,…,n=10,000 etc.
to test the effect of the input size on the running time of each algorithm.
See the console output below for a selection of suggested sizes of n.
You may test values of n which are higher than 10,000 if you wish, e.g. 500,000.
Just be aware that algorithms such as Bubble Sort may take a long time to run when using large values of n! 
 
The running time (in milliseconds) for each algorithm should be measured 10 times, and the average of the 10 runs for each algorithm
and each input size n should be output to the console when the program finishes executing. See sample console output below
(note that the output is formatted to 3 decimal places and laid out neatly): """

import os
import psutil

import statistics
import time
from random import randint


#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

bubble1000 = []
bubble2500 = []
bubble5000 = []
bubble7500 = []
bubble10000 = []
bubble12500 = []
bubble15000 = []
bubble20000 = []
bubble25000 = []
bubble50000 = []

quick1000 = []
quick2500 = []
quick5000 = []
quick7500 = []
quick10000 = []
quick12500 = []
quick15000 = []
quick20000 = []
quick25000 = []
quick50000 = []

radix1000 = []
radix2500 = []
radix5000 = []
radix7500 = []
radix10000 = []
radix12500 = []
radix15000 = []
radix20000 = []
radix25000 = []
radix50000 = []

merge1000 = []
merge2500 = []
merge5000 = []
merge7500 = []
merge10000 = []
merge12500 = []
merge15000 = []
merge20000 = []
merge25000 = []
merge50000 = []

timsort1000 = []
timsort2500 = []
timsort5000 = []
timsort7500 = []
timsort10000 = []
timsort12500 = []
timsort15000 = []
timsort20000 = []
timsort25000 = []
timsort50000 = []

python1000 = []
python2500 = []
python5000 = []
python7500 = []
python10000 = []
python12500 = []
python15000 = []
python20000 = []
python25000 = []
python50000 = []

bubble1000memory = []
bubble2500memory = []
bubble5000memory = []
bubble7500memory = []
bubble10000memory = []
bubble12500memory = []
bubble15000memory = []
bubble20000memory = []
bubble25000memory = []
bubble50000memory = []

quick1000memory = []
quick2500memory = []
quick5000memory = []
quick7500memory = []
quick10000memory = []
quick12500memory = []
quick15000memory = []
quick20000memory = []
quick25000memory = []
quick50000memory = []

radix1000memory = []
radix2500memory = []
radix5000memory = []
radix7500memory = []
radix10000memory = []
radix12500memory = []
radix15000memory = []
radix20000memory = []
radix25000memory = []
radix50000memory = []

merge1000memory = []
merge2500memory = []
merge5000memory = []
merge7500memory = []
merge10000memory = []
merge12500memory = []
merge15000memory = []
merge20000memory = []
merge25000memory = []
merge50000memory = []

timsort1000memory = []
timsort2500memory = []
timsort5000memory = []
timsort7500memory = []
timsort10000memory = []
timsort12500memory = []
timsort15000memory = []
timsort20000memory = []
timsort25000memory = []
timsort50000memory = []

python1000memory = []
python2500memory = []
python5000memory = []
python7500memory = []
python10000memory = []
python12500memory = []
python15000memory = []
python20000memory = []
python25000memory = []
python50000memory = []



def random_array(n):
    array= []
    for i in range (0,n,1):
        array.append(randint(0,n))
    return array




def main_testing_algorithm(array_to_sort):
    """ -------- Bubble Algorithm -------- """
    

    """https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python"""
    def bubble_sort(array):
        n = len(array)

        for i in range(n):
            # Create a flag that will allow the function to
            # terminate early if there's nothing left to sort
            already_sorted = True

            # Start looking at each item of the list one by one,
            # comparing it with its adjacent value. With each
            # iteration, the portion of the array that you look at
            # shrinks because the remaining items have already been
            # sorted.
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    # If the item you're looking at is greater than its
                    # adjacent value, then swap them
                    array[j], array[j + 1] = array[j + 1], array[j]

                    # Since you had to swap two elements,
                    # set the `already_sorted` flag to `False` so the
                    # algorithm doesn't finish prematurely
                    already_sorted = False

            # If there were no swaps during the last iteration,
            # the array is already sorted, and you can terminate
            if already_sorted:
                break

        return array



    # Verify it works
    random_list_of_nums = array_to_sort

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    bubble_sort(random_list_of_nums) #call the bubble sort formula


    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)

    if testsize == 1000:
        bubble1000memory.append(float(process.memory_percent()))
        bubble1000.append(time_elapsed)
        

    elif testsize == 2500:
        bubble2500memory.append(float(process.memory_percent()))
        bubble2500.append(time_elapsed)

    elif testsize == 5000:
        bubble5000memory.append(float(process.memory_percent()))
        bubble5000.append(time_elapsed)

    elif testsize == 7500:
        bubble7500memory.append(float(process.memory_percent()))
        bubble7500.append(time_elapsed)
        
    elif testsize == 10000:
        bubble10000memory.append(float(process.memory_percent()))
        bubble10000.append(time_elapsed)
        
    elif testsize == 12500:
        bubble12500memory.append(float(process.memory_percent()))
        bubble12500.append(time_elapsed)

    elif testsize == 15000:
        bubble15000memory.append(float(process.memory_percent()))
        bubble15000.append(time_elapsed)

    elif testsize == 20000:
        bubble20000memory.append(float(process.memory_percent()))
        bubble20000.append(time_elapsed)
        
    elif testsize == 25000:
        bubble25000memory.append(float(process.memory_percent()))
        bubble25000.append(time_elapsed)
        
    elif testsize == 50000:
        bubble50000memory.append(float(process.memory_percent()))
        bubble50000.append(time_elapsed)

    """-------- Quick Sort"""


    """https://realpython.com/sorting-algorithms-python/#the-quicksort-algorithm-in-python"""

    def quicksort(array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        low, same, high = [], [], []

        # Select your `pivot` element randomly
        pivot = array[randint(0, len(array) - 1)]

        for item in array:
            # Elements that are smaller than the `pivot` go to
            # the `low` list. Elements that are larger than
            # `pivot` go to the `high` list. Elements that are
            # equal to `pivot` go to the `same` list.
            if item < pivot:
                low.append(item)
            elif item == pivot:
                same.append(item)
            elif item > pivot:
                high.append(item)

        # The final result combines the sorted `low` list
        # with the `same` list and the sorted `high` list
        return quicksort(low) + same + quicksort(high)


    # Verify it works
    random_list_of_nums = array_to_sort


    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    quicksort(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == 1000:
        quick1000memory.append(float(process.memory_percent()))
        quick1000.append(time_elapsed)
        

    elif testsize == 2500:
        quick2500memory.append(float(process.memory_percent()))
        quick2500.append(time_elapsed)

    elif testsize == 5000:
        quick5000memory.append(float(process.memory_percent()))
        quick5000.append(time_elapsed)

    elif testsize == 7500:
        quick7500memory.append(float(process.memory_percent()))
        quick7500.append(time_elapsed)
        
    elif testsize == 10000:
        quick10000memory.append(float(process.memory_percent()))
        quick10000.append(time_elapsed)
        
    elif testsize == 12500:
        quick12500memory.append(float(process.memory_percent()))
        quick12500.append(time_elapsed)

    elif testsize == 15000:
        quick15000memory.append(float(process.memory_percent()))
        quick15000.append(time_elapsed)

    elif testsize == 20000:
        quick20000memory.append(float(process.memory_percent()))
        quick20000.append(time_elapsed)
        
    elif testsize == 25000:
        quick25000memory.append(float(process.memory_percent()))
        quick25000.append(time_elapsed)
        
    elif testsize == 50000:
        quick50000memory.append(float(process.memory_percent()))
        quick50000.append(time_elapsed)




    """ -------------------- Radix Sort Algorithm """
    """https://www.programiz.com/dsa/radix-sort"""




    def countingSort(array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]


    def radixSort(array):
        max_element = max(array)
        place = 1
        while max_element // place > 0:
            countingSort(array, place)
            place *= 10


    data = array_to_sort
    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    radixSort(data)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)

    if testsize == 1000:
        radix1000memory.append(float(process.memory_percent()))
        radix1000.append(time_elapsed)
        

    elif testsize == 2500:
        radix2500memory.append(float(process.memory_percent()))
        radix2500.append(time_elapsed)

    elif testsize == 5000:
        radix5000memory.append(float(process.memory_percent()))
        radix5000.append(time_elapsed)

    elif testsize == 7500:
        radix7500memory.append(float(process.memory_percent()))
        radix7500.append(time_elapsed)
        
    elif testsize == 10000:
        radix10000memory.append(float(process.memory_percent()))
        radix10000.append(time_elapsed)
        
    elif testsize == 12500:
        radix12500memory.append(float(process.memory_percent()))
        radix12500.append(time_elapsed)

    elif testsize == 15000:
        radix15000memory.append(float(process.memory_percent()))
        radix15000.append(time_elapsed)

    elif testsize == 20000:
        radix20000memory.append(float(process.memory_percent()))
        radix20000.append(time_elapsed)
        
    elif testsize == 25000:
        radix25000memory.append(float(process.memory_percent()))
        radix25000.append(time_elapsed)
        
    elif testsize == 50000:
        radix50000memory.append(float(process.memory_percent()))
        radix50000.append(time_elapsed)


    """ -------------------- Merge Sort Algorithm """
    """https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python"""


    def merge(left, right):
        # If the first array is empty, then nothing needs
        # to be merged, and you can return the second array as the result
        if len(left) == 0:
            return right

        # If the second array is empty, then nothing needs
        # to be merged, and you can return the first array as the result
        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0

        # Now go through both arrays until all the elements
        # make it into the resultant array
        while len(result) < len(left) + len(right):
            # The elements need to be sorted to add them to the
            # resultant array, so you need to decide whether to get
            # the next element from the first or the second array
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            # If you reach the end of either array, then you can
            # add the remaining elements from the other array to
            # the result and break the loop
            if index_right == len(right):
                result += left[index_left:]
                break

            if index_left == len(left):
                result += right[index_right:]
                break

        return result


    def merge_sort(array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        midpoint = len(array) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return merge(
            left=merge_sort(array[:midpoint]),
            right=merge_sort(array[midpoint:]))


    # Verify it works
    random_list_of_nums = array_to_sort

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    random_list_of_nums = merge_sort(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == 1000:
        merge1000memory.append(float(process.memory_percent()))
        merge1000.append(time_elapsed)
        

    elif testsize == 2500:
        merge2500memory.append(float(process.memory_percent()))
        merge2500.append(time_elapsed)

    elif testsize == 5000:
        merge5000memory.append(float(process.memory_percent()))
        merge5000.append(time_elapsed)

    elif testsize == 7500:
        merge7500memory.append(float(process.memory_percent()))
        merge7500.append(time_elapsed)
        
    elif testsize == 10000:
        merge10000memory.append(float(process.memory_percent()))
        merge10000.append(time_elapsed)
        
    elif testsize == 12500:
        merge12500memory.append(float(process.memory_percent()))
        merge12500.append(time_elapsed)

    elif testsize == 15000:
        merge15000memory.append(float(process.memory_percent()))
        merge15000.append(time_elapsed)

    elif testsize == 20000:
        merge20000memory.append(float(process.memory_percent()))
        merge20000.append(time_elapsed)
        
    elif testsize == 25000:
        merge25000memory.append(float(process.memory_percent()))
        merge25000.append(time_elapsed)
        
    elif testsize == 50000:
        merge50000memory.append(float(process.memory_percent()))
        merge50000.append(time_elapsed)


    """ -------------------- Tim Sort"""
    """https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python"""

    def insertion_sort(array, left=0, right=None):
        if right is None:
            right = len(array) - 1

        # Loop from the element indicated by
        # `left` until the element indicated by `right`
        for i in range(left + 1, right + 1):
            # This is the element we want to position in its
            # correct place
            key_item = array[i]

            # Initialize the variable that will be used to
            # find the correct position of the element referenced
            # by `key_item`
            j = i - 1

            # Run through the list of items (the left
            # portion of the array) and find the correct position
            # of the element referenced by `key_item`. Do this only
            # if the `key_item` is smaller than its adjacent values.
            while j >= left and array[j] > key_item:
                # Shift the value one position to the left
                # and reposition `j` to point to the next element
                # (from right to left)
                array[j + 1] = array[j]
                j -= 1

            # When you finish shifting the elements, position
            # the `key_item` in its correct location
            array[j + 1] = key_item

        return array

    def timsort(array):
        min_run = 32
        n = len(array)

        # Start by slicing and sorting small portions of the
        # input array. The size of these slices is defined by
        # your `min_run` size.
        for i in range(0, n, min_run):
            insertion_sort(array, i, min((i + min_run - 1), n - 1))

        # Now you can start merging the sorted slices.
        # Start from `min_run`, doubling the size on
        # each iteration until you surpass the length of
        # the array.
        size = min_run
        while size < n:
            # Determine the arrays that will
            # be merged together
            for start in range(0, n, size * 2):
                # Compute the `midpoint` (where the first array ends
                # and the second starts) and the `endpoint` (where
                # the second array ends)
                midpoint = start + size - 1
                end = min((start + size * 2 - 1), (n-1))

                # Merge the two subarrays.
                # The `left` array should go from `start` to
                # `midpoint + 1`, while the `right` array should
                # go from `midpoint + 1` to `end + 1`.
                merged_array = merge(
                    left=array[start:midpoint + 1],
                    right=array[midpoint + 1:end + 1])

                # Finally, put the merged array back into
                # your array
                array[start:start + len(merged_array)] = merged_array

            # Each iteration should double the size of your arrays
            size *= 2

        return array



    # Verify it works
    random_list_of_nums = array_to_sort

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    random_list_of_nums = timsort(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == 1000:
        timsort1000memory.append(float(process.memory_percent()))
        timsort1000.append(time_elapsed)
        

    elif testsize == 2500:
        timsort2500memory.append(float(process.memory_percent()))
        timsort2500.append(time_elapsed)

    elif testsize == 5000:
        timsort5000memory.append(float(process.memory_percent()))
        timsort5000.append(time_elapsed)

    elif testsize == 7500:
        timsort7500memory.append(float(process.memory_percent()))
        timsort7500.append(time_elapsed)
        
    elif testsize == 10000:
        timsort10000memory.append(float(process.memory_percent()))
        timsort10000.append(time_elapsed)
        
    elif testsize == 12500:
        timsort12500memory.append(float(process.memory_percent()))
        timsort12500.append(time_elapsed)

    elif testsize == 15000:
        timsort15000memory.append(float(process.memory_percent()))
        timsort15000.append(time_elapsed)

    elif testsize == 20000:
        timsort20000memory.append(float(process.memory_percent()))
        timsort20000.append(time_elapsed)
        
    elif testsize == 25000:
        timsort25000memory.append(float(process.memory_percent()))
        timsort25000.append(time_elapsed)
        
    elif testsize == 50000:
        timsort50000memory.append(float(process.memory_percent()))
        timsort50000.append(time_elapsed)






    """ -------------------- Python Inbuilt Function"""


    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    python_inbuilt_sorted = sorted(array_to_sort)
    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == 1000:
        python1000memory.append(float(process.memory_percent()))
        python1000.append(time_elapsed)
        

    elif testsize == 2500:
        python2500memory.append(float(process.memory_percent()))
        python2500.append(time_elapsed)

    elif testsize == 5000:
        python5000memory.append(float(process.memory_percent()))
        python5000.append(time_elapsed)

    elif testsize == 7500:
        python7500memory.append(float(process.memory_percent()))
        python7500.append(time_elapsed)
        
    elif testsize == 10000:
        python10000memory.append(float(process.memory_percent()))
        python10000.append(time_elapsed)
        
    elif testsize == 12500:
        python12500memory.append(float(process.memory_percent()))
        python12500.append(time_elapsed)

    elif testsize == 15000:
        python15000memory.append(float(process.memory_percent()))
        python15000.append(time_elapsed)

    elif testsize == 20000:
        python20000memory.append(float(process.memory_percent()))
        python20000.append(time_elapsed)
        
    elif testsize == 25000:
        python25000memory.append(float(process.memory_percent()))
        python25000.append(time_elapsed)
        
    elif testsize == 50000:
        python50000memory.append(float(process.memory_percent()))
        python50000.append(time_elapsed)






testsizes = [1000,2500,5000,7500,10000,12500,15000,20000,25000,50000]

How_Many_Tests = int(input("How many tests do you want to run?"))



for test in testsizes:
    testsize  = test
    count = 0
    while count < How_Many_Tests:
        count += 1
        array_to_sort = random_array(test)
        main_testing_algorithm(array_to_sort)
        print("TEST " + str(count) + " OF TEST SIZE " + str(test))
        
        
    count = 0

print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", "1000","2500","5000","7500","10000","12500","15000","20000","25000","50000"))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", statistics.mean(bubble1000),statistics.mean(bubble2500),statistics.mean(bubble5000),statistics.mean(bubble7500),statistics.mean(bubble10000),statistics.mean(bubble12500),statistics.mean(bubble15000),statistics.mean(bubble20000),statistics.mean(bubble25000),statistics.mean(bubble50000)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", statistics.mean(quick1000),statistics.mean(quick2500),statistics.mean(quick5000),statistics.mean(quick7500),statistics.mean(quick10000),statistics.mean(quick12500),statistics.mean(quick15000),statistics.mean(quick20000),statistics.mean(quick25000),statistics.mean(quick50000)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", statistics.mean(radix1000),statistics.mean(radix2500),statistics.mean(radix5000),statistics.mean(radix7500),statistics.mean(radix10000),statistics.mean(radix12500),statistics.mean(radix15000),statistics.mean(radix20000),statistics.mean(radix25000),statistics.mean(radix50000)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", statistics.mean(merge1000),statistics.mean(merge2500),statistics.mean(merge5000),statistics.mean(merge7500),statistics.mean(merge10000),statistics.mean(merge12500),statistics.mean(merge15000),statistics.mean(merge20000),statistics.mean(merge25000),statistics.mean(merge50000)))                                                                       
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", statistics.mean(timsort1000),statistics.mean(timsort2500),statistics.mean(timsort5000),statistics.mean(timsort7500),statistics.mean(timsort10000),statistics.mean(timsort12500),statistics.mean(timsort15000),statistics.mean(timsort20000),statistics.mean(timsort25000),statistics.mean(timsort50000)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", statistics.mean(python1000),statistics.mean(python2500),statistics.mean(python5000),statistics.mean(python7500),statistics.mean(python10000),statistics.mean(python12500),statistics.mean(python15000),statistics.mean(python20000),statistics.mean(python25000),statistics.mean(python50000)))



print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", "1000 memory","2500 memory","5000 memory","7500 memory","10000 memory","12500 memory","15000 memory","20000 memory","25000 memory","50000 memory"))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", statistics.mean(bubble1000memory),statistics.mean(bubble2500memory),statistics.mean(bubble5000memory),statistics.mean(bubble7500memory),statistics.mean(bubble10000memory),statistics.mean(bubble12500memory),statistics.mean(bubble15000memory),statistics.mean(bubble20000memory),statistics.mean(bubble25000memory),statistics.mean(bubble50000memory)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", statistics.mean(quick1000memory),statistics.mean(quick2500memory),statistics.mean(quick5000memory),statistics.mean(quick7500memory),statistics.mean(quick10000memory),statistics.mean(quick12500memory),statistics.mean(quick15000memory),statistics.mean(quick20000memory),statistics.mean(quick25000memory),statistics.mean(quick50000memory)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", statistics.mean(radix1000memory),statistics.mean(radix2500memory),statistics.mean(radix5000memory),statistics.mean(radix7500memory),statistics.mean(radix10000memory),statistics.mean(radix12500memory),statistics.mean(radix15000memory),statistics.mean(radix20000memory),statistics.mean(radix25000memory),statistics.mean(radix50000memory)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", statistics.mean(merge1000memory),statistics.mean(merge2500memory),statistics.mean(merge5000memory),statistics.mean(merge7500memory),statistics.mean(merge10000memory),statistics.mean(merge12500memory),statistics.mean(merge15000memory),statistics.mean(merge20000memory),statistics.mean(merge25000memory),statistics.mean(merge50000memory)))                                                                       
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", statistics.mean(timsort1000memory),statistics.mean(timsort2500memory),statistics.mean(timsort5000memory),statistics.mean(timsort7500memory),statistics.mean(timsort10000memory),statistics.mean(timsort12500memory),statistics.mean(timsort15000memory),statistics.mean(timsort20000memory),statistics.mean(timsort25000memory),statistics.mean(timsort50000memory)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", statistics.mean(python1000memory),statistics.mean(python2500memory),statistics.mean(python5000memory),statistics.mean(python7500memory),statistics.mean(python10000memory),statistics.mean(python12500memory),statistics.mean(python15000memory),statistics.mean(python20000memory),statistics.mean(python25000memory),statistics.mean(python50000memory)))


plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(bubble1000),statistics.mean(bubble2500),statistics.mean(bubble5000),statistics.mean(bubble7500),statistics.mean(bubble10000),statistics.mean(bubble12500),statistics.mean(bubble15000),statistics.mean(bubble20000),statistics.mean(bubble25000),statistics.mean(bubble50000)],label='Bubble Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(quick1000),statistics.mean(quick2500),statistics.mean(quick5000),statistics.mean(quick7500),statistics.mean(quick10000),statistics.mean(quick12500),statistics.mean(quick15000),statistics.mean(quick20000),statistics.mean(quick25000),statistics.mean(quick50000)],label='Quick Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(radix1000),statistics.mean(radix2500),statistics.mean(radix5000),statistics.mean(radix7500),statistics.mean(radix10000),statistics.mean(radix12500),statistics.mean(radix15000),statistics.mean(radix20000),statistics.mean(radix25000),statistics.mean(radix50000)],label='Radix Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(merge1000),statistics.mean(merge2500),statistics.mean(merge5000),statistics.mean(merge7500),statistics.mean(merge10000),statistics.mean(merge12500),statistics.mean(merge15000),statistics.mean(merge20000),statistics.mean(merge25000),statistics.mean(merge50000)],label='Merge Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(timsort1000),statistics.mean(timsort2500),statistics.mean(timsort5000),statistics.mean(timsort7500),statistics.mean(timsort10000),statistics.mean(timsort12500),statistics.mean(timsort15000),statistics.mean(timsort20000),statistics.mean(timsort25000),statistics.mean(timsort50000)],label='timsort Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(python1000),statistics.mean(python2500),statistics.mean(python5000),statistics.mean(python7500),statistics.mean(python10000),statistics.mean(python12500),statistics.mean(python15000),statistics.mean(python20000),statistics.mean(python25000),statistics.mean(python50000)],label='Python Inbuilt-Sort')
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")
plt.show()



plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(bubble1000memory),statistics.mean(bubble2500memory),statistics.mean(bubble5000memory),statistics.mean(bubble7500memory),statistics.mean(bubble10000memory),statistics.mean(bubble12500memory),statistics.mean(bubble15000memory),statistics.mean(bubble20000memory),statistics.mean(bubble25000memory),statistics.mean(bubble50000memory)],label='Bubble Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(quick1000memory),statistics.mean(quick2500memory),statistics.mean(quick5000memory),statistics.mean(quick7500memory),statistics.mean(quick10000memory),statistics.mean(quick12500memory),statistics.mean(quick15000memory),statistics.mean(quick20000memory),statistics.mean(quick25000memory),statistics.mean(quick50000memory)],label='Quick Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(radix1000memory),statistics.mean(radix2500memory),statistics.mean(radix5000memory),statistics.mean(radix7500memory),statistics.mean(radix10000memory),statistics.mean(radix12500memory),statistics.mean(radix15000memory),statistics.mean(radix20000memory),statistics.mean(radix25000memory),statistics.mean(radix50000memory)],label='Radix Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(merge1000memory),statistics.mean(merge2500memory),statistics.mean(merge5000memory),statistics.mean(merge7500memory),statistics.mean(merge10000memory),statistics.mean(merge12500memory),statistics.mean(merge15000memory),statistics.mean(merge20000memory),statistics.mean(merge25000memory),statistics.mean(merge50000memory)],label='Merge Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(timsort1000memory),statistics.mean(timsort2500memory),statistics.mean(timsort5000memory),statistics.mean(timsort7500memory),statistics.mean(timsort10000memory),statistics.mean(timsort12500memory),statistics.mean(timsort15000memory),statistics.mean(timsort20000memory),statistics.mean(timsort25000memory),statistics.mean(timsort50000memory)],label='timsort Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(python1000memory),statistics.mean(python2500memory),statistics.mean(python5000memory),statistics.mean(python7500memory),statistics.mean(python10000memory),statistics.mean(python12500memory),statistics.mean(python15000memory),statistics.mean(python20000memory),statistics.mean(python25000memory),statistics.mean(python50000memory)],label='Python Inbuilt-Sort')
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Memory Use %")
plt.show()



