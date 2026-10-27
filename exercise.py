# question 1 arthmeric and assignment operators
x = 8 
y = 6
x += 3
y *= 2
result = x / y
print(result)
 
# question 2
b = 10
a = 15
c = 20
cond1 = a > b 
cond2 = b % 2== 0
cond3 = c <= a
final_condition = cond1 or (cond2 and cond3)
print(final_condition)

# question 3
score = 50
if  score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 70:
    grade = "C"
elif score > 60:
    grade = "D"

else:
    grade = "F"
print (grade)

# question 4 

num1 = float (8)
num2 = float (6)
operation = input("enter an operation (+, -, *, /): ") 
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2 
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("error ; division by zero is not allow ")
        result = None

    else:
        result = num1 / num2
    
else:
    result = "invalid operation selected"

if result is not None:
    print(result)


    