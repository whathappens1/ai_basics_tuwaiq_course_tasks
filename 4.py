customers = [
    {"name": "m7md", "phone": "0598754321", "email": "m7md@mail.com", "age": 20, "id": 1},
    {"name": "a7md", "phone": "0592684635", "email": "a7md@mail.com", "age": 14, "id": 2},
    {"name": "abdullah", "phone": "0598457578", "email": "abdullah@mail.com", "age": 19, "id": 3},
    {"name": "faris", "phone": "0574775477", "email": "faris@mail.com", "age": 27, "id": 4},
    {"name": "noura", "phone": "0598532556", "email": "noura@mail.com", "age": 55, "id": 5}
]
# step 1: enter customer index to change thier phone number

print("now step 1:")
customers[0]["phone"] = input("Enter the new phone number for customer 1: \n")
print(f"data of customer 1 after edit: \n {customers[0]}")
print("done step 1 \n")

# step 2: enter customer index to remove thier email

print("now step 2:")
x = int(input("Enter customer index to delete thier email: \n"))
customers[x].pop("email")
print(f"data of customer {x} after edit: \n {customers[x]}")
print("done step 2 \n")

# step 3: add gender input for all customers

print("now step 3:")
for c in customers:
    genderInput = str(input(f"Enter gender for {c["name"]}: \n"))
    c["gender"] = genderInput
print(f"data of all customers after edit: \n {customers}")
print("done step 3 \n")

# step 4: enter index customer to clear all thier data

print("now step 4:")
clearDataIndex = int(input("Enter customer index to clear all thier data: \n"))
customers[clearDataIndex].clear()
print(customers[clearDataIndex])
print("done step 4 \n")

# step 5: enter customer index to delete thier dictionary

print("now step 5:")
deleteIndex = int(input("Enter customer index to delete thier dictionary: \n"))
del customers[deleteIndex]
print("done step 5 \n")

print(f"final data of all customers: \n {customers}")

# end
print("===================================================== \n")
print("code by tameem al-sahli (: \n")