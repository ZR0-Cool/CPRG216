'''
 this is our third class demo, we will be working on variables, operators, and stuff i guess
'''
# Review
# assignment

x = 5 # int
y = 2.5 # float
print("x is",x,"and is", type(x))
print("y is",y,"and is", type(y))
z = "this statement is false" # string
print("z is",z,"and is", type(z))
v = False # bool
print("v is",v,"and is", type(v))

# some functions call: print, input, int, float, str, bool

number_as_text = "43" #this is text, not a number
number_as_number = int(number_as_text)
print(number_as_text) # this outputs 43 as a string and not as an integer.
print(number_as_number) # this is still going to output as 43, but as an integer and not a string.
print(str(number_as_number)) # despite starting as an int, it outputs as a string because that's what it was changed to
num = 3
num_f = float(3)

num2 = 3.4
num2_i = int(num2)

num2_as_txt = str(num2)

print(num, num_f, num2, num2_i, num2_as_txt)