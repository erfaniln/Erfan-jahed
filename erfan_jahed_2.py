
# 1
number = int(input("Enter number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    
    
# 2
age = int(input("Enter age: "))


if age < 5:
    print("Free")
elif age <= 18:
    print("Price: 50000 Toman")
elif age <= 60:
    print("Price: 100000 Toman")
else:
    print("Price: 70000 Toman")
    
    

# 3
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
    
    
    
    
# 4
score = float(input("enter your score: "))

if score >= 18:
    print("level A")

elif score >= 15:
    print("level B")

elif score >= 10:
    print("level C")

elif score <= 9:
    print("You are fail")




# 5


level = int(input("enter your level: "))
price = int(input("enter your final price: "))

if level == 1:
    finalprice = price / 2
    if level == 2:
        finalprice = price / 0.25
        if level == 3:
            finalprice = price / 0.05

else:
    print("sell is not available for you")

print(finalprice)