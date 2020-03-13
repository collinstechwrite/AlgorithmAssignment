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

chris1000 = []
chris2500 = []
chris5000 = []
chris7500 = []
chris10000 = []
chris12500 = []
chris15000 = []
chris20000 = []
chris25000 = []
chris50000 = []

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

chris1000memory = []
chris2500memory = []
chris5000memory = []
chris7500memory = []
chris10000memory = []
chris12500memory = []
chris15000memory = []
chris20000memory = []
chris25000memory = []
chris50000memory = []

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
    



    def bubble_sort(nums):
        # We set swapped to True so the loop looks runs at least once
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    # Swap the elements
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    # Set the flag to True so we'll loop again
                    swapped = True


    # Verify it works
    random_list_of_nums = array_to_sort

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    bubble_sort(random_list_of_nums)


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





    # There are different ways to do a Quick Sort partition, this implements the
    # Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
    def partition(nums, low, high):
        # We select the middle element to be the pivot. Some implementations select
        # the first element or the last element. Sometimes the median value becomes
        # the pivot, or a random one. There are many more strategies that can be
        # chosen or created.
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums[i] < pivot:
                i += 1

            j -= 1
            while nums[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # If an element at i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot), then swap them
            nums[i], nums[j] = nums[j], nums[i]


    def quick_sort(nums):
        # Create a helper function that will be called recursively
        def _quick_sort(items, low, high):
            if low < high:
                # This is the index after the pivot, where our lists are split
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)


    # Verify it works
    random_list_of_nums = array_to_sort


    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    quick_sort(random_list_of_nums)

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
    """https://stackabuse.com/sorting-algorithms-in-python/#mergesort"""



    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # We use the list lengths often, so its handy to make variables
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # We check which value from the start of each list is smaller
                # If the item at the beginning of the left list is smaller, add it
                # to the sorted list
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                # If the item at the beginning of the right list is smaller, add it
                # to the sorted list
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # If we've reached the end of the of the left list, add the elements
            # from the right list
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            # If we've reached the end of the of the right list, add the elements
            # from the left list
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list



    def merge_sort(nums):
        # If the list is a single element, return it
        if len(nums) <= 1:
            return nums

        # Use floor division to get midpoint, indices must be integers
        mid = len(nums) // 2

        # Sort and merge each half
        left_list = merge_sort(nums[:mid])
        right_list = merge_sort(nums[mid:])

        # Merge the sorted lists into a new one
        return merge(left_list, right_list)


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

    """ -------------------- Chris Algorithm """




    new_sorted_array = []
    process = psutil.Process(os.getpid())
    start_time = time.time()
    #call the sorting algorithm


    for number in array_to_sort:

        if len(new_sorted_array) == 0:
            #error handling, if new sorted list has no entries number is appended
            new_sorted_array.append(number)
            
        elif number > new_sorted_array[-1]:
            #where number is greater than last number of the new sorted list it is appended to the end
            new_sorted_array.append(number)
            
        elif number < new_sorted_array[0]:
            #where number is lower than first number of the sorted list it is inserted to the beginning
            new_sorted_array.insert(0, number)

        elif not number < new_sorted_array[0] and not number > new_sorted_array[-1]:
            #where number is not lower than the number at beginning of the new sorted list ,
            #and number not higher than number at end of new sorted list
            #this code then utilizes a searh to find index of nearest lowest number

            target = number

            res = min(enumerate(new_sorted_array), key=lambda x: abs(target - x[1]))

            res2 = res[0]
            if res2 != 0: 
                new_sorted_array.insert(res2, number)
            elif res2 == 0:
                new_sorted_array.insert(1, number)

        array_to_sort.remove(number)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == 1000:
        chris1000memory.append(float(process.memory_percent()))
        chris1000.append(time_elapsed)
        

    elif testsize == 2500:
        chris2500memory.append(float(process.memory_percent()))
        chris2500.append(time_elapsed)

    elif testsize == 5000:
        chris5000memory.append(float(process.memory_percent()))
        chris5000.append(time_elapsed)

    elif testsize == 7500:
        chris7500memory.append(float(process.memory_percent()))
        chris7500.append(time_elapsed)
        
    elif testsize == 10000:
        chris10000memory.append(float(process.memory_percent()))
        chris10000.append(time_elapsed)
        
    elif testsize == 12500:
        chris12500memory.append(float(process.memory_percent()))
        chris12500.append(time_elapsed)

    elif testsize == 15000:
        chris15000memory.append(float(process.memory_percent()))
        chris15000.append(time_elapsed)

    elif testsize == 20000:
        chris20000memory.append(float(process.memory_percent()))
        chris20000.append(time_elapsed)
        
    elif testsize == 25000:
        chris25000memory.append(float(process.memory_percent()))
        chris25000.append(time_elapsed)
        
    elif testsize == 50000:
        chris50000memory.append(float(process.memory_percent()))
        chris50000.append(time_elapsed)



