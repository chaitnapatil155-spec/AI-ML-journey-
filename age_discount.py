age = int(input("enter your age: "))

bill_amount = int(input("enter your bill amount: "))

if age <= 5:
    print("Congrats! Your bill amount is 0")

elif 5 < age <= 12:
    discount = bill_amount * 0.5
    print(f"your bill amount is: {bill_amount - discount} after 50% discount")

elif 13 <= age < 60:
    print(f"you don't get any type of discount, our bill amount is: {bill_amount}")

elif age >= 60:
    discount = bill_amount * 0.3
    print(f"your bill amount is: {bill_amount - discount} after 30% discount")
