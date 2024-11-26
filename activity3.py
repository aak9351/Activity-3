import time 


"Define variables for further work"
data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90] # list of sorted numbers
value = 15 # the key which we suppose to find


'Starting the measure process of binary search'
start_time = time.perf_counter()

'creating binary search function'
def binary_search(data, value, start, end):
    if start > end: #indicates the stop case
        return False 
    else:
        mid = (start + end) // 2 #calculates the mid point 
        if value == data[mid]: # compares two value 
            return mid
        elif value > data[mid]: # if value bigger than number at mid index 
            return binary_search(data, value, mid + 1, end) #moves start point till the next index of mid
        elif value < data[mid]: # if value is lesser than number at mid index 
            return binary_search(data, value, start, mid - 1) # sets the end index before mid 

'Finishing the time measure'
end_time = time.perf_counter()
    
'Calculating the time spent on finding the value' 
binary_time = end_time - start_time

'implmentation of binary search'
exec_binar = binary_search(data,value,0,len(data)-1)

'define the initial time of proceeding the linear search'
initiating_measure = time.perf_counter()

'constructing the linear search function'
def linear_search(data,value):
    for i in range(len(data)): # initialize the loop 
        if data[i] == value: # if number at index i is equal to value
            return i # then it returns the i 

'define the end of measuring for linear_search function'
end = time.perf_counter()

'calculating the time which has been spent on linear_search function'
linear_time = end - initiating_measure

'giving the parameters'
exec_linear = linear_search(data,value)

'printing the result'
print(f'The index of value {value}, time spent on is = {linear_time}')
print(f'The index of value {value}, time spent on is = {binary_time}')

'determine which func is most efficient'
if linear_time > binary_time:
    print(f'Linear search executes with more efficiency, the time which has been spent is {binary_time}')
elif linear_time < binary_time:
    print(f'Binary search executes with more efficiency, the time which has been spent is {linear_time}')