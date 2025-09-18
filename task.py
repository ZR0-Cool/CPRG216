# basic calculator

in1 = input("input your first number: \n")
in2 = input("input your second number: \n")
operation = input("input the operation (add | subtract | multiply | divide): \n")

if operation == "add" :
    print(int(in1) + int(in2))

elif operation == "subtract" :
    print(int(in1) - int(in2))

elif operation == "multiply" :
    print(int(in1) * int(in2))

elif operation == "divide" :
    print(int(int(in1) / int(in2)))

else :
    print("invalid input, try again...")

