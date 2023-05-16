name = str(input("What is your name?: "))
yn = str(input("Hello " + name + ", would you like to find out if you are eligible for a raise? (y/n): "))
if yn == "n":
    print("Have a good day.")
if yn == "y": 
    age = int(input("Great! What is your age?: "))
if age < 16:
    print(" Im sorry, you have to be 16 or older for a raise.")
if age > 15:
    school = str(input("What school do you go to?: "))
    
if school == "bvw":
    print("We don't accept your kind")
else:
    money = int(input("How much do you want to make?: "))
if money > 20:
    print("Im sorry, you can not get this raise")
if money < 21:
    print("We can probably make that work!")
    for i in range(5):
        print("$")