testsizes = [1000,2500,5000,7500,10000,12500,15000,20000,25000,50000]



for test in testsizes:
    testsize  = test
    count = 0
    while count < 10:
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
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Chris Sort Algorithm", statistics.mean(chris1000),statistics.mean(chris2500),statistics.mean(chris5000),statistics.mean(chris7500),statistics.mean(chris10000),statistics.mean(chris12500),statistics.mean(chris15000),statistics.mean(chris20000),statistics.mean(chris25000),statistics.mean(chris50000)))
print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", statistics.mean(python1000),statistics.mean(python2500),statistics.mean(python5000),statistics.mean(python7500),statistics.mean(python10000),statistics.mean(python12500),statistics.mean(python15000),statistics.mean(python20000),statistics.mean(python25000),statistics.mean(python50000)))



print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", "1000 memory","2500 memory","5000 memory","7500 memory","10000 memory","12500 memory","15000 memory","20000 memory","25000 memory","50000 memory"))
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("Bubble Sort Algorithm", statistics.mean(bubble1000memory),statistics.mean(bubble2500memory),statistics.mean(bubble5000memory),statistics.mean(bubble7500memory),statistics.mean(bubble10000memory),statistics.mean(bubble12500memory),statistics.mean(bubble15000memory),statistics.mean(bubble20000memory),statistics.mean(bubble25000memory),statistics.mean(bubble50000memory)))
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("QuickSort Algorithm", statistics.mean(quick1000memory),statistics.mean(quick2500memory),statistics.mean(quick5000memory),statistics.mean(quick7500memory),statistics.mean(quick10000memory),statistics.mean(quick12500memory),statistics.mean(quick15000memory),statistics.mean(quick20000memory),statistics.mean(quick25000memory),statistics.mean(quick50000memory)))
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("Radix Sort Algorithm", statistics.mean(radix1000memory),statistics.mean(radix2500memory),statistics.mean(radix5000memory),statistics.mean(radix7500memory),statistics.mean(radix10000memory),statistics.mean(radix12500memory),statistics.mean(radix15000memory),statistics.mean(radix20000memory),statistics.mean(radix25000memory),statistics.mean(radix50000memory)))
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("Merge Sort Algorithm", statistics.mean(merge1000memory),statistics.mean(merge2500memory),statistics.mean(merge5000memory),statistics.mean(merge7500memory),statistics.mean(merge10000memory),statistics.mean(merge12500memory),statistics.mean(merge15000memory),statistics.mean(merge20000memory),statistics.mean(merge25000memory),statistics.mean(merge50000memory)))                                                                       
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("Chris Sort Algorithm", statistics.mean(chris1000memory),statistics.mean(chris2500memory),statistics.mean(chris5000memory),statistics.mean(chris7500memory),statistics.mean(chris10000memory),statistics.mean(chris12500memory),statistics.mean(chris15000memory),statistics.mean(chris20000memory),statistics.mean(chris25000memory),statistics.mean(chris50000memory)))
print('{:30} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f} {:12.7f}'.format("Python in-built sort", statistics.mean(python1000memory),statistics.mean(python2500memory),statistics.mean(python5000memory),statistics.mean(python7500memory),statistics.mean(python10000memory),statistics.mean(python12500memory),statistics.mean(python15000memory),statistics.mean(python20000memory),statistics.mean(python25000memory),statistics.mean(python50000memory)))


plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(bubble1000),statistics.mean(bubble2500),statistics.mean(bubble5000),statistics.mean(bubble7500),statistics.mean(bubble10000),statistics.mean(bubble12500),statistics.mean(bubble15000),statistics.mean(bubble20000),statistics.mean(bubble25000),statistics.mean(bubble50000)],label='Bubble Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(quick1000),statistics.mean(quick2500),statistics.mean(quick5000),statistics.mean(quick7500),statistics.mean(quick10000),statistics.mean(quick12500),statistics.mean(quick15000),statistics.mean(quick20000),statistics.mean(quick25000),statistics.mean(quick50000)],label='Quick Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(radix1000),statistics.mean(radix2500),statistics.mean(radix5000),statistics.mean(radix7500),statistics.mean(radix10000),statistics.mean(radix12500),statistics.mean(radix15000),statistics.mean(radix20000),statistics.mean(radix25000),statistics.mean(radix50000)],label='Radix Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(merge1000),statistics.mean(merge2500),statistics.mean(merge5000),statistics.mean(merge7500),statistics.mean(merge10000),statistics.mean(merge12500),statistics.mean(merge15000),statistics.mean(merge20000),statistics.mean(merge25000),statistics.mean(merge50000)],label='Merge Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(chris1000),statistics.mean(chris2500),statistics.mean(chris5000),statistics.mean(chris7500),statistics.mean(chris10000),statistics.mean(chris12500),statistics.mean(chris15000),statistics.mean(chris20000),statistics.mean(chris25000),statistics.mean(chris50000)],label='Chris Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(python1000),statistics.mean(python2500),statistics.mean(python5000),statistics.mean(python7500),statistics.mean(python10000),statistics.mean(python12500),statistics.mean(python15000),statistics.mean(python20000),statistics.mean(python25000),statistics.mean(python50000)],label='Python Inbuilt-Sort')
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")
plt.title("Algorithm Performance By Speed")
plt.savefig("Algorithm_Performance_By_Speed.png")
plt.clf()



plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(bubble1000memory),statistics.mean(bubble2500memory),statistics.mean(bubble5000memory),statistics.mean(bubble7500memory),statistics.mean(bubble10000memory),statistics.mean(bubble12500memory),statistics.mean(bubble15000memory),statistics.mean(bubble20000memory),statistics.mean(bubble25000memory),statistics.mean(bubble50000memory)],label='Bubble Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(quick1000memory),statistics.mean(quick2500memory),statistics.mean(quick5000memory),statistics.mean(quick7500memory),statistics.mean(quick10000memory),statistics.mean(quick12500memory),statistics.mean(quick15000memory),statistics.mean(quick20000memory),statistics.mean(quick25000memory),statistics.mean(quick50000memory)],label='Quick Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(radix1000memory),statistics.mean(radix2500memory),statistics.mean(radix5000memory),statistics.mean(radix7500memory),statistics.mean(radix10000memory),statistics.mean(radix12500memory),statistics.mean(radix15000memory),statistics.mean(radix20000memory),statistics.mean(radix25000memory),statistics.mean(radix50000memory)],label='Radix Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(merge1000memory),statistics.mean(merge2500memory),statistics.mean(merge5000memory),statistics.mean(merge7500memory),statistics.mean(merge10000memory),statistics.mean(merge12500memory),statistics.mean(merge15000memory),statistics.mean(merge20000memory),statistics.mean(merge25000memory),statistics.mean(merge50000memory)],label='Merge Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(chris1000memory),statistics.mean(chris2500memory),statistics.mean(chris5000memory),statistics.mean(chris7500memory),statistics.mean(chris10000memory),statistics.mean(chris12500memory),statistics.mean(chris15000memory),statistics.mean(chris20000memory),statistics.mean(chris25000memory),statistics.mean(chris50000memory)],label='Chris Sort Algorithm')
plt.plot([1000,2500,5000,7500,10000,12500,15000,20000,25000,50000],[statistics.mean(python1000memory),statistics.mean(python2500memory),statistics.mean(python5000memory),statistics.mean(python7500memory),statistics.mean(python10000memory),statistics.mean(python12500memory),statistics.mean(python15000memory),statistics.mean(python20000memory),statistics.mean(python25000memory),statistics.mean(python50000memory)],label='Python Inbuilt-Sort')
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Memory Use %")
plt.title("Algorithm Performance By Memory Usage")
plt.savefig("Algorithm_Performance_By_Memory_Usage.png")
plt.clf()



