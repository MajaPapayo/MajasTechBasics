import random
import time

def print_animation(text_parts):
    text = "".join(str(part) for part in text_parts)
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()

#lists
flower_list=["🌷", "🌹", "🌻","🌼","🌸"]
food_list=["🍕","🌭","🍔","🍟","🍜"]
smileys_list=["😀","☺️","😗","😎","🤡"]

# Welcome and asking for the type of list
def game():
        #Intro
    print_animation ("Welcome to my Pattern maker, Let's start!")

    print_animation("What do you want to print?\n" \
        "[🌸] flowers\n" \
        "[🍜] food\n" \
        "[☺️ ] smileys \n")
       
    choice = str(input("Enter either flowers, food or smileys: "))

    try:
        if choice == "flowers":
            print_animation("Im sure they will smell wonderfull!")
        elif choice == "food":
            print_animation("Mhh Yummy!")
        elif choice == "smileys":
            print_animation("let's look at some faces o.o")
        else:
            print_animation("Please enter either flowers, food or smileys"), game()
    except ValueError:
        print_animation("Beep Boop Bap: SystemCrash! No just kidding, but please only enter either flowers, food or smileys"), game()

    #asking for width and height
    def width_and_height():
        global width
        global height
        try:    
            width = int(input("How wide should your pattern be? : "))
        except ValueError:
            print_animation("Beep Boop Bap: SystemCrash! No just kidding, but please only enter numbers"), width_and_height()

        try:
            height =int(input("How high should your pattern be? : "))
        except ValueError:
            print_animation("Beep Boop Bap: SystemCrash! No just kidding, but please only enter numbers. Now you have to entern width again :c"), width_and_height()
    width_and_height()

    #actually calculating
    for y in range (height):
        for x in range (width):
            if choice == "flowers":
                pattern=random.choice(flower_list)
                print(pattern, end=" ")
            elif choice == "food":
                pattern=random.choice(food_list)
                print(pattern, end=" ")
            elif choice == "smileys":
                pattern=random.choice(smileys_list)
                print(pattern, end=" ")
            else:
                print_animation("Please enter either flowers, food or smileys"), game()
        print()
        

    def end_game():
        try:
            end= str(input("So cute! You want to print another pattern :)? yes or no \nPlease enter either:"))

            if end=="yes":
                game()
            elif end=="no":
                print_animation("Thank you for printing ^^\nHave a loveley Day xoxo")
            else:
                print_animation("Please enter either yes or no"), end_game()  
        except ValueError:
            print_animation("Please enter either yes or no"), end_game()
    end_game()

game()


#flower ASCII art
# in the following you will see some beautiful flowers, which after many hours of trial and error I didnt manage to add the my flower maker :,)  
#        "  _,-._  \n",
#        " / \_/ \ \n",
#        " >-(_)-< \n",
#        " \_/ \_/ \n",
#        "   `-'   \n",
#        "  \ | /  \n",
#        "   \|/   \n"
#    
#    
#        "     _    \n",
#        "   '\ /'  \n",
#        "  < ~O~ > \n",
#        "   '/_\'  \n",
#        "   \ | /  \n",
#        "    \|/   \n"
#    
#        "       __/)  \n",
#        "    .-(__(=: \n",
#        " |\ |    \)  \n",
#        " \ ||        \n",
#        "  \||        \n",
#        "   \|        \n")