
age = int(input("Enter your age: "))
    
if age < 5:
    price = 0
elif 5 <= age < 18:
    price = 5
elif 18 <= age < 60:
    price = 10
else:
    price = 7
    
print(f"The ticket price is ${price}.")