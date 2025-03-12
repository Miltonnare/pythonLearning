import datetime
def morning():
        hour=datetime.datetime.now().hour
        if hour <12:
            return "Good Morning"
        elif hour <18:
            return "Good Afternoon"
        else:
            return "Good Evening"

def greeting():
    print("Are you Ready for a greeting? ")
    userName=input("Enter your Name Dear: ").strip().capitalize()
    color=input("What's your Favorite Color: ").strip()
    print(f"{time_greeting}, {userName} your favorite Color is: {color}")

    
time_greeting=morning()

greeting()