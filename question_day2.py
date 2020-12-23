"""At a particular company, employees’ salaries are raised progressively, calculated using the following formula:

salary = salary + salary x (raise percentage)

Raises are predefined as given below, according to the current salary of the worker.
 For instance, if the worker’s current salary is less than or equal to 1000 TL, then its salary is increased 15%.

Range	Percentage
0 < salary ≤ 1000	15%
1000 < salary ≤ 2000	10%
2000 < salary ≤ 3000	5%
3000 < salary	2.5%
Write a program that asks the user to enter his/her salary. 
Then your program should calculate and print the raised salary of the user.

Some example program runs:

Please enter your salary: 1000

Your raised salary is 1150.0.

Please enter your salary: 2500

Your raised salary is 2625.0."""
salary = float(input("Please enter your salary: "))
raised_salary = 0
if salary >= 0:
    if salary <= 1000:
        raised_salary = salary * 115 / 100
    elif salary <= 2000:
        raised_salary = salary * 110 / 100
    elif salary <= 3000:
        raised_salary = salary * 105 / 100
    else:
        raised_salary = salary * 102.5 / 100
    print(f"Your raised salary is {raised_salary}.")
else:
    print("Invalid input.")
