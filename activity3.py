import time 


#extracting the sorted array and value from activity3
data = [15, 22, 34, 39, 44, 55, 67, 72, 89, 90]
value = 15


#Starting the measure process of binary search
start_time = time.perf_counter()

#creating binary search function
def binary_search(data, value, start, end):
    if start > end:
        return False 
    else:
        mid = (start + end) // 2 
        if value == data[mid]:
            return mid 
        elif value > data[mid]:
            return binary_search(data, value, mid + 1, end)
        elif value < data[mid]:
            return binary_search(data, value, start, mid - 1)

#Finishing the time measure
end_time = time.perf_counter()
    
#Calculating the time spent on finding the value 
binary_time = end_time - start_time

#implmentation of binary search
exec_binar = binary_search(data,value,0,len(data)-1)

#define the initial time of proceeding the linear search
initiating_measure = time.perf_counter()

#constructing the linear search function
def linear_search(data,value):
    for i in range(len(data)):
        if data[i] == value:
            return i

#define the end of measuring for linear_search function
end = time.perf_counter()

#calculating the time which has been spent on linear_search function
linear_time = end - initiating_measure

#giving the parameters
exec_linear = linear_search(data,value)

#printing the result
print(f'The index of value {value} is {exec_linear}, time spent on is = {linear_time}')
print(f'The index of value {value} is {exec_binar}, time spent on is = {binary_time}')

#determine which func is most efficient
if linear_time > binary_time:
    print(f'Linear search executes with more efficiency, the time which has been spent is {binary_time}')
elif linear_time < binary_time:
    print(f'Binary search executes with more efficiency, the time which has been spent is {linear_time}')