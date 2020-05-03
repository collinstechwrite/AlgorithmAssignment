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

#imports needed for measuring memory
import os
import psutil

#import needed for measuring time
import time

#import for getting average
import statistics

#import for generating random numbers
from random import randint

#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

#import used to find out computer specs
import wmi

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # KB to GB



testsize = 1
graph_title = ""

bubbletestsiz1 = []
bubbletestsiz2 = []
bubbletestsiz3 = []
bubbletestsiz4 = []
bubbletestsiz5 = []
bubbletestsiz6 = []
bubbletestsiz7 = []
bubbletestsiz8 = []
bubbletestsiz9 = []
bubbletestsiz10 = []

quicktestsiz1 = []
quicktestsiz2 = []
quicktestsiz3 = []
quicktestsiz4 = []
quicktestsiz5 = []
quicktestsiz6 = []
quicktestsiz7 = []
quicktestsiz8 = []
quicktestsiz9 = []
quicktestsiz10 = []

radixtestsiz1 = []
radixtestsiz2 = []
radixtestsiz3 = []
radixtestsiz4 = []
radixtestsiz5 = []
radixtestsiz6 = []
radixtestsiz7 = []
radixtestsiz8 = []
radixtestsiz9 = []
radixtestsiz10 = []

mergetestsiz1 = []
mergetestsiz2 = []
mergetestsiz3 = []
mergetestsiz4 = []
mergetestsiz5 = []
mergetestsiz6 = []
mergetestsiz7 = []
mergetestsiz8 = []
mergetestsiz9 = []
mergetestsiz10 = []

timsorttestsiz1 = []
timsorttestsiz2 = []
timsorttestsiz3 = []
timsorttestsiz4 = []
timsorttestsiz5 = []
timsorttestsiz6 = []
timsorttestsiz7 = []
timsorttestsiz8 = []
timsorttestsiz9 = []
timsorttestsiz10 = []

pythontestsiz1 = []
pythontestsiz2 = []
pythontestsiz3 = []
pythontestsiz4 = []
pythontestsiz5 = []
pythontestsiz6 = []
pythontestsiz7 = []
pythontestsiz8 = []
pythontestsiz9 = []
pythontestsiz10 = []

bubbletestsiz1memory = []
bubbletestsiz2memory = []
bubbletestsiz3memory = []
bubbletestsiz4memory = []
bubbletestsiz5memory = []
bubbletestsiz6memory = []
bubbletestsiz7memory = []
bubbletestsiz8memory = []
bubbletestsiz9memory = []
bubbletestsiz10memory = []

quicktestsiz1memory = []
quicktestsiz2memory = []
quicktestsiz3memory = []
quicktestsiz4memory = []
quicktestsiz5memory = []
quicktestsiz6memory = []
quicktestsiz7memory = []
quicktestsiz8memory = []
quicktestsiz9memory = []
quicktestsiz10memory = []

radixtestsiz1memory = []
radixtestsiz2memory = []
radixtestsiz3memory = []
radixtestsiz4memory = []
radixtestsiz5memory = []
radixtestsiz6memory = []
radixtestsiz7memory = []
radixtestsiz8memory = []
radixtestsiz9memory = []
radixtestsiz10memory = []

mergetestsiz1memory = []
mergetestsiz2memory = []
mergetestsiz3memory = []
mergetestsiz4memory = []
mergetestsiz5memory = []
mergetestsiz6memory = []
mergetestsiz7memory = []
mergetestsiz8memory = []
mergetestsiz9memory = []
mergetestsiz10memory = []

timsorttestsiz1memory = []
timsorttestsiz2memory = []
timsorttestsiz3memory = []
timsorttestsiz4memory = []
timsorttestsiz5memory = []
timsorttestsiz6memory = []
timsorttestsiz7memory = []
timsorttestsiz8memory = []
timsorttestsiz9memory = []
timsorttestsiz10memory = []

pythontestsiz1memory = []
pythontestsiz2memory = []
pythontestsiz3memory = []
pythontestsiz4memory = []
pythontestsiz5memory = []
pythontestsiz6memory = []
pythontestsiz7memory = []
pythontestsiz8memory = []
pythontestsiz9memory = []
pythontestsiz10memory = []


#this function is used for creating randomised unsorted data arrays
def random_array(n):
    array= []
    for i in range (0,n,1):
        array.append(randint(0,n))
    return array

#this function is used for creating sorted data arrays
def sorted_array(n):
    array= []
    for i in range (0,n,1):
        array.append(randint(0,n))
    array.sort() #sorts numbers in order
    return array

#this function is used for creating sorted data arrays
def reversed_array(n):
    array= []
    for i in range (0,n,1):
        array.append(randint(0,n))
    array.sort(reverse = True) #sorts numbers in reverse order
    return array










def call_bubble_sort(array_to_sort):



    def bubble_sort(array):
        """https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python"""
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

    if testsize == testsize1:
        bubbletestsiz1memory.append(float(process.memory_percent()))
        bubbletestsiz1.append(time_elapsed)
        

    elif testsize == testsize2:
        bubbletestsiz2memory.append(float(process.memory_percent()))
        bubbletestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        bubbletestsiz3memory.append(float(process.memory_percent()))
        bubbletestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        bubbletestsiz4memory.append(float(process.memory_percent()))
        bubbletestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        bubbletestsiz5memory.append(float(process.memory_percent()))
        bubbletestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        bubbletestsiz6memory.append(float(process.memory_percent()))
        bubbletestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        bubbletestsiz7memory.append(float(process.memory_percent()))
        bubbletestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        bubbletestsiz8memory.append(float(process.memory_percent()))
        bubbletestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        bubbletestsiz9memory.append(float(process.memory_percent()))
        bubbletestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        bubbletestsiz10memory.append(float(process.memory_percent()))
        bubbletestsiz10.append(time_elapsed)


