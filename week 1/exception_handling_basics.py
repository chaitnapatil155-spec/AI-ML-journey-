try:
    num = int(input("Enter the number: "))
    result = num * 10 
    print("Result:", result)
except ValueError:
    print("Error: You did not enter a valid number!") 
    print("Please run the program again and enter digits only (1, 2, 3).") 

print("Program is running successfully without crashing!")      
