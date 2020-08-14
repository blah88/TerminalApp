#!/usr/sbin/python
import sys
if  "--help" in sys.argv:
    print("""
Welcome to 'You Wake Up In Alone In A Forest'.

This game is a text-based adventure game that is in a form of a terminal app.

Your main and only form of interaction is with the command line.

After an introduction you will be presented with a Heads Up Display that shows 



""")

from time import sleep
import time
import sys
import os
import random

#import encounter
import display
import merchant
import encounter

#Initial Setting
items = {}
fruits=0
mushroom=0
hatchet=0
armour=0
machete=0
mysterious=0
money = 1000000

health = 400
status = "Bleeding"
LocationID=1
action = display.location[LocationID]["action"]
interact = display.location[LocationID]["Interactable"]
CurrentLocation = display.location[LocationID]["name"]
CanGoTo = display.location[LocationID]["CanGoTo"]
picture = display.location[LocationID]["draw"]

#Introduction
line_1 = """

You wake up alone in a forest.

"""

display.animatetype(line_1)
sleep(2)

line_2 = """
You don't remember who you are. 
You feel light headed as you stand up. 
You feel a sharp pain at the back of your head. 
You find a deep wound. 
You are bleeding enough to get you worried. 
You feel dizzy. 

You somehow know that you don't have long before collapse into an unknown fate.

"""

display.animatetype(line_2)
sleep(2)

line_3 = """
You desperately look around to find an old hatchet lodged into the side of a tree with mysterious red fruits.

"""

display.animatetype(line_3)
sleep(2)

line_4 = """
To retrieve the hatchet type and enter the word “hatchet”.

"""

display.animatetype(line_4)
user = input()

if user =="hatchet":
    hatchet+=1
    items.update({"hatchet":hatchet})
    print("You obtained a hatchet.")
    sleep(1)
else:
    while user != "hatchet":
        user = input("Type in the word 'hatchet'")
        items.update({"hatchet":1})
        print("You obtained a hatchet.")
        sleep(1)

user = input("""
You find the mysterious fruit is good to eat and pleasing to the eye. 
You try to take a fruit from the tree but it will not come off easily.
Use hatchet to obtain the fruit. 

Type 'fruit,cut' to get the fruit.

""")

if "fruit" in user and "cut" in user:
    fruits+=1
    items.update({"fruit":fruits})
    print("You obtained a fruit.")
sleep(1)

os.system("clear")
display.tophud(CurrentLocation,display.location[1]["CanGoTo"])
print(display.location[1]["draw"])
display.downhud(items,action,health,status,money,interact)
print("To cut more fruit type 'cut,fruit' again.\nTo go to the deeper into the forest type 'goto deeper forest'.\nIf you want to go to The Road type 'goto road'.")

