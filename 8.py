grade = float(input("enter your school grade to see your average: \n"))

if grade >= 90:
    print("your average is Excellent")
elif grade >= 80:
    print("your average is Very Good")
elif grade >= 70:
    print("your average is Good")
elif grade >= 60:
    print("your average is Acceptable")
else:
    print("your average is Fail")