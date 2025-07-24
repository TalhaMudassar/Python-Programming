#strings
name = "TALHA"
friend = "ALI"
another_frined = 'hassan'

apple = """
here this triple quote we use 
for multiple lining.

"""

print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) # through error becuase 5th index cannot not exist 


print("Lets use a for loop\n")
for character in name:
    print(character,end=" ")