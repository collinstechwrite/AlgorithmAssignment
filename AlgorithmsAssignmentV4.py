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




import statistics
import time
from random import randint


#imports needed for plotting graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
bubble500 = []
bubble1000 = []
bubble1250 = []
bubble2500 = []
bubble3750 = []
bubble5000 = []
bubble6250 = []
bubble7500 = []
bubble8750 = []
bubble10000 = []

quick500 = []
quick1000 = []
quick1250 = []
quick2500 = []
quick3750 = []
quick5000 = []
quick6250 = []
quick7500 = []
quick8750 = []
quick10000 = []

radix500 = []
radix1000 = []
radix1250 = []
radix2500 = []
radix3750 = []
radix5000 = []
radix6250 = []
radix7500 = []
radix8750 = []
radix10000 = []

merge500 = []
merge1000 = []
merge1250 = []
merge2500 = []
merge3750 = []
merge5000 = []
merge6250 = []
merge7500 = []
merge8750 = []
merge10000 = []

chris500 = []
chris1000 = []
chris1250 = []
chris2500 = []
chris3750 = []
chris5000 = []
chris6250 = []
chris7500 = []
chris8750 = []
chris10000 = []

python500 = []
python1000 = []
python1250 = []
python2500 = []
python3750 = []
python5000 = []
python6250 = []
python7500 = []
python8750 = []
python10000 = []



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
    start_time = time.time()
    bubble_sort(random_list_of_nums)


    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)


    if testsize == 500:
        bubble500.append(time_elapsed)

    elif testsize == 1000:
        bubble1000.append(time_elapsed)

    elif testsize == 1250:
        bubble1250.append(time_elapsed)

    elif testsize == 2500:
        bubble2500.append(time_elapsed)
        
    elif testsize == 3750:
        bubble3750.append(time_elapsed)
        
    elif testsize == 5000:
        bubble5000.append(time_elapsed)

    elif testsize == 6250:
        bubble6250.append(time_elapsed)

    elif testsize == 7500:
        bubble7500.append(time_elapsed)
        
    elif testsize == 8750:
        bubble8750.append(time_elapsed)
        
    elif testsize == 10000:
        bubble10000.append(time_elapsed)


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
    start_time = time.time()
    quick_sort(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)


    if testsize == 500:
        quick500.append(time_elapsed)

    elif testsize == 1000:
        quick1000.append(time_elapsed)

    elif testsize == 1250:
        quick1250.append(time_elapsed)

    elif testsize == 2500:
        quick2500.append(time_elapsed)
        
    elif testsize == 3750:
        quick3750.append(time_elapsed)
        
    elif testsize == 5000:
        quick5000.append(time_elapsed)

    elif testsize == 6250:
        quick6250.append(time_elapsed)

    elif testsize == 7500:
        quick7500.append(time_elapsed)
        
    elif testsize == 8750:
        quick8750.append(time_elapsed)
        
    elif testsize == 10000:
        quick10000.append(time_elapsed)








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
    start_time = time.time()
    radixSort(data)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)



    if testsize == 500:
        radix500.append(time_elapsed)

    elif testsize == 1000:
        radix1000.append(time_elapsed)

    elif testsize == 1250:
        radix1250.append(time_elapsed)

    elif testsize == 2500:
        radix2500.append(time_elapsed)
        
    elif testsize == 3750:
        radix3750.append(time_elapsed)
        
    elif testsize == 5000:
        radix5000.append(time_elapsed)

    elif testsize == 6250:
        radix6250.append(time_elapsed)

    elif testsize == 7500:
        radix7500.append(time_elapsed)
        
    elif testsize == 8750:
        radix8750.append(time_elapsed)
        
    elif testsize == 10000:
        radix10000.append(time_elapsed)








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
    start_time = time.time()
    random_list_of_nums = merge_sort(random_list_of_nums)

    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)



    if testsize == 500:
        merge500.append(time_elapsed)

    elif testsize == 1000:
        merge1000.append(time_elapsed)

    elif testsize == 1250:
        merge1250.append(time_elapsed)

    elif testsize == 2500:
        merge2500.append(time_elapsed)
        
    elif testsize == 3750:
        merge3750.append(time_elapsed)
        
    elif testsize == 5000:
        merge5000.append(time_elapsed)

    elif testsize == 6250:
        merge6250.append(time_elapsed)

    elif testsize == 7500:
        merge7500.append(time_elapsed)
        
    elif testsize == 8750:
        merge8750.append(time_elapsed)
        
    elif testsize == 10000:
        merge10000.append(time_elapsed)




    """ -------------------- Python Inbuilt Function"""


    #call the sorting algorithm
    start_time = time.time()
    python_inbuilt_sorted = sorted(array_to_sort)
    end_time = time.time()
    time_elapsed = end_time - start_time
    time_elapsed = float(time_elapsed)


    if testsize == 500:
        python500.append(time_elapsed)

    elif testsize == 1000:
        python1000.append(time_elapsed)

    elif testsize == 1250:
        python1250.append(time_elapsed)

    elif testsize == 2500:
        python2500.append(time_elapsed)
        
    elif testsize == 3750:
        python3750.append(time_elapsed)
        
    elif testsize == 5000:
        python5000.append(time_elapsed)

    elif testsize == 6250:
        python6250.append(time_elapsed)

    elif testsize == 7500:
        python7500.append(time_elapsed)
        
    elif testsize == 8750:
        python8750.append(time_elapsed)
        
    elif testsize == 10000:
        python10000.append(time_elapsed)
    



    """ -------------------- Chris Algorithm """




    new_sorted_array = []
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

    if testsize == 500:
        chris500.append(time_elapsed)

    elif testsize == 1000:
        chris1000.append(time_elapsed)

    elif testsize == 1250:
        chris1250.append(time_elapsed)

    elif testsize == 2500:
        chris2500.append(time_elapsed)
        
    elif testsize == 3750:
        chris3750.append(time_elapsed)
        
    elif testsize == 5000:
        chris5000.append(time_elapsed)

    elif testsize == 6250:
        chris6250.append(time_elapsed)

    elif testsize == 7500:
        chris7500.append(time_elapsed)
        
    elif testsize == 8750:
        chris8750.append(time_elapsed)
        
    elif testsize == 10000:
        chris10000.append(time_elapsed)




