# print(12)
# print(str(12))
# print(5-3)
# print(3*2)
# print(6/3)
# print(6//3) 
# print(2**3  )
# print(3*3+3/3-3)



print("Welcome to tip calculator !")
total_bill=float(input("What was the total bill ? $"))
given_tip=float(input("how much percentage tip would you like to give? 10 , 12 or 15 : "))
count_people=int(input("how many people to split the bill"))
print(total_bill,type(given_tip))
bill_with_tip=(total_bill*given_tip)/100 + total_bill
tip_for_each=bill_with_tip/count_people
print(bill_with_tip12)
