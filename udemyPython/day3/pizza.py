print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").strip().lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").strip().lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().lower()


bill = 0

if size == "s":
    bill += 15
    if pepperoni == "y":
        bill += 2
elif size == "m":
    bill += 20
    if pepperoni == "y":
        bill += 3
elif size == "l":
    bill += 25
    if pepperoni == "y":
        bill += 3
else:
    print("You typed the wrong input.")
    exit()

if extra_cheese == "y":
    bill += 1

print(f"Your final bill will be: ${bill}")
