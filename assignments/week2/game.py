def game():   
 #imports
    import time,os,sys
    import random


    def typingPrint(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    
    def typingInput(text):
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
        value = input()  
        return value  
    
    def clearScreen():
        os.system("clear")
    #welcome and ask for name
    typingPrint("Welcome to Game \n")
    name = str(typingInput("please enter your name: "))

    #story introduction
    typingPrint("You have woken up in a little hut in the middle of a forest. Before you leave the house you remeber the dangers of the world outside so you decide to take a weaopn with you.\n")

    #first desicion wand
    def weapon_choice():
        typingPrint("Which weapon will you choose? \n")

        print(" [1]\n"     
        "            _\n"
        " _         | |\n"
        "| | _______| |---------------------------------------------\ \n"
        "|:-)_______|==[]============================================> \n"
        "|_|        | |---------------------------------------------/ \n"
        "           |_|\n")

        time.sleep(1)

        print(" [2] \n" 
        "__/\__\n"
        "\    /\n"
        "/_  _\ \n"
        "XX\/XX\n"
        " X  X\n" 
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n"
        " X  X\n" 
        " X  X\n"
        " XXXX\n" 
        "X    X\n"
        " XXXX\n" )

        time.sleep(1)
        global weapon_hand
        try:
            weapon = int(typingInput("please enter 1 or 2: "))
            if weapon==1:
                weapon_hand="sword"
                typingPrint("You picked up the sword \n")
            elif weapon==2:
                weapon_hand="wand"
                typingPrint("You picked up the wand \n")
            else:
                typingPrint("Please enter either 1 or 2"), weapon_choice() #Ask again
        except ValueError:
            typingPrint("Please only enter numbers. You have the choice between 1 or 2.\n")
            weapon_choice() #Ask again

    weapon_choice()

    #defining fight mechenic

    def fighting():
        global enemy_health, enemy_name

        while enemy_health>0:
            if weapon_hand == "sword":
                typingInput("Describe your attack: ")
            else:
                typingInput("Name your spell: ")

            
                hit=random.randint(0,101)
                if hit<=20 and weapon_hand=="sword":
                    typingPrint("You bareley scratched"+ enemy_name)
                elif hit>=70 and weapon_hand=="sword":
                    typingPrint("You hit" + enemy_name +"'s weak spot")
                elif 20<=hit<=70 and weapon_hand=="sword":
                    typingPrint("Your attack on"+ enemy_name +"was succesful")
                elif hit<=20 and weapon_hand=="wand":
                    typingPrint("Your spell barley influenced"+ enemy_name +".")
                elif hit>=70 and weapon_hand=="wand":
                    typingPrint("Your spell was maginificent"+ enemy_name +"'s weak spot was hit. ")
                elif 20<=hit<=70 and weapon_hand=="wand":
                    typingPrint("Your spell on"+ enemy_name +"succesfully hit them")

                enemy_health-=hit
                typingPrint(" You dealt "+ str(hit) +" damage. Enemy health is now at "+ str(enemy_health) + ". \n" )
                time.sleep(1)
        else:
            typingPrint(" You have succesfully defeated"+ enemy_name)
            game_ending1()
    #
    def try_choice():
                    try:
                        try_again= int(typingInput("\n Do you want to\n [1] go home? \n [2] try fighting the ogre? \nPlease enter 1 or 2:"))
                        if try_again==1:
                                typingPrint("You go back to the hut put down your " +weapon_hand+ " and call it quits for today. \n" )
                                game_ending2()
                        elif try_again==2:
                                typingPrint("You turn around back over the bridge to attack the ogre")
                                fighting()
                        else:
                                    typingPrint("Please enter either 1 or 2."),try_choice()
                    except ValueError:
                        typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), try_choice()
    def try_choice2():
                    try:
                        try_again= int(typingInput("\nDo you want to\n[1] go home. \n[2] try fighting the unicorn. \n[3] try approching the unicorn again. \nPlease enter 1,2 or 3:"))
                        if try_again==1:
                                typingPrint("You go back to the hut put down your " +weapon_hand+ " and call it quits for today. \n" )
                                game_ending2()
                        elif try_again==2:
                                typingPrint("You turn around back throught the forest and attack the unicorn.")
                                fighting()
                        elif try_again==3:
                                typingPrint("You carefully approch the unicorn, but step on a twig. The unicorn, startled by the sound, runs away. ")
                                game_ending3()
                            
                        else:
                            typingPrint("Please enter either 1,2 or 3."),try_choice2()
                    except ValueError:
                        typingPrint("Please only enter numbers. You have the choice between 1,2 or 3. \n"), try_choice2()
    #define endings
    def game_ending1():
        typingPrint("after defeating "+enemy_name+ " you return home, exhausted from your long day. \n Thank you "+name+" for playing my game. Do you want to play again?\n")
        try:
            end_choice= int(typingInput("[1] Yes! \n[2] No!"))
            if end_choice==1:
                game()
            elif end_choice==2:
                typingPrint("Okay, Bye!")
                            
            else:
                typingPrint("Please enter either 1 or 2."),game_ending1()
        except ValueError:
                typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), game_ending1()

    def game_ending2():
        typingPrint("after returning home, frightend from your expiriences you lay down on your bed to rest. \n Thank you "+name+" for playing my game. Do you want to play again?\n")
        try:
            end_choice= int(typingInput("[1] Yes! \n[2] No!"))
            if end_choice==1:
                game()
            elif end_choice==2:
                typingPrint("Okay, Bye!")
                            
            else:
                typingPrint("Please enter either 1 or 2."),game_ending2()
        except ValueError:
                typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), game_ending2()
    def game_ending3():
        typingPrint("After failing to come closer to the unicorn, you return home dissapointed from your day. \n Thank you "+name+" for playing my game. Do you want to play again? \n ")
        try:
            end_choice= int(typingInput("[1] Yes! \n [2] No!"))
            if end_choice==1:
                game()
            elif end_choice==2:
                typingPrint("Okay, Bye!")
                            
            else:
                typingPrint("Please enter either 1 or 2."),game_ending3()
        except ValueError:
                typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), game_ending3()
    def game_ending4():
        typingPrint("After spending some time with the unicorn, it befriends you. What a blissful day! \n Thank you "+name+" for playing my game. Do you want to play again? \n ")
        try:
            end_choice= int(typingInput("[1] Yes! \n [2] No!"))
            if end_choice==1:
                game()
            elif end_choice==2:
                typingPrint("Okay, Bye!")
                            
            else:
                typingPrint("Please enter either 1 or 2."),game_ending4()
        except ValueError:
                typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), game_ending4()

    #second desicion where to go
    typingPrint("With your "+ weapon_hand +" in hand you leave the hut. Ready for adventure you following the only way leading away from your hut. After a little while the way splits into two.")
    def way_choice():
        global enemy_name
        global enemy_health
        typingPrint("\n[1] To your left is a clear sunny way with a bridge leading over a river \n"
        "[2] To your right the way leads into a bright forest with green trees ")
        time.sleep(1)
        try:
            way = int(typingInput("\nPlease enter 1 or 2: "))
            if way==1:
                enemy_name=" the ogre "
                enemy_health= 250
                typingPrint("You walk up to the bridge looking at the beautiful water. Suddenly a haggish ogre appears in front of you.")
                ogre_choice=typingInput(" Do you\n[1] Attack\n" \
                "[2] Flee\nPlease enter 1 or 2: ")
                try:
                    if int(ogre_choice)==1:
                        fighting()
                    elif int(ogre_choice)==2:
                        typingPrint("You run back over the bridge, towards your hut.")
                        try_choice()
                    else:
                        typingPrint("Please enter either 1 or 2."), way_choice()

                except ValueError:
                    typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), way_choice()

            
            elif way==2:
                enemy_name=" the unicorn "
                enemy_health= 100
                typingPrint("You enter the forest looking at the beautiful trees surrounding you. Suddenly you see a unicorn just a couple meters away from you. What do you do?")
                unicorn_choice=typingInput(" Do you\n[1] Attack the unicorn to harvest it's magnificent horn\n" \
                "[2] Flee\n[3] Carefully approch it. \nPlease enter 1, 2 or 3: ")
                try:
                    if int(unicorn_choice)==1:
                        fighting()
                    elif int(unicorn_choice)==2:
                        typingPrint("You run back through the forest, towards your hut.")
                        try_choice2()
                    elif int(unicorn_choice)==3:
                        typingPrint("You carefully approch the unicorn. Because of your carful steps the unicorn, doesnt get frightend. Once in reach you gently stroke it's back. The unicorn enjoys your presence")
                        game_ending4()
                    else:
                        typingPrint("Please enter either 1, 2 or 3."), way_choice()

                except ValueError:
                    typingPrint("Please only enter numbers. You have the choice between 1 or 2. \n"), way_choice()
            else:
                typingPrint("Please enter either 1 or 2"), way_choice()
        except ValueError:
            typingPrint("Please only enter numbers. You have the choice between 1 or 2.\n"), way_choice()
        
    way_choice()
        
game()
