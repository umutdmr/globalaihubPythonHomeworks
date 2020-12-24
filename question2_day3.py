#Extend your program to also input the start_number from the user.
#In this case, your program will add all numbers from start_number to stop_number. 
#You can assume that the user will enter two valid values.
start_num = int(input())
stop_num = int(input())
res = 0
for i in range(start_num, stop_num + 1):
    res += i
print(res)