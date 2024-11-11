import random
def extend_generate_sorted_data(array, extension):
    """Extends the original generate function by adding more random integers
    
       Arguments:
       array: original generate function
       extension: Number of extra random integers
    """
    return array +  [random.randint(1,100) for _ in range(extension)]

def merge_sort(list):
    """Recursive function that keeps calling itself until the length of list is 1
    
       Arguments:
       list: the list
    """
    length = len(list)  #number of characters in list
    if length == 1:
        return list # if the list has only one element, return the list
    half = len(list)//2     # Divides the len by 2
    first = (list[:half])   # is the first half of the list
    second = (list[half:])  # is the second half of the list
    

    first_half = merge_sort(first)  #Will call the first half of the list until only 1 element remains
    second_half = merge_sort(second)  #Will call the second half of the list until only 1 element remains


    return merging_halves(first_half, second_half) #After list is brought down to 1 element it goes to next function merging

def merging_halves(first, second):
    """Function that merges the first and second half of the list given in merge_sort function
    
       Arguments:
       first: first half of the list
       second: second half of the list
    """
    mix = [] # Empty list where we will place the sorted elements
    count_first = 0 # Counter for first half of list
    count_second = 0 # Counter for second half of list

    while len(first) > count_first and len(second) > count_second: # A while loop that will keep going until counter for both halves of list is bigger than len of list
        if first[count_first] < second[count_second]: # if statement that checks if the same index of each half is bigger than the other
            mix.append(first[count_first]) # will append the current value of first half of list to the mix list if it is smaller than second half
            count_first = count_first + 1 # adds 1 to the counter of first half list
        else:
            mix.append(second[count_second]) # will append the current value of second half of list to the mix list if it is smaller than first half
            count_second = count_second + 1 # adds 1 to the counter of second half list

    while len(first) > count_first: # a while loop that will add any of the remaining elements of the first half list to mix
        mix.append(first[count_first])
        count_first = count_first + 1

    while len(second) > count_second: # a while loop that will add any of the remaining elements of the second half list to mix
        mix.append(second[count_second])
        count_second = count_second + 1

    return mix # returns the sorted list