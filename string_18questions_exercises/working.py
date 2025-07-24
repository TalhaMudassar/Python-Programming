# Table of contents
# Exercise 1A: Create a string made of the first, middle, and last character
def exercise_1a(name):
    print(f"Original string is: {name}")
    first = name[0]
    print(f"First character is: {first}")
    l = len(name)
    middle = int(l / 2)
    middlevalue = name[middle]
    print(f"Middle character is: {middlevalue}")
    last = name[l - 1]
    print(f"Last character is: {last}")

# Exercise 1B: Create a string made of the middle three characters
def exercise_1b(name_1b):
    length_1b = len(name_1b)
    middle_1b = int(length_1b / 2)
    middle_value = name_1b[middle_1b]
    left_mid_value = name_1b[middle_1b - 1]
    right_mid_value = name_1b[middle_1b + 1]
    print(f"Middle 3 characters are: {left_mid_value, middle_value, right_mid_value}")


# Exercise 2: Append new string in the middle of a given string
def appending_string_middle(string1,string2):
    print(f"original string are {string1,string2}")
    middle = int(len(string1)/2)
    x=string1[:middle:]
    x=x+string2
    x=x+string1[middle:]
    print(f"after appending new string the value are : {x}")

#appending_string_middle("talha","mudassar")
    
    

# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
def newstring(s1,s2):
    first_char = s1[0]+s2[0]
    middle_character = s1[int(len(s1) /2):int(len(s1) / 2) + 1 ]+s2[int(len(s2) / 2):int(len(s2)/2)+1]
    last_character = s1[len(s1)-1]+s2[len(s2)-1]
    add_all = first_char + middle_character + last_character
    print(f"complete  string are : {add_all}")
    
#newstring("talha","mudassar")    
# Exercise 4: Arrange string characters such that lowercase letters should come first
def arranging_charater(s1):
    print("original string are ",s1)
    lower=[]
    upper=[]
    for char in s1:
        if char.islower():
            lower.append(char)
        else:
            upper.append(char)
            
    sorted_str = ''.join(lower + upper)
    print('Result:', sorted_str)

#arranging_charater("talHa")
# Exercise 5: Count all letters, digits, and special symbols from a given string.
def find_digits_chars_symbols(st1):
    for char in st1:
        if char.isalpha():
            print(f"this is alphabetic:{char}")
        elif char.isdigit():
            print(f"this is digit:{char}")
        else:
            print(f"this is special character {char}")

#find_digits_chars_symbols("ta+lh-a_07")
    

# Exercise 6: Create a mixed String using the following rules
def mix_string(st1,st2):
    st1_length = len(st1)
    st2_length = len(st2)
    length = st1_length if st1_length > st2_length else st2_length
    result = ""
    st2=st2[::-1]
    for i in range(length):
        if i < length:
            result +=st1[i]
        if i < length:
            result +=st2[i]
    print(result)
#mix_string("Abc","Xyz")

    

# Exercise 7: String characters balance Test
def check_balance_test(s1,s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag
s1 = "Ynf"
s2 = "PYnative"
#flag = check_balance_test(s1, s2)
#print("s1 and s2 are balanced:", flag)

            
    
# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
def find_occur(st1,find_word):
    count=0
    temp_string= st1.lower()
    find_word = find_word.lower()
    count = temp_string.count(find_word)
    return count   
#counting = find_occur("Welcome to USA. usa awesome, isn't it?","USA")
#print(f"Count are : {counting}")


# Exercise 9: Calculate the sum and average of the digits present in a string
def find_Sum(st1):
    count=0
    sum=0
    for char in st1:
        if char.isdigit():
            sum += int(char)
            count += 1
        else:
            continue
    print(f" the sum are : {sum}")
    average=0
    average = sum/count
    print(f"the average are : {average}")
    
#find_Sum("PYnative29@#8496")  

# Exercise 10: Write a program to count occurrences of all characters within a string
str1 ="Apple"
char_dict= dict()
for char in str1:
    count = str1.count(char)
    char_dict[char]=count
print("result",char_dict)

# Exercise 11: Reverse a given string
string1="Hello how are you?"
rev_string = string1[::-1]
print(f"the reverse string are {rev_string}")

# Exercise 12: Find the last position of a given substring
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)


# Exercise 13: Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)
sub_String = str1.split("-")
for sub in sub_String:
    print(sub)
# Exercise 14: Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)
# Exercise 15: Remove special symbols / punctuation from a string
import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)
new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("New string is ", new_str)

# Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 ears and 10 months old'
digit_string=""
for char in str1:
    if char.isdigit():
        digit_string += char
print(f"exercise 16 :digit string are : {digit_string}")
    
# Exercise 17: Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)

res = []
# split string on whitespace
temp = str1.split()

# Words with both alphabets and numbers
# isdigit() for numbers + isalpha() for alphabets
# use any() to check each character

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

# Exercise 18: Replace each special symbol with # in the following string
import string

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)

# Replace punctuations with #
replace_char = '#'

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print("The strings after replacement : ", str1)
