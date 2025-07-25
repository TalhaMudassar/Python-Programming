# able of contents
# Exercise 1: Perform Basic Tuple Operations
my_tuples = (1,2,3,4,5)
print(f"my tuples are : {my_tuples}")
print(f"third element in my tuple are {my_tuples[2]}")
length_tup = len(my_tuples)
print(f"Length of my tuple are : {length_tup}")

# Exercise 2: Tuple Repetition
my_tuples = (1,2,3,4,5)
multiple_my_tuple = my_tuples * 3
print(f"after multiplication my tuple are : {multiple_my_tuple}")

# Exercise 3: Slicing Tuples
my_tuples3 = (1,2,3,4,5,6,7,8,9,10)
my_tuples3_slice = my_tuples3[2:6]
print(f"after slicling my tuple are : {my_tuples3_slice}")

# Exercise 4: Reverse the tuple
my_tuples4 = (1,2,3,4,5,6,7,8,9,10)

rever_tuple = my_tuples4[::-1]
print(f"reversed tuple are : {rever_tuple}")

# Exercise 5: Access Nested Tuples
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# understand indexing
# tuple1[0] = 'Orange'
# tuple1[1] = [10, 20, 30]
# list1[1][1] = 20
print(tuple1[1][1])

# Exercise 6: Create a tuple with single item 50
single_tuple = (50,)
print(f"sigle tuple are {single_tuple}")

# Exercise 7: Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
tup1,tup2,tup3,tup4 = tuple1
print(f"first are : {tup1}")
print(f"second are : {tup2}")
print(f"third are : {tup3}")
print(f"fourth are : {tup4}")

# Exercise 8: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)

# Exercise 9: Copy Specific Elements From Tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)


# Exercise 10: List to Tuple
my_list = [10, 20, 30]
# Use the tuple() constructor to convert the list
converted_tuple = tuple(my_list)
print(f"Converted list to tuple: {converted_tuple}")


# Exercise 11: Function Returning Tuple
def get_min_max(numbers):
    if not numbers:
        return (None, None) # Handle empty list case
    
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")


# Exercise 12: Comparing Tuples
t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(f"Tuple 1: {t1}")
print(f"Tuple 2: {t2}")

if t1 > t2:
    print(f"{t1} is greater than {t2}")
elif t1 < t2:
    print(f"{t1} is less than {t2}")
else:
    print(f"{t1} is equal to {t2}")
    

# Exercise 13: Removing Duplicates from Tuple
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")
# Convert to a set to remove duplicates (order is not preserved)
unique_elements_set = set(my_tuple)
# Convert back to a tuple
unique_tuple = tuple(unique_elements_set)
print(f"Tuple with unique elements: {unique_tuple}")


# Exercise 14: Filter Tuples
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 95)]
print(f"Original student list: {students}")

high_achievers_loop = []
for student in students:
  if student[1] >= 90:
    high_achievers_loop.append(student)
print(f"Students with scores 90 or above (loop method): {high_achievers_loop}")

# Exercise 15: Map Tuples

t = (1, 2, 3, 4)
print(f"Original tuple: {t}")

# Method 2: Using a loop
squared_list_loop = []
for num in t:
  squared_list_loop.append(num ** 2)
  squared_tuple_loop = tuple(squared_list_loop)
print(f"Squared tuple (loop): {squared_tuple_loop}")

# Exercise 16: Modify Tuple
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


# Exercise 17: Sort a tuple of tuples by 2nd item
# 1. Sort a tuple by 2nd item
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print(f"Original tuple: {tuple1}")
# Convert the tuple to a list because tuples are immutable and cannot be sorted in-place
list1 = list(tuple1)
# Sort the list using the 'sorted()' function with a lambda key
# The lambda function `lambda item: item[1]` tells sorted() to use the second element
# (index 1) of each inner tuple for comparison.
sorted_list = sorted(list1, key=lambda item: item[1])
# If you need the result back as a tuple, convert the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)
print(f"Sorted tuple by 2nd item: {sorted_tuple}")

# Exercise 18: Count Elements
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

# Exercise 19: Check if all items in the tuple are the same
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))