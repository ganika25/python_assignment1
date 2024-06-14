num1 = int(input("Enter any number: "))
first = 0
second = 1
print("fibonacci series is: ", first,',', second ,end=' ,')
for i in range(2,num1):
    next = first + second
    print(next, end=',')
    first=second
    second = next
    