while user!="exit game":
    user=input()
    customer=""
    RoadInteraction=""   

    if health<=0:
        os.system("clear")
        print("\n\nGame Over\n\n")
        sleep(3)
        sys.exit()

    #status
    if status == "Bleeding":
        stat=random.randint(0, 1)
        if stat == 0:
            health-=5
            os.system("clear")
            display.tophud(CurrentLocation,CanGoTo)
            print(picture)
            display.downhud(items,action,health,status,money,interact)
    
    if status == "Poisoned":
        stat=random.randint(0, 4)
        if stat == 0:
            health-=15
            os.system("clear")
            display.tophud(CurrentLocation,CanGoTo)
            print(picture)
            display.downhud(items,action,health,status,money,interact)

 #   if CurrentLocation == "road" and 

    #actions
    if "cut" in user and "fruit" in user and CurrentLocation == "forest":
        fruits+=1
        items.update({"fruit":fruits})
        print("You obtained a fruit.")
        sleep(1)

    if "eat" in user and "fruit" in user and mushroom > 0:
        fruits-=1
        health+=10
        items.update({"fruit":fruits})
        print("You ate a fruit.")
        if fruits==0:
            items.pop("fruit")

    if "eat" in user and "mushroom" in user and mushroom > 0:
        mushroom-=1
        health+=40
        items.update({"mushroom":mushroom})
        print("You ate a mushroom.")
        if fruits==0:
            items.pop("mushroom")


    #encounter 
    trigger = random.randint(0,5)
    trigger = 4

    if CurrentLocation == "road" and trigger==4:
        while RoadInteraction != "run":
            os.system("clear")
            encounter.EncounterBeggar()
            display.downhud(items,{"give", "run"},health,status,money,interact)    
            RoadInteraction = input()
            TipChance = random.randint(0,1)
            if "give" in RoadInteraction and "fruit" in RoadInteraction and fruits>0:
                fruits-=1
                items.update({"fruit":fruits})
                if fruits==0:
                    items.pop("fruit")
                print("Gave a fruit to the beggar. He thanks you.")
                sleep(2)
                if TipChance==1:
                    print("The beggar tells you that the mysterious object sold at the town store is related to the chest in the deeper forest")
                    sleep(4)
                break

            if "give" in RoadInteraction and "mushroom" in RoadInteraction and mushroom>0:
                mushroom-=1
                items.update({"mushroom":mushroom})
                if mushroom==0:
                    items.pop("mushroom")
                print("Gave a mushroom to the beggar. He thanks you.")
                sleep(2)
                if TipChance==1:
                    print("The beggar tells you that the mysterious object sold at the town store is related to the chest in the deeper forest")
                    sleep(4)                
                break

    #combat with bandit
    BanditHealth=40

    if CurrentLocation == "road" and trigger==5:
        while RoadInteraction != "run":
            while health>0 and BanditHealth>0:
                os.system("clear")
                encounter.EncounterBandit(5)
                print(f"Bandit's health: {BanditHealth}\n")
                display.downhud(items,{"attack", "run"},health,status,money,{"bandit"})    
                RoadInteraction = input()
                if RoadInteraction == "run":
                    break
                AttackChance = random.randint(0,10)
                if AttackChance%3==0:
                    health-=10
                    os.system("clear")
                    encounter.EncounterBandit(5)
                    print(f"Bandit's health: {BanditHealth}\n")
                    display.downhud(items,{"attack", "run"},health,status,money,{"bandit"})    
                    print("The bandit attempted to attack and succeeded!")
                    sleep(2)
                else:
                    os.system("clear")
                    encounter.EncounterBandit(5)
                    print(f"Bandit's health: {BanditHealth}\n")
                    display.downhud(items,{"attack", "run"},health,status,money,{"bandit"})    
                    print("The bandit attempted to attack and missed!")
                    sleep(2)

                if "attack" in RoadInteraction and "bandit" in RoadInteraction:
                    if "hatchet" in items:
                        BanditHealth-=20
                    if "machete" in items:
                        BanditHealth-=40
                    else:
                        BanditHealth-=10
                    os.system("clear")
                    encounter.EncounterBandit(5)
                    print(f"Bandit's health: {BanditHealth}\n")
                    display.downhud(items,{"attack", "run"},health,status,money,{"bandit"})    
                    print("You attempted to attack the bandit and succeeded!")
                    sleep(2)
                else:
                    os.system("clear")
                    encounter.EncounterBandit(5)
                    print(f"Bandit's health: {BanditHealth}\n")
                    display.downhud(items,{"attack", "run"},health,status,money,{"bandit"})    
                    print("You attempted to attack the bandit and missed!")

                if health<=0:
                    os.system("clear")
                    print("\n\nGame Over\n\n")
                    sleep(3)
                    sys.exit()

                if BanditHealth <= 0:
                    loot=random.randint(0,1)
                    lootgold=random.randint(1,50)
                    money+=lootgold
                    print("You have defeated the bandit!")
                    print(f"You took {lootgold} from the bandit")
                    if loot==1:
                        hatchet+=1
                        items.update({"hatchet":hatchet})
                        print(f"You took a hatchet from the bandit!")
                    sleep(4)    
                    break
            break

    #store
    elif CurrentLocation == "store" and "merchant" in user and "engage" in user:
        while customer != "exit":
            os.system("clear")
            merchant.store(items)
            display.downhud(items,{"buy","sell","exit"},health,status,money,interact)

            customer=input()
            #sell
            if "sell" in customer and "fruit" in customer and (fruits > 0):
                fruits-=1
                money+=1
                items.update({"fruit":fruits})
                if fruits==0:
                    items.pop("fruit")
                print("Sold a fruit")
                sleep(2)
            if "sell" in customer and "mushroom" in customer and (mushroom > 0):
                mushroom-=1
                money+=5
                items.update({"mushroom":mushroom})
                if mushroom==0:
                    items.pop("mushroom")
                print("Sold a mushroom")
                sleep(2)
            if "sell" in customer and "hatchet" in customer and (hatchet > 0):
                hatchet-=1
                money+=10
                items.update({"hatchet":hatchet})
                if hatchet==0:
                    items.pop("hatchet")
                print("Sold a hatchet")
                sleep(2)
            if "sell" in customer and "armour" in customer and (armour > 0):
                armour-=1
                money+=25
                items.update({"armour":armour})
                if armour==0:
                    items.pop("armour")
                print("Sold an armour")
                sleep(2)
            if "sell" in customer and "machete" in customer and (machete > 0):
                machete-=1
                money+=50
                items.update({"machete":machete})
                if machete==0:
                    items.pop("machete")
                print("Sold a machete")
                sleep(2)

            #buy
            if "buy" in customer and "fruit" in customer and money >= 2:
                money-=2
                fruits+=1
                items.update({"fruit":fruits})
                print(f"Bought a fruit")
                sleep(2)
            if "buy" in customer and "mushroom" in customer and money >= 10:
                money-=10
                mushroom+=1
                items.update({"mushroom":mushroom})
                print(f"Bought a mushroom")
                sleep(2)
            if "buy" in customer and "armour" in customer and money >= 50:
                money-=50
                armour+=1
                items.update({"armour":armour})
                print(f"Bought an armour")
                sleep(2)
            if "buy" in customer and "hatchet" in customer and money >= 20:
                money-=20
                hatchet+=1
                items.update({"hatchet":hatchet})
                print(f"Bought a hatchet")
                sleep(2)
            if "buy" in customer and "machete" in customer and money >= 50:
                money-=100
                machete+=1
                items.update({"machete":machete})
                print(f"Bought a machete")
                sleep(2)
            if "buy" in customer and "mysterious object" in customer and money >= 1000:
                money-=1000
                machete+=1
                items.update({"mysterious object":1})
                print(f"Bought a mysterious object")
                sleep(2)


    elif CurrentLocation == "infirmary" and "engage" in user and "doctor" in user:
        health=100
        status="Execellent"
        print("You are healed.")
        sleep(2)
    
    elif CurrentLocation == "casino" and "dealer" in user and "engage" in user:
        while customer != "exit":

            os.system("clear")
            print(f"Your money: {money}\n")
            customer=input("In this Casino, you will decide whether the sum of the two dice will be odd or even. \nIf your answer is correct, your betting amount will be doubled. \nIf not, you will lose your betting amount. \nTo play, type in 'let's roll', if not type 'exit'\n")
            if customer=="exit":
                break

            if "let" and "roll" in customer:
                betting_amount=0
                betting_amount=int(input("How much money would you like bet today?\n"))
                while betting_amount > money:
                    betting_amount=int(input(f"Please bet an amount equal or less than you currently have.\nYou currently have {money}."))

            even_or_odd= input("Is your luck on 'even' or 'odd' today?\n")

            customer= input("Type 'roll' to roll the die once\n")

            if customer == "roll":
                die_value_1=0
                die_value_1=(random.randint(1, 6))
                print(die_value_1)
            
            customer= input("Type 'roll' to roll the die again\n")

            if customer == "roll":
                die_value_2=0
                die_value_2=(random.randint(1, 6))
                print(die_value_2)
            if (die_value_1 + die_value_2)%2==0 and even_or_odd=="even":
                betting_amount = betting_amount*10
                money+=betting_amount
                print(f"You have won! Your betting amount becomes {betting_amount}")
                sleep(2)
            elif (die_value_1 + die_value_2)%2==0 and even_or_odd=="odd":
                betting_amount = betting_amount/2
                money-=betting_amount
                print("You have lost Your betting amount becomes {betting_amount} :( ")
                sleep(2)
            elif (die_value_1 + die_value_2)%2==1 and even_or_odd=="odd":
                betting_amount = betting_amount*10
                money+=betting_amount
                print(f"You have won! Your betting amount becomes {betting_amount}")
                sleep(2)
            elif (die_value_1 + die_value_2)%2==1 and even_or_odd=="even":
                betting_amount = betting_amount/2
                money-=betting_amount
                print("You have lost Your betting amount becomes {betting_amount} :(")
                sleep(2)



    #deserted house purchase
    elif CurrentLocation == "deserted house" and "purchase" in user and "deserted house" in user:
        purchase=input("Purchase this house? (yes/no)")
        if purchase=="yes" and money>= 10000:
            os.system("clear")
            print("Congretulations!\nYou have purchased this house.\nYou decide that it does not matter what happened in the past.\nYou decide to move on and make a start a new life here in this small town.")
            sleep(2)
            question=input("\nYou would move on? (yes/no)\n")
            if question == "yes":
                print("Good bye and thanks for playing! - Richard Noh")
                sleep(3)
                sys.exit()
            elif question=="no":
                print("You decide you need to do something more")
                sleep(2)
        if purchase=="yes" and money < 10000:
            print("Insufficient fund.")
            sleep(2)
        



    #navigation
    elif "goto" in user:
        if "deeper forest" in user and CurrentLocation =="forest":
            LocationID = 0
        elif "forest" in user and "deeper" not in user and (CurrentLocation == "deeper forest" or CurrentLocation=="road"):
            LocationID = 1
        elif "road" in user and (CurrentLocation=="forest" or CurrentLocation=="town"):
            LocationID = 2
        elif "town" in user and (CurrentLocation=="road" or CurrentLocation=="infirmary" or CurrentLocation=="store" or CurrentLocation=="casino"):
            LocationID = 3
        elif "infirmary" in user and CurrentLocation=="town":
            LocationID = 4
        elif "store" in user and CurrentLocation=="town":
            LocationID = 5
        elif "casino" in user and CurrentLocation=="town":
            LocationID = 6
        elif "deserted house" in user and CurrentLocation=="town":
            LocationID = 7
        else:
            print("Invalid location")
            sleep(2)

    else:
        if user=="exit game":
            os.system("clear")
            print("Thanks for playing 'You Wake Up Alone In A Forest' - Richard Noh")
            sleep(3)
            sys.exit()
        print("Invalid command")
        sleep(2)

    action = display.location[LocationID]["action"]
    interact = display.location[LocationID]["Interactable"]
    CurrentLocation = display.location[LocationID]["name"]
    CanGoTo = display.location[LocationID]["CanGoTo"]
    picture = display.location[LocationID]["draw"]

    os.system("clear")
    display.tophud(CurrentLocation,CanGoTo)
    print(picture)
    display.downhud(items,action,health,status,money,interact)



