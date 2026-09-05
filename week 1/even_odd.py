def check_even_odd(num):
    if num % 2 == 0:
        return "even number"
    else:
        return "odd number"
num = int(input("enter the number to check even or odd:-"))
number = check_even_odd(num)
print(number)
