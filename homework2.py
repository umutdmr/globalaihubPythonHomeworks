#Create a user by taking name, surname, age, and birth year. Then print something acording to his/her age.
user = []
name = input("please enter your name: ")
surname = input("please enter your surname: ")
age = int(input("please enter your age: "))
birth_year = input("please enter your birth year: ")
user = [name, surname, age, birth_year]
for i in user: 
    print(i)
if age <= 18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")