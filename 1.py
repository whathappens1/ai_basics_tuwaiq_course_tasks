name = str(input("Enter your name: ")) # اسم المستخدم
age = int(input("Enter your age: ")) # عمر المستخدم
isStudent = bool(input("Are you a student? (True/False): ")) # هل هو طالب


print(f"your name: {name} and your age: {age} and you are a student: {isStudent}") # اطبع اسم المستخدم وعمره
print(type(name),type(age),type(isStudent)) # اطبع نوع كل متغير
