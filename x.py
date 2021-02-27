
def name():
    print
    try :
        user_age = int(input("Please input your age : "))
        if  0 <= user_age <= 3 :
            print("Your a toddler!")
        elif 4 <= user_age <= 12 :
            print("You are a kid!!")
        elif 13 <= user_age <= 19 :

            print("You are a teenager!")
        elif 13 <= user_age <= 19 :
            print("You are a teenager!")
        elif 20 <= user_age <= 30: 
            print("You are a youth!")
        elif user_age >30 :
            print("You are an adult!")

        else :   
            print("You are foolish!!. \nWhich number is that!!")


    except ValueError :

        print("Un expected error occurred!")
        print("You cannot have an age like that!!!")
        print("would you like to start again!!")
        name()
name()        

            

