height=int(input("Enter your hieght: "))
if height>=3:
    print("You are eligible to ride !!!")
    age=int(input("Enter your age: "))
    if age<=18:
        print("You entry fee is 250 Rs.")
    else:
        print("Your fee is 500Rs.")
else:
    print("You are not allowed in this ride!!!")
print("Bye Bye !!!")