def call_quick_sort(array_to_sort):


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
    if testsize == testsize1:
        quicktestsiz1memory.append(float(process.memory_percent()))
        quicktestsiz1.append(time_elapsed)
        

    elif testsize == testsize2:
        quicktestsiz2memory.append(float(process.memory_percent()))
        quicktestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        quicktestsiz3memory.append(float(process.memory_percent()))
        quicktestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        quicktestsiz4memory.append(float(process.memory_percent()))
        quicktestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        quicktestsiz5memory.append(float(process.memory_percent()))
        quicktestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        quicktestsiz6memory.append(float(process.memory_percent()))
        quicktestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        quicktestsiz7memory.append(float(process.memory_percent()))
        quicktestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        quicktestsiz8memory.append(float(process.memory_percent()))
        quicktestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        quicktestsiz9memory.append(float(process.memory_percent()))
        quicktestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        quicktestsiz10memory.append(float(process.memory_percent()))
        quicktestsiz10.append(time_elapsed)




def call_radix_sort(array_to_sort):


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

    if testsize == testsize1:
        radixtestsiz1memory.append(float(process.memory_percent()))
        radixtestsiz1.append(time_elapsed)
        

    elif testsize == testsize2:
        radixtestsiz2memory.append(float(process.memory_percent()))
        radixtestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        radixtestsiz3memory.append(float(process.memory_percent()))
        radixtestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        radixtestsiz4memory.append(float(process.memory_percent()))
        radixtestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        radixtestsiz5memory.append(float(process.memory_percent()))
        radixtestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        radixtestsiz6memory.append(float(process.memory_percent()))
        radixtestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        radixtestsiz7memory.append(float(process.memory_percent()))
        radixtestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        radixtestsiz8memory.append(float(process.memory_percent()))
        radixtestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        radixtestsiz9memory.append(float(process.memory_percent()))
        radixtestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        radixtestsiz10memory.append(float(process.memory_percent()))
        radixtestsiz10.append(time_elapsed)


def call_merge_sort(array_to_sort):


    def merge2(left, right):
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


    def merge_sort2(array):
        # If the input array contains fewer than two elements,
        # then return it as the result of the function
        if len(array) < 2:
            return array

        midpoint = len(array) // 2

        # Sort the array by recursively splitting the input
        # into two equal halves, sorting each half and merging them
        # together into the final result
        return merge2(
            left=merge_sort2(array[:midpoint]),
            right=merge_sort2(array[midpoint:]))



    # Verify it works
    random_list_of_nums = array_to_sort

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    random_list_of_nums = merge_sort2(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    if testsize == testsize1:
        mergetestsiz1memory.append(float(process.memory_percent()))
        mergetestsiz1.append(time_elapsed)
        

    elif testsize == testsize2:
        mergetestsiz2memory.append(float(process.memory_percent()))
        mergetestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        mergetestsiz3memory.append(float(process.memory_percent()))
        mergetestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        mergetestsiz4memory.append(float(process.memory_percent()))
        mergetestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        mergetestsiz5memory.append(float(process.memory_percent()))
        mergetestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        mergetestsiz6memory.append(float(process.memory_percent()))
        mergetestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        mergetestsiz7memory.append(float(process.memory_percent()))
        mergetestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        mergetestsiz8memory.append(float(process.memory_percent()))
        mergetestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        mergetestsiz9memory.append(float(process.memory_percent()))
        mergetestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        mergetestsiz10memory.append(float(process.memory_percent()))
        mergetestsiz10.append(time_elapsed)



def call_tim_sort(array_to_sort):
    

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
    if testsize == testsize1:
        timsorttestsiz1memory.append(float(process.memory_percent()))
        timsorttestsiz1.append(time_elapsed)
        

    elif testsize == testsize2:
        timsorttestsiz2memory.append(float(process.memory_percent()))
        timsorttestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        timsorttestsiz3memory.append(float(process.memory_percent()))
        timsorttestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        timsorttestsiz4memory.append(float(process.memory_percent()))
        timsorttestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        timsorttestsiz5memory.append(float(process.memory_percent()))
        timsorttestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        timsorttestsiz6memory.append(float(process.memory_percent()))
        timsorttestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        timsorttestsiz7memory.append(float(process.memory_percent()))
        timsorttestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        timsorttestsiz8memory.append(float(process.memory_percent()))
        timsorttestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        timsorttestsiz9memory.append(float(process.memory_percent()))
        timsorttestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        timsorttestsiz10memory.append(float(process.memory_percent()))
        timsorttestsiz10.append(time_elapsed)


def call_python_inbuilt_sort(array_to_sort):

    #call the sorting algorithm
    process = psutil.Process(os.getpid())
    start_time = time.time()
    python_inbuilt_sorted = sorted(array_to_sort)
    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)
    
    if testsize == testsize1:
        pythontestsiz1memory.append(float(process.memory_percent()))
        pythontestsiz1.append(time_elapsed)
        
    elif testsize == testsize2:
        pythontestsiz2memory.append(float(process.memory_percent()))
        pythontestsiz2.append(time_elapsed)

    elif testsize == testsize3:
        pythontestsiz3memory.append(float(process.memory_percent()))
        pythontestsiz3.append(time_elapsed)

    elif testsize == testsize4:
        pythontestsiz4memory.append(float(process.memory_percent()))
        pythontestsiz4.append(time_elapsed)
        
    elif testsize == testsize5:
        pythontestsiz5memory.append(float(process.memory_percent()))
        pythontestsiz5.append(time_elapsed)
        
    elif testsize == testsize6:
        pythontestsiz6memory.append(float(process.memory_percent()))
        pythontestsiz6.append(time_elapsed)

    elif testsize == testsize7:
        pythontestsiz7memory.append(float(process.memory_percent()))
        pythontestsiz7.append(time_elapsed)

    elif testsize == testsize8:
        pythontestsiz8memory.append(float(process.memory_percent()))
        pythontestsiz8.append(time_elapsed)
        
    elif testsize == testsize9:
        pythontestsiz9memory.append(float(process.memory_percent()))
        pythontestsiz9.append(time_elapsed)
        
    elif testsize == testsize10:
        pythontestsiz10memory.append(float(process.memory_percent()))
        pythontestsiz10.append(time_elapsed)


