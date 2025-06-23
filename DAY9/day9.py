# Type Casting in Python - Full Code with Comments

# 1️⃣ Implicit Type Casting
print("---- Implicit Type Casting ----")

# int + float = float
x = 5         # int
y = 2.5       # float
z = x + y     # Python automatically converts int to float
print(z)      # Output: 7.5
print(type(z))  # <class 'float'>

# bool + int = int
a = True      # True is 1
b = 10
print(a + b)  # Output: 11
print(type(a + b))  # <class 'int'>


# 2️⃣ Explicit Type Casting
print("\n---- Explicit Type Casting ----")

# int()
print("\n-- Using int() --")
s = "100"
print(int(s))    # Convert string to int

f = 12.8
print(int(f))    # Convert float to int (decimal removed)

b = True
print(int(b))    # True → 1

# float()
print("\n-- Using float() --")
s = "3.14"
print(float(s))  # Convert string to float

i = 10
print(float(i))  # Convert int to float

# str()
print("\n-- Using str() --")
num = 123
print(str(num))  # Convert int to string

flt = 9.8
print(str(flt))  # Convert float to string

# bool()
print("\n-- Using bool() --")
print(bool(1))        # True
print(bool(0))        # False
print(bool("hello"))  # True
print(bool(""))       # False

# Converting between collections
print("\n-- Collection Conversions --")
lst = [1, 2, 3]
print(tuple(lst))     # Convert list to tuple

tpl = (4, 5, 6)
print(list(tpl))      # Convert tuple to list

text = "abc"
print(list(text))     # Convert string to list: ['a', 'b', 'c']

# Mixed Type Casting Example
print("\n-- Mixed Type Operation --")
s = "10"
n = 5
print(int(s) + n)     # Convert string to int before addition

# Common Error
print("\n-- Common Error Example --")
invalid_str = "abc"
# print(int(invalid_str))  # ❌ Error: cannot convert letters to int
print("Cannot convert 'abc' to int - would cause ValueError!")

### 
PRINT("NEW CODE")