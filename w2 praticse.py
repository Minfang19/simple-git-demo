#e3
count = 0
ques = input("which direction you want to count, up or down?")
if ques == "up":
    top_number = int(input("enter a top number:"))
    for number3 in range(1, (top_number+1)):
        print(number3)   # 直接print函数就可以数每一个数

elif ques == "down":
    down_number = int(input("enter a number below 20:"))
    for number3 in range(20, (down_number-1), -1):   # range(start,end,seperator)
        print(number3)
else:
    print("I don't understand.")


#e2
total = 0
for value in range(0, 5):   # range(1,6)表明了可以输入多少个数字，一般直接end后面要+1； range()函数的使用：https://blog.csdn.net/qq_41799291/article/details/90673570
    number2 = input("enter a number:")
    answer = input("do you want this number to be included?")
    if answer == "yes":
        total = total + int(number2)
    else:
        total = total
print("the total is:", total)



#e1
name = input("enter your name:")
num1 = int(input("enter a number:"))
if num < 10:
    print(num1 * (name+" "))
else:
    print("Too high " * 3)