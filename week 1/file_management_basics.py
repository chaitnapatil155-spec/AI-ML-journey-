# write file "w"
with open("ai_goal.txt", "w") as file:
    file.write("I will be getting an AI internship in 2027.\n")
    file.write("This is my first data on hard disk.\n")
print("File saved on hard disk successfully!")    

# read file "r"
with open("ai_goal.txt", "r") as file:
    content = file.read()
    print(content)

# append "a" 
with open("ai_goal.txt", "a") as file:
    file.write("Today I did not post on LinkedIn, but I uploaded my code on GitHub.\n")

print("_"*60)
