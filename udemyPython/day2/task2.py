print("Welcome to roller coster!")
height=int(input("What is your height in cm ? "))

if height>112:
    print("Congratulation you are eligible for rollercoaster")
    age=int(input("what is your age ?"))
    if age<=12:
        print("Please pay 5$.")
    elif(age<=18):
        print("Please pay $7.")
    else:
        print("please pay $7.")
else:
    print("Sorry !! you are not eligible for this.")
    
    

