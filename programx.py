user_age = int(input("Please input your age : "))
 
if user_age < 3 :
     print("You are a toddler!!")
elif user_age >= 4 or <= 12:
     print("You are a kid!") 
elif user_age >= 13 or <=19:
    print('You are a teeneger!')
elif user_age >=20 or <=30:
    print("You are a youth!")
else:
    print('You are an adult!')              