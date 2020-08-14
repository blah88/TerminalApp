#displays the casino interface



def CasinoDisplay():

    #Casino_introduction
    casino_consent=input("In this Casino, you will decide whether the sum of the two dice will be odd or even. \nIf your answer is correct, your betting amount will be doubled. \nIf not, you will lose your betting amount. \nTo play, type in 'let's roll', if not type 'next time'\n")

    if "let" and "roll" in casino_consent:
        betting_amount=0
        betting_amount=input("How much money would you like bet today?\n")

    even_or_odd= input("Is your luck on 'even' or 'odd' today?\n")

    user= input("Type 'roll' to roll the die once\n")

    if user == "roll":
        die_value_1=0
        die_value_1=(random.randint(1, 6))
        print(die_value_1)
    
    user= input("Type 'roll' to roll the die again\n")

    if user == "roll":
        die_value_2=0
        die_value_2=(random.randint(1, 6))
        print(die_value_2)
    if (die_value_1 + die_value_2)%2==0 and even_or_odd=="even":
        print("You have won!")
    elif (die_value_1 + die_value_2)%2==0 and even_or_odd=="odd":
        print("You have lost :( ")
    elif (die_value_1 + die_value_2)%2==1 and even_or_odd=="odd":
        print("You have won!")
    elif (die_value_1 + die_value_2)%2==1 and even_or_odd=="even":
        print("You have lost :(")

#when betting is entered returns earning
# def bet(betting_amount):
#     earning = 0

#     pass
#     return earning
