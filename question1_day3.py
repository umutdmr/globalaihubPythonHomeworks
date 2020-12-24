#Write a program that inputs an integer value (stop_number) from the user 
#and prints the sum of all numbers from 0 to stop_number. 
#You can assume the user will enter a valid value.
stop_num = int(input())
res = 0
for i in range(stop_num + 1):
    res += i
print(res)