def main_testing_algorithm(array_to_sort):


    #ensure all tests are the same
    #copy original array pre sort into duplicate arrays to be sorted for each tested algorithm
    array_to_sortB = []
    array_to_sortQ = []
    array_to_sortR = []
    array_to_sortM = []
    array_to_sortT = []
    array_to_sortP = []

    for i in array_to_sort:
        array_to_sortB.append(i)
        array_to_sortQ.append(i)
        array_to_sortR.append(i)
        array_to_sortM.append(i)
        array_to_sortT.append(i)
        array_to_sortP.append(i)

    
    """ -------- Bubble Algorithm -------- """
    if Use_Bubble_Sort == "Y":
        call_bubble_sort(array_to_sortB)
        
    """-------- Quick Sort"""
    if Use_Quick_Sort == "Y":
        call_quick_sort(array_to_sortQ)


    """ -------------------- Radix Sort Algorithm """
    """https://www.programiz.com/dsa/radix-sort"""
    if Use_Radix_Sort == "Y":
        call_radix_sort(array_to_sortR)


    """ -------------------- Merge Sort Algorithm """
    """https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python"""
    if Use_Merge_Sort == "Y":
        call_merge_sort(array_to_sortM)
    

    """ -------------------- Tim Sort"""
    """https://realpython.com/sorting-algorithms-python/#the-timsort-algorithm-in-python"""
    if Use_Tim_Sort == "Y":
        call_tim_sort(array_to_sortT)

    """ -------------------- Python Inbuilt Function"""
    if Use_Python_Inbuilt_Sort == "Y":
        call_python_inbuilt_sort(array_to_sortP)


testsize1 = int(input("Enter a value for test size 1"))
testsize2 = int(input("Enter a value for test size 2"))
testsize3 = int(input("Enter a value for test size 3"))
testsize4 = int(input("Enter a value for test size 4"))
testsize5 = int(input("Enter a value for test size 5"))
testsize6 = int(input("Enter a value for test size 6"))
testsize7 = int(input("Enter a value for test size 7"))
testsize8 = int(input("Enter a value for test size 8"))
testsize9 = int(input("Enter a value for test size 9"))
testsize10 = int(input("Enter a value for test size 10"))




Use_Bubble_Sort = input("Do you want to run test with Bubble Sort? Y or N.")

while Use_Bubble_Sort != "Y" or "N":
    
    if Use_Bubble_Sort == "Y":
        break

    elif Use_Bubble_Sort == "N":
        break

    else:
        Use_Bubble_Sort = input("Do you want to run test with Bubble Sort? Y or N.")


Use_Quick_Sort = input("Do you want to run test with Quick Sort? Y or N.")

while Use_Quick_Sort != "Y" or "N":
    
    if Use_Quick_Sort == "Y":
        break

    elif Use_Quick_Sort == "N":
        break

    else:
        Use_Quick_Sort = input("Do you want to run test with Quick Sort? Y or N.")



Use_Radix_Sort = input("Do you want to run test with Radix Sort? Y or N.")

while Use_Radix_Sort != "Y" or "N":
    
    if Use_Radix_Sort == "Y":
        break

    elif Use_Radix_Sort == "N":
        break

    else:
        Use_Radix_Sort = input("Do you want to run test with Radix Sort? Y or N.")



Use_Merge_Sort = input("Do you want to run test with Merge Sort? Y or N.")

while Use_Merge_Sort != "Y" or "N":
    
    if Use_Merge_Sort == "Y":
        break

    elif Use_Merge_Sort == "N":
        break

    else:
        Use_Merge_Sort = input("Do you want to run test with Merge Sort? Y or N.")



Use_Tim_Sort = input("Do you want to run test with Tim Sort? Y or N.")

while Use_Tim_Sort != "Y" or "N":
    
    if Use_Tim_Sort == "Y":
        break

    elif Use_Tim_Sort == "N":
        break

    else:
        Use_Tim_Sort = input("Do you want to run test with Tim Sort? Y or N.")




Use_Python_Inbuilt_Sort = input("Do you want to run test with Python_Inbuilt Sort? Y or N.")

while Use_Python_Inbuilt_Sort != "Y" or "N":
    
    if Use_Python_Inbuilt_Sort == "Y":
        break

    elif Use_Python_Inbuilt_Sort == "N":
        break

    else:
        Use_Python_Inbuilt_Sort = input("Do you want to run test with Python_Inbuilt Sort? Y or N.")



How_Many_Runs = int(input("How many tests do you want to run?"))


#in future version of benchmarking tool the testsizes can be made variable sizes
testsizes = [testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10]


def unsorted_algorithm():
    global graph_title
    graph_title = "Tests With Unsorted Data"
    global testsize
    for test in testsizes:
        testsize = test
        count = 0
        while count < How_Many_Runs:
            count += 1
            array_to_sort = random_array(test)
            main_testing_algorithm(array_to_sort)
            print("TEST " + str(count) + " OF TEST SIZE " + str(test))
        count = 0


def reversed_algorithm():
    global graph_title
    graph_title = "Tests With Reversed Data"
    global testsize
    for test in testsizes:
        testsize = test
        count = 0
        while count < How_Many_Runs:
            count += 1
            array_to_sort = reversed_array(test)
            main_testing_algorithm(array_to_sort)
            print("TEST " + str(count) + " OF TEST SIZE " + str(test))
        count = 0



def sorted_algorithm():
    global graph_title
    graph_title = "Tests With Sorted Data"
    global testsize
    for test in testsizes:
        testsize = test
        count = 0
        while count < How_Many_Runs:
            count += 1
            array_to_sort = sorted_array(test)
            main_testing_algorithm(array_to_sort)
            print("TEST " + str(count) + " OF TEST SIZE " + str(test))
        count = 0    


