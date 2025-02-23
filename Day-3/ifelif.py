hei=int(input("Enter you height: "))
hei=float(hei)
if hei >= 5:
    print("Welcome to Wonderla!!!")
    
    age=int(input("Enter your age: "))
    if age >= 18:
        print("You are allowed to water sports")
    else:
        print("You play only in land area...")
        var1=input("DO you know swimming: ")
        if var1 == "Yes":
            print("You are allowed to beach area")
        else:
            print("You can play only in Pool")
else:
    print("You are no allowed in Wonderla!!!")
print("Bye BYe BYe !!!")
    