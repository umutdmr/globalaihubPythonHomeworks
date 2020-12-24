#Extend your program to check if the start_number is an integer between 0 and 100. 
#If so, your program will continue to ask for the second input and perform calculations; 
#otherwise, it prints an error and stops execution.
start_num = int(input())
if start_num <=100 and start_num >= 0:
    stop_num = int(input())
    if stop_num >= start_num and stop_num <= 100:
        res = 0
        for i in range(start_num, stop_num + 1):
            res += i
        print("Result is:", res)
    else:
            print("Invalid stop number!") 
else:
    print("Invalid start number!") 