#lets users choose whether to test algorithms with unsorted data, reversed data or sorted data
        
Sorted_Or_Unsorted = input("Do you want to run test with unsorted data(U), reversed data(R) or sorted datat(S)? Choose U, R or S.")

while Sorted_Or_Unsorted != "U" or "S":
    
    if Sorted_Or_Unsorted == "U":
        unsorted_algorithm()
        break

    elif Sorted_Or_Unsorted == "R":
        reversed_algorithm()
        break

    elif Sorted_Or_Unsorted == "S":
        sorted_algorithm()
        break

        
    else:
        Sorted_Or_Unsorted = input("Do you want to run test with unsorted data(U) or sorted datat(S)? Choose U or S.")
        

#The code below reports the computer spec

print("Algorithms being tested on:")
print('\nOS Name:' , os_name,'\nOS Version:' , os_version,'\nCPU:', proc_info.Name , '\nRAM:',system_ram,'GB','\nGraphics Card:',gpu_info.Name)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#The code below reports the average speed of each algorithm

print(graph_title)
print("Speed Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", statistics.mean(bubbletestsiz1),statistics.mean(bubbletestsiz2),statistics.mean(bubbletestsiz3),statistics.mean(bubbletestsiz4),statistics.mean(bubbletestsiz5),statistics.mean(bubbletestsiz6),statistics.mean(bubbletestsiz7),statistics.mean(bubbletestsiz8),statistics.mean(bubbletestsiz9),statistics.mean(bubbletestsiz10)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", statistics.mean(quicktestsiz1),statistics.mean(quicktestsiz2),statistics.mean(quicktestsiz3),statistics.mean(quicktestsiz4),statistics.mean(quicktestsiz5),statistics.mean(quicktestsiz6),statistics.mean(quicktestsiz7),statistics.mean(quicktestsiz8),statistics.mean(quicktestsiz9),statistics.mean(quicktestsiz10)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", statistics.mean(radixtestsiz1),statistics.mean(radixtestsiz2),statistics.mean(radixtestsiz3),statistics.mean(radixtestsiz4),statistics.mean(radixtestsiz5),statistics.mean(radixtestsiz6),statistics.mean(radixtestsiz7),statistics.mean(radixtestsiz8),statistics.mean(radixtestsiz9),statistics.mean(radixtestsiz10)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", statistics.mean(mergetestsiz1),statistics.mean(mergetestsiz2),statistics.mean(mergetestsiz3),statistics.mean(mergetestsiz4),statistics.mean(mergetestsiz5),statistics.mean(mergetestsiz6),statistics.mean(mergetestsiz7),statistics.mean(mergetestsiz8),statistics.mean(mergetestsiz9),statistics.mean(mergetestsiz10)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", statistics.mean(timsorttestsiz1),statistics.mean(timsorttestsiz2),statistics.mean(timsorttestsiz3),statistics.mean(timsorttestsiz4),statistics.mean(timsorttestsiz5),statistics.mean(timsorttestsiz6),statistics.mean(timsorttestsiz7),statistics.mean(timsorttestsiz8),statistics.mean(timsorttestsiz9),statistics.mean(timsorttestsiz10)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", statistics.mean(pythontestsiz1),statistics.mean(pythontestsiz2),statistics.mean(pythontestsiz3),statistics.mean(pythontestsiz4),statistics.mean(pythontestsiz5),statistics.mean(pythontestsiz6),statistics.mean(pythontestsiz7),statistics.mean(pythontestsiz8),statistics.mean(pythontestsiz9),statistics.mean(pythontestsiz10)))


print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#The code below reports the average memory used for each algorithm


print(graph_title)
print("Memory Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", statistics.mean(bubbletestsiz1memory),statistics.mean(bubbletestsiz2memory),statistics.mean(bubbletestsiz3memory),statistics.mean(bubbletestsiz4memory),statistics.mean(bubbletestsiz5memory),statistics.mean(bubbletestsiz6memory),statistics.mean(bubbletestsiz7memory),statistics.mean(bubbletestsiz8memory),statistics.mean(bubbletestsiz9memory),statistics.mean(bubbletestsiz10memory)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", statistics.mean(quicktestsiz1memory),statistics.mean(quicktestsiz2memory),statistics.mean(quicktestsiz3memory),statistics.mean(quicktestsiz4memory),statistics.mean(quicktestsiz5memory),statistics.mean(quicktestsiz6memory),statistics.mean(quicktestsiz7memory),statistics.mean(quicktestsiz8memory),statistics.mean(quicktestsiz9memory),statistics.mean(quicktestsiz10memory)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", statistics.mean(radixtestsiz1memory),statistics.mean(radixtestsiz2memory),statistics.mean(radixtestsiz3memory),statistics.mean(radixtestsiz4memory),statistics.mean(radixtestsiz5memory),statistics.mean(radixtestsiz6memory),statistics.mean(radixtestsiz7memory),statistics.mean(radixtestsiz8memory),statistics.mean(radixtestsiz9memory),statistics.mean(radixtestsiz10memory)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", statistics.mean(mergetestsiz1memory),statistics.mean(mergetestsiz2memory),statistics.mean(mergetestsiz3memory),statistics.mean(mergetestsiz4memory),statistics.mean(mergetestsiz5memory),statistics.mean(mergetestsiz6memory),statistics.mean(mergetestsiz7memory),statistics.mean(mergetestsiz8memory),statistics.mean(mergetestsiz9memory),statistics.mean(mergetestsiz10memory)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", statistics.mean(timsorttestsiz1memory),statistics.mean(timsorttestsiz2memory),statistics.mean(timsorttestsiz3memory),statistics.mean(timsorttestsiz4memory),statistics.mean(timsorttestsiz5memory),statistics.mean(timsorttestsiz6memory),statistics.mean(timsorttestsiz7memory),statistics.mean(timsorttestsiz8memory),statistics.mean(timsorttestsiz9memory),statistics.mean(timsorttestsiz10memory)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", statistics.mean(pythontestsiz1memory),statistics.mean(pythontestsiz2memory),statistics.mean(pythontestsiz3memory),statistics.mean(pythontestsiz4memory),statistics.mean(pythontestsiz5memory),statistics.mean(pythontestsiz6memory),statistics.mean(pythontestsiz7memory),statistics.mean(pythontestsiz8memory),statistics.mean(pythontestsiz9memory),statistics.mean(pythontestsiz10memory)))


print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#The code below reports the minimum speed of each algorithm

print("\nMINIMUM TESTS")
print(graph_title)
print("Speed Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", min(bubbletestsiz1),min(bubbletestsiz2),min(bubbletestsiz3),min(bubbletestsiz4),min(bubbletestsiz5),min(bubbletestsiz6),min(bubbletestsiz7),min(bubbletestsiz8),min(bubbletestsiz9),min(bubbletestsiz10)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", min(quicktestsiz1),min(quicktestsiz2),min(quicktestsiz3),min(quicktestsiz4),min(quicktestsiz5),min(quicktestsiz6),min(quicktestsiz7),min(quicktestsiz8),min(quicktestsiz9),min(quicktestsiz10)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", min(radixtestsiz1),min(radixtestsiz2),min(radixtestsiz3),min(radixtestsiz4),min(radixtestsiz5),min(radixtestsiz6),min(radixtestsiz7),min(radixtestsiz8),min(radixtestsiz9),min(radixtestsiz10)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", min(mergetestsiz1),min(mergetestsiz2),min(mergetestsiz3),min(mergetestsiz4),min(mergetestsiz5),min(mergetestsiz6),min(mergetestsiz7),min(mergetestsiz8),min(mergetestsiz9),min(mergetestsiz10)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", min(timsorttestsiz1),min(timsorttestsiz2),min(timsorttestsiz3),min(timsorttestsiz4),min(timsorttestsiz5),min(timsorttestsiz6),min(timsorttestsiz7),min(timsorttestsiz8),min(timsorttestsiz9),min(timsorttestsiz10)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", min(pythontestsiz1),min(pythontestsiz2),min(pythontestsiz3),min(pythontestsiz4),min(pythontestsiz5),min(pythontestsiz6),min(pythontestsiz7),min(pythontestsiz8),min(pythontestsiz9),min(pythontestsiz10)))


print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#The code below reports the minimum memory used for each algorithm

print(graph_title)
print("Memory Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", min(bubbletestsiz1memory),min(bubbletestsiz2memory),min(bubbletestsiz3memory),min(bubbletestsiz4memory),min(bubbletestsiz5memory),min(bubbletestsiz6memory),min(bubbletestsiz7memory),min(bubbletestsiz8memory),min(bubbletestsiz9memory),min(bubbletestsiz10memory)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", min(quicktestsiz1memory),min(quicktestsiz2memory),min(quicktestsiz3memory),min(quicktestsiz4memory),min(quicktestsiz5memory),min(quicktestsiz6memory),min(quicktestsiz7memory),min(quicktestsiz8memory),min(quicktestsiz9memory),min(quicktestsiz10memory)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", min(radixtestsiz1memory),min(radixtestsiz2memory),min(radixtestsiz3memory),min(radixtestsiz4memory),min(radixtestsiz5memory),min(radixtestsiz6memory),min(radixtestsiz7memory),min(radixtestsiz8memory),min(radixtestsiz9memory),min(radixtestsiz10memory)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", min(mergetestsiz1memory),min(mergetestsiz2memory),min(mergetestsiz3memory),min(mergetestsiz4memory),min(mergetestsiz5memory),min(mergetestsiz6memory),min(mergetestsiz7memory),min(mergetestsiz8memory),min(mergetestsiz9memory),min(mergetestsiz10memory)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", min(timsorttestsiz1memory),min(timsorttestsiz2memory),min(timsorttestsiz3memory),min(timsorttestsiz4memory),min(timsorttestsiz5memory),min(timsorttestsiz6memory),min(timsorttestsiz7memory),min(timsorttestsiz8memory),min(timsorttestsiz9memory),min(timsorttestsiz10memory)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", min(pythontestsiz1memory),min(pythontestsiz2memory),min(pythontestsiz3memory),min(pythontestsiz4memory),min(pythontestsiz5memory),min(pythontestsiz6memory),min(pythontestsiz7memory),min(pythontestsiz8memory),min(pythontestsiz9memory),min(pythontestsiz10memory)))


print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")


#The code below reports the maximum / slowest speed of each algorithm

print("\nMAXIMUM TESTS")
print(graph_title)
print("Speed Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", max(bubbletestsiz1),max(bubbletestsiz2),max(bubbletestsiz3),max(bubbletestsiz4),max(bubbletestsiz5),max(bubbletestsiz6),max(bubbletestsiz7),max(bubbletestsiz8),max(bubbletestsiz9),max(bubbletestsiz10)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", max(quicktestsiz1),max(quicktestsiz2),max(quicktestsiz3),max(quicktestsiz4),max(quicktestsiz5),max(quicktestsiz6),max(quicktestsiz7),max(quicktestsiz8),max(quicktestsiz9),max(quicktestsiz10)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", max(radixtestsiz1),max(radixtestsiz2),max(radixtestsiz3),max(radixtestsiz4),max(radixtestsiz5),max(radixtestsiz6),max(radixtestsiz7),max(radixtestsiz8),max(radixtestsiz9),max(radixtestsiz10)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", max(mergetestsiz1),max(mergetestsiz2),max(mergetestsiz3),max(mergetestsiz4),max(mergetestsiz5),max(mergetestsiz6),max(mergetestsiz7),max(mergetestsiz8),max(mergetestsiz9),max(mergetestsiz10)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", max(timsorttestsiz1),max(timsorttestsiz2),max(timsorttestsiz3),max(timsorttestsiz4),max(timsorttestsiz5),max(timsorttestsiz6),max(timsorttestsiz7),max(timsorttestsiz8),max(timsorttestsiz9),max(timsorttestsiz10)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", max(pythontestsiz1),max(pythontestsiz2),max(pythontestsiz3),max(pythontestsiz4),max(pythontestsiz5),max(pythontestsiz6),max(pythontestsiz7),max(pythontestsiz8),max(pythontestsiz9),max(pythontestsiz10)))


print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#The code below reports the maximum memory used for each algorithm

print(graph_title)
print("Memory Test")
print('{:30} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}'.format("Size", str(testsize1),str(testsize2),str(testsize3),str(testsize4),str(testsize5),str(testsize6),str(testsize7),str(testsize8),str(testsize9),str(testsize10)))
if Use_Bubble_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Bubble Sort Algorithm", max(bubbletestsiz1memory),max(bubbletestsiz2memory),max(bubbletestsiz3memory),max(bubbletestsiz4memory),max(bubbletestsiz5memory),max(bubbletestsiz6memory),max(bubbletestsiz7memory),max(bubbletestsiz8memory),max(bubbletestsiz9memory),max(bubbletestsiz10memory)))
if Use_Quick_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("QuickSort Algorithm", max(quicktestsiz1memory),max(quicktestsiz2memory),max(quicktestsiz3memory),max(quicktestsiz4memory),max(quicktestsiz5memory),max(quicktestsiz6memory),max(quicktestsiz7memory),max(quicktestsiz8memory),max(quicktestsiz9memory),max(quicktestsiz10memory)))
if Use_Radix_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Radix Sort Algorithm", max(radixtestsiz1memory),max(radixtestsiz2memory),max(radixtestsiz3memory),max(radixtestsiz4memory),max(radixtestsiz5memory),max(radixtestsiz6memory),max(radixtestsiz7memory),max(radixtestsiz8memory),max(radixtestsiz9memory),max(radixtestsiz10memory)))
if Use_Merge_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Merge Sort Algorithm", max(mergetestsiz1memory),max(mergetestsiz2memory),max(mergetestsiz3memory),max(mergetestsiz4memory),max(mergetestsiz5memory),max(mergetestsiz6memory),max(mergetestsiz7memory),max(mergetestsiz8memory),max(mergetestsiz9memory),max(mergetestsiz10memory)))                                                                       
if Use_Tim_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("timsort Sort Algorithm", max(timsorttestsiz1memory),max(timsorttestsiz2memory),max(timsorttestsiz3memory),max(timsorttestsiz4memory),max(timsorttestsiz5memory),max(timsorttestsiz6memory),max(timsorttestsiz7memory),max(timsorttestsiz8memory),max(timsorttestsiz9memory),max(timsorttestsiz10memory)))
if Use_Python_Inbuilt_Sort == "Y":
    print('{:30} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:12.3f}'.format("Python in-built sort", max(pythontestsiz1memory),max(pythontestsiz2memory),max(pythontestsiz3memory),max(pythontestsiz4memory),max(pythontestsiz5memory),max(pythontestsiz6memory),max(pythontestsiz7memory),max(pythontestsiz8memory),max(pythontestsiz9memory),max(pythontestsiz10memory)))

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#The code below plots graph showing the average speed used by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y

if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(bubbletestsiz1),statistics.mean(bubbletestsiz2),statistics.mean(bubbletestsiz3),statistics.mean(bubbletestsiz4),statistics.mean(bubbletestsiz5),statistics.mean(bubbletestsiz6),statistics.mean(bubbletestsiz7),statistics.mean(bubbletestsiz8),statistics.mean(bubbletestsiz9),statistics.mean(bubbletestsiz10)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(quicktestsiz1),statistics.mean(quicktestsiz2),statistics.mean(quicktestsiz3),statistics.mean(quicktestsiz4),statistics.mean(quicktestsiz5),statistics.mean(quicktestsiz6),statistics.mean(quicktestsiz7),statistics.mean(quicktestsiz8),statistics.mean(quicktestsiz9),statistics.mean(quicktestsiz10)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(radixtestsiz1),statistics.mean(radixtestsiz2),statistics.mean(radixtestsiz3),statistics.mean(radixtestsiz4),statistics.mean(radixtestsiz5),statistics.mean(radixtestsiz6),statistics.mean(radixtestsiz7),statistics.mean(radixtestsiz8),statistics.mean(radixtestsiz9),statistics.mean(radixtestsiz10)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(mergetestsiz1),statistics.mean(mergetestsiz2),statistics.mean(mergetestsiz3),statistics.mean(mergetestsiz4),statistics.mean(mergetestsiz5),statistics.mean(mergetestsiz6),statistics.mean(mergetestsiz7),statistics.mean(mergetestsiz8),statistics.mean(mergetestsiz9),statistics.mean(mergetestsiz10)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(timsorttestsiz1),statistics.mean(timsorttestsiz2),statistics.mean(timsorttestsiz3),statistics.mean(timsorttestsiz4),statistics.mean(timsorttestsiz5),statistics.mean(timsorttestsiz6),statistics.mean(timsorttestsiz7),statistics.mean(timsorttestsiz8),statistics.mean(timsorttestsiz9),statistics.mean(timsorttestsiz10)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(pythontestsiz1),statistics.mean(pythontestsiz2),statistics.mean(pythontestsiz3),statistics.mean(pythontestsiz4),statistics.mean(pythontestsiz5),statistics.mean(pythontestsiz6),statistics.mean(pythontestsiz7),statistics.mean(pythontestsiz8),statistics.mean(pythontestsiz9),statistics.mean(pythontestsiz10)],label='Python Inbuilt-Sort')

plt.legend()
plt.title("\nAverage Speed " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")
plt.show()

#The code below plots graph showing the average memory used  by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y

if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(bubbletestsiz1memory),statistics.mean(bubbletestsiz2memory),statistics.mean(bubbletestsiz3memory),statistics.mean(bubbletestsiz4memory),statistics.mean(bubbletestsiz5memory),statistics.mean(bubbletestsiz6memory),statistics.mean(bubbletestsiz7memory),statistics.mean(bubbletestsiz8memory),statistics.mean(bubbletestsiz9memory),statistics.mean(bubbletestsiz10memory)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(quicktestsiz1memory),statistics.mean(quicktestsiz2memory),statistics.mean(quicktestsiz3memory),statistics.mean(quicktestsiz4memory),statistics.mean(quicktestsiz5memory),statistics.mean(quicktestsiz6memory),statistics.mean(quicktestsiz7memory),statistics.mean(quicktestsiz8memory),statistics.mean(quicktestsiz9memory),statistics.mean(quicktestsiz10memory)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(radixtestsiz1memory),statistics.mean(radixtestsiz2memory),statistics.mean(radixtestsiz3memory),statistics.mean(radixtestsiz4memory),statistics.mean(radixtestsiz5memory),statistics.mean(radixtestsiz6memory),statistics.mean(radixtestsiz7memory),statistics.mean(radixtestsiz8memory),statistics.mean(radixtestsiz9memory),statistics.mean(radixtestsiz10memory)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(mergetestsiz1memory),statistics.mean(mergetestsiz2memory),statistics.mean(mergetestsiz3memory),statistics.mean(mergetestsiz4memory),statistics.mean(mergetestsiz5memory),statistics.mean(mergetestsiz6memory),statistics.mean(mergetestsiz7memory),statistics.mean(mergetestsiz8memory),statistics.mean(mergetestsiz9memory),statistics.mean(mergetestsiz10memory)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(timsorttestsiz1memory),statistics.mean(timsorttestsiz2memory),statistics.mean(timsorttestsiz3memory),statistics.mean(timsorttestsiz4memory),statistics.mean(timsorttestsiz5memory),statistics.mean(timsorttestsiz6memory),statistics.mean(timsorttestsiz7memory),statistics.mean(timsorttestsiz8memory),statistics.mean(timsorttestsiz9memory),statistics.mean(timsorttestsiz10memory)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[statistics.mean(pythontestsiz1memory),statistics.mean(pythontestsiz2memory),statistics.mean(pythontestsiz3memory),statistics.mean(pythontestsiz4memory),statistics.mean(pythontestsiz5memory),statistics.mean(pythontestsiz6memory),statistics.mean(pythontestsiz7memory),statistics.mean(pythontestsiz8memory),statistics.mean(pythontestsiz9memory),statistics.mean(pythontestsiz10memory)],label='Python Inbuilt-Sort')

plt.legend()
plt.title("\nAverage Memory Use % " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Memory Use %")
plt.show()


#The code below plots graph showing the minimum speed / fastest speed used  by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y

if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(bubbletestsiz1),min(bubbletestsiz2),min(bubbletestsiz3),min(bubbletestsiz4),min(bubbletestsiz5),min(bubbletestsiz6),min(bubbletestsiz7),min(bubbletestsiz8),min(bubbletestsiz9),min(bubbletestsiz10)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(quicktestsiz1),min(quicktestsiz2),min(quicktestsiz3),min(quicktestsiz4),min(quicktestsiz5),min(quicktestsiz6),min(quicktestsiz7),min(quicktestsiz8),min(quicktestsiz9),min(quicktestsiz10)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(radixtestsiz1),min(radixtestsiz2),min(radixtestsiz3),min(radixtestsiz4),min(radixtestsiz5),min(radixtestsiz6),min(radixtestsiz7),min(radixtestsiz8),min(radixtestsiz9),min(radixtestsiz10)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(mergetestsiz1),min(mergetestsiz2),min(mergetestsiz3),min(mergetestsiz4),min(mergetestsiz5),min(mergetestsiz6),min(mergetestsiz7),min(mergetestsiz8),min(mergetestsiz9),min(mergetestsiz10)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(timsorttestsiz1),min(timsorttestsiz2),min(timsorttestsiz3),min(timsorttestsiz4),min(timsorttestsiz5),min(timsorttestsiz6),min(timsorttestsiz7),min(timsorttestsiz8),min(timsorttestsiz9),min(timsorttestsiz10)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(pythontestsiz1),min(pythontestsiz2),min(pythontestsiz3),min(pythontestsiz4),min(pythontestsiz5),min(pythontestsiz6),min(pythontestsiz7),min(pythontestsiz8),min(pythontestsiz9),min(pythontestsiz10)],label='Python Inbuilt-Sort')

