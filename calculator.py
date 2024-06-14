num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calc = str(input("Enter operation(sum,subtract,multiplication,division) only: "))
if calc =="sum":
  print("Sum is:", num1+num2)
elif calc== "subtract" :
  print("Difference is:", num1-num2)
elif calc== "multiplication":
  print("Product is:", num1*num2)
elif calc== "division":
  print("Division is:", num1/num2)
else :
  print("Not in calculator")
print("Program Over")  