testsizes = [500,1000,1250,2500,3750,5000,6250,7500,8750,10000]



for test in testsizes:
    testsize  = test
    count = 0
    while count < 10:
        count += 1
        array_to_sort = random_array(test)
        main_testing_algorithm(array_to_sort)
        print("TEST " + str(count) + " OF TEST SIZE " + str(test))
    count = 0



print('{:30} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7} {:>7}'.format("Size", "500","1000","1250","2500","3750","5000","6250","7500","8750","10000"))
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("Bubble Sort Algorithm", statistics.mean(bubble500),statistics.mean(bubble1000),statistics.mean(bubble1250),statistics.mean(bubble2500),statistics.mean(bubble3750),statistics.mean(bubble5000),statistics.mean(bubble6250),statistics.mean(bubble7500),statistics.mean(bubble8750),statistics.mean(bubble10000)))
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("QuickSort Algorithm", statistics.mean(quick500),statistics.mean(quick1000),statistics.mean(quick1250),statistics.mean(quick2500),statistics.mean(quick3750),statistics.mean(quick5000),statistics.mean(quick6250),statistics.mean(quick7500),statistics.mean(quick8750),statistics.mean(quick10000)))
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("Radix Sort Algorithm", statistics.mean(radix500),statistics.mean(radix1000),statistics.mean(radix1250),statistics.mean(radix2500),statistics.mean(radix3750),statistics.mean(radix5000),statistics.mean(radix6250),statistics.mean(radix7500),statistics.mean(radix8750),statistics.mean(radix10000)))
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("Merge Sort Algorithm", statistics.mean(merge500),statistics.mean(merge1000),statistics.mean(merge1250),statistics.mean(merge2500),statistics.mean(merge3750),statistics.mean(merge5000),statistics.mean(merge6250),statistics.mean(merge7500),statistics.mean(merge8750),statistics.mean(merge10000)))                                                                       
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("Chris Sort Algorithm", statistics.mean(chris500),statistics.mean(chris1000),statistics.mean(chris1250),statistics.mean(chris2500),statistics.mean(chris3750),statistics.mean(chris5000),statistics.mean(chris6250),statistics.mean(chris7500),statistics.mean(chris8750),statistics.mean(chris10000)))
print('{:30} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f} {:7.3f}'.format("Python in-built sort", statistics.mean(python500),statistics.mean(python1000),statistics.mean(python1250),statistics.mean(python2500),statistics.mean(python3750),statistics.mean(python5000),statistics.mean(python6250),statistics.mean(python7500),statistics.mean(python8750),statistics.mean(python10000)))


plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(bubble500),statistics.mean(bubble1000),statistics.mean(bubble1250),statistics.mean(bubble2500),statistics.mean(bubble3750),statistics.mean(bubble5000),statistics.mean(bubble6250),statistics.mean(bubble7500),statistics.mean(bubble8750),statistics.mean(bubble10000)],label='Bubble Sort Algorithm')
plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(quick500),statistics.mean(quick1000),statistics.mean(quick1250),statistics.mean(quick2500),statistics.mean(quick3750),statistics.mean(quick5000),statistics.mean(quick6250),statistics.mean(quick7500),statistics.mean(quick8750),statistics.mean(quick10000)],label='Quick Sort Algorithm')
plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(radix500),statistics.mean(radix1000),statistics.mean(radix1250),statistics.mean(radix2500),statistics.mean(radix3750),statistics.mean(radix5000),statistics.mean(radix6250),statistics.mean(radix7500),statistics.mean(radix8750),statistics.mean(radix10000)],label='Radix Sort Algorithm')
plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(merge500),statistics.mean(merge1000),statistics.mean(merge1250),statistics.mean(merge2500),statistics.mean(merge3750),statistics.mean(merge5000),statistics.mean(merge6250),statistics.mean(merge7500),statistics.mean(merge8750),statistics.mean(merge10000)],label='Merge Sort Algorithm')
plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(chris500),statistics.mean(chris1000),statistics.mean(chris1250),statistics.mean(chris2500),statistics.mean(chris3750),statistics.mean(chris5000),statistics.mean(chris6250),statistics.mean(chris7500),statistics.mean(chris8750),statistics.mean(chris10000)],label='Chris Sort Algorithm')
plt.plot([500,1000,1250,2500,3750,5000,6250,7500,8750,10000],[statistics.mean(python500),statistics.mean(python1000),statistics.mean(python1250),statistics.mean(python2500),statistics.mean(python3750),statistics.mean(python5000),statistics.mean(python6250),statistics.mean(python7500),statistics.mean(python8750),statistics.mean(python10000)],label='Python Inbuilt-Sort')
plt.legend()
plt.xlabel("Input Size")
plt.ylabel("Running Time(Milliseconds)")


plt.show()