plt.legend()
plt.title("\nMinimum Speed / Fastest Speed " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")
plt.show()


#The code below plots graph showing the minimum memory used  by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y



if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(bubbletestsiz1memory),min(bubbletestsiz2memory),min(bubbletestsiz3memory),min(bubbletestsiz4memory),min(bubbletestsiz5memory),min(bubbletestsiz6memory),min(bubbletestsiz7memory),min(bubbletestsiz8memory),min(bubbletestsiz9memory),min(bubbletestsiz10memory)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(quicktestsiz1memory),min(quicktestsiz2memory),min(quicktestsiz3memory),min(quicktestsiz4memory),min(quicktestsiz5memory),min(quicktestsiz6memory),min(quicktestsiz7memory),min(quicktestsiz8memory),min(quicktestsiz9memory),min(quicktestsiz10memory)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(radixtestsiz1memory),min(radixtestsiz2memory),min(radixtestsiz3memory),min(radixtestsiz4memory),min(radixtestsiz5memory),min(radixtestsiz6memory),min(radixtestsiz7memory),min(radixtestsiz8memory),min(radixtestsiz9memory),min(radixtestsiz10memory)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(mergetestsiz1memory),min(mergetestsiz2memory),min(mergetestsiz3memory),min(mergetestsiz4memory),min(mergetestsiz5memory),min(mergetestsiz6memory),min(mergetestsiz7memory),min(mergetestsiz8memory),min(mergetestsiz9memory),min(mergetestsiz10memory)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(timsorttestsiz1memory),min(timsorttestsiz2memory),min(timsorttestsiz3memory),min(timsorttestsiz4memory),min(timsorttestsiz5memory),min(timsorttestsiz6memory),min(timsorttestsiz7memory),min(timsorttestsiz8memory),min(timsorttestsiz9memory),min(timsorttestsiz10memory)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[min(pythontestsiz1memory),min(pythontestsiz2memory),min(pythontestsiz3memory),min(pythontestsiz4memory),min(pythontestsiz5memory),min(pythontestsiz6memory),min(pythontestsiz7memory),min(pythontestsiz8memory),min(pythontestsiz9memory),min(pythontestsiz10memory)],label='Python Inbuilt-Sort')
plt.legend()
plt.title("\nMinimum Memory Use % " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Memory Use %")
plt.show()


#The code below plots graph showing the maximum speed used  by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y

if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(bubbletestsiz1),max(bubbletestsiz2),max(bubbletestsiz3),max(bubbletestsiz4),max(bubbletestsiz5),max(bubbletestsiz6),max(bubbletestsiz7),max(bubbletestsiz8),max(bubbletestsiz9),max(bubbletestsiz10)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(quicktestsiz1),max(quicktestsiz2),max(quicktestsiz3),max(quicktestsiz4),max(quicktestsiz5),max(quicktestsiz6),max(quicktestsiz7),max(quicktestsiz8),max(quicktestsiz9),max(quicktestsiz10)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(radixtestsiz1),max(radixtestsiz2),max(radixtestsiz3),max(radixtestsiz4),max(radixtestsiz5),max(radixtestsiz6),max(radixtestsiz7),max(radixtestsiz8),max(radixtestsiz9),max(radixtestsiz10)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(mergetestsiz1),max(mergetestsiz2),max(mergetestsiz3),max(mergetestsiz4),max(mergetestsiz5),max(mergetestsiz6),max(mergetestsiz7),max(mergetestsiz8),max(mergetestsiz9),max(mergetestsiz10)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(timsorttestsiz1),max(timsorttestsiz2),max(timsorttestsiz3),max(timsorttestsiz4),max(timsorttestsiz5),max(timsorttestsiz6),max(timsorttestsiz7),max(timsorttestsiz8),max(timsorttestsiz9),max(timsorttestsiz10)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(pythontestsiz1),max(pythontestsiz2),max(pythontestsiz3),max(pythontestsiz4),max(pythontestsiz5),max(pythontestsiz6),max(pythontestsiz7),max(pythontestsiz8),max(pythontestsiz9),max(pythontestsiz10)],label='Python Inbuilt-Sort')
plt.legend()
plt.title("\nMaximum Speed / Slowest Speed " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")
plt.show()


#The code below plots graph showing the maximum memory used  by each algorithm, the code only loads algorithms into the graph that have been chosen by user, e.g. if Y

if Use_Bubble_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(bubbletestsiz1memory),max(bubbletestsiz2memory),max(bubbletestsiz3memory),max(bubbletestsiz4memory),max(bubbletestsiz5memory),max(bubbletestsiz6memory),max(bubbletestsiz7memory),max(bubbletestsiz8memory),max(bubbletestsiz9memory),max(bubbletestsiz10memory)],label='Bubble Sort Algorithm')
if Use_Quick_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(quicktestsiz1memory),max(quicktestsiz2memory),max(quicktestsiz3memory),max(quicktestsiz4memory),max(quicktestsiz5memory),max(quicktestsiz6memory),max(quicktestsiz7memory),max(quicktestsiz8memory),max(quicktestsiz9memory),max(quicktestsiz10memory)],label='Quick Sort Algorithm')
if Use_Radix_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(radixtestsiz1memory),max(radixtestsiz2memory),max(radixtestsiz3memory),max(radixtestsiz4memory),max(radixtestsiz5memory),max(radixtestsiz6memory),max(radixtestsiz7memory),max(radixtestsiz8memory),max(radixtestsiz9memory),max(radixtestsiz10memory)],label='Radix Sort Algorithm')
if Use_Merge_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(mergetestsiz1memory),max(mergetestsiz2memory),max(mergetestsiz3memory),max(mergetestsiz4memory),max(mergetestsiz5memory),max(mergetestsiz6memory),max(mergetestsiz7memory),max(mergetestsiz8memory),max(mergetestsiz9memory),max(mergetestsiz10memory)],label='Merge Sort Algorithm')
if Use_Tim_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(timsorttestsiz1memory),max(timsorttestsiz2memory),max(timsorttestsiz3memory),max(timsorttestsiz4memory),max(timsorttestsiz5memory),max(timsorttestsiz6memory),max(timsorttestsiz7memory),max(timsorttestsiz8memory),max(timsorttestsiz9memory),max(timsorttestsiz10memory)],label='Tim Sort Algorithm')
if Use_Python_Inbuilt_Sort == "Y":
    plt.plot([testsize1,testsize2,testsize3,testsize4,testsize5,testsize6,testsize7,testsize8,testsize9,testsize10],[max(pythontestsiz1memory),max(pythontestsiz2memory),max(pythontestsiz3memory),max(pythontestsiz4memory),max(pythontestsiz5memory),max(pythontestsiz6memory),max(pythontestsiz7memory),max(pythontestsiz8memory),max(pythontestsiz9memory),max(pythontestsiz10memory)],label='Python Inbuilt-Sort')
plt.legend()
plt.title("\nMaximum Memory Use % " + graph_title)
plt.xlabel("Input Size")
plt.ylabel("Memory Use %")
plt.show()










