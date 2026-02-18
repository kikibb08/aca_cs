print ("Hello, World!")
age = 25
print (f"{age}")
first_name = "Kyriaki"
last_name = "Baker"
print (first_name)
print (f"{last_name}")
x = 10 
y = 5
print (x+y)
print (x-y)
print (x*y)
print (x/y)
temp =72
if temp > 65:
    print("greater than 65")
else:
    print("less than 65")
a = 8 
b = 12
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")
else:
    print("a equals b")
score = 85
if score > 90:
    print("score is greater than 90")
if score <90:
    print("score is less than 90")
else :
    print("score equals 90")
is_raining= True
print(f"{is_raining}")
has_ticket = True
has_id = False
if has_ticket ==True and has_id == True:
    print(f"{has_ticket}{has_id}")
is_closed = True
print(f"{not is_closed}")
name = "alice" 
age = 30
print(f"{name}is {age} years old")
price = 19.99
quantity = 3
print(f"Total cost: ${price*quantity}")
radius = 5
area = (2 ** radius) * 3.14
print(f"the area is {area}")
celsius = 25
fahrenheit = ( celsius * 9/5 +32)
print(f"{celsius}C is {fahrenheit}F")
a = 15
b = 4
c = 2
print(a+(b*c))
print((a+b)*c)
is_weekend = True
is_sunny = True 
print(f"Is it the weekend? : {is_weekend}")
print(f"Is it sunny outside? : {is_sunny}")
print("should i go to the beach? Yes!")
age = 16
has_license = True
if age == 16 and has_license == True:
    print("You can drive!")
hour = 14
if hour < 12 or hour:
    print("It is morning!")
if hour >= 12 or hour < 18:
    print("It is afternoon!")
password = "secret123"
confirm = "secret123"
length = len(password)
if password == confirm:
    print(f"the passwords match and {length}")
x = 7
y = 14
z = 21
if x % y == 0 and x % y == 0: 
    print(f"{x} is even")
else:
    print(f"{x} is odd")
name = "Jordan"
grade = 88
is_passing = grade>= 60 
improvement =  12
print(f"Student {name} scored {grade}, passing:{is_passing}, with {improvement} points improvement")