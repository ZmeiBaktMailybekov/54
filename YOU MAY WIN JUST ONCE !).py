print "You are a boy :)" # game loading
print "One day you are going to the shop." # it is game loading too
print "There is just one shop in your town." # it is game loading again
print "You are walking on the street..." # when this f... game wil start?
print "And you came to the shop" # game beginnig... really?
print "is door #1 open or #2 close ???" # ok let's go!!!

door = raw_input("> ")
 
if door == "1":
    print "You are in shop/ What would you buy?" # you must choose one of options
    print "1. T-shirt"
    print "2. Ice-cream"
    print "3. Chocolate"
    print "4. Meat and vegetables"

    buy = raw_input("> ")

    if buy == "1":
        print "You bought a T-shirt and came home..."
        print "Your mother told you that you must buy another things!"
        print "You are going to the shop again"
        print "When you walked on the street..."
        print "... a car bits you!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
    elif buy == "2":
        print "You bought an ice-cream and came home..."
        print "Your mother told you that you must buy another things!"
        print "You are going to the shop again"
        print "When you walked on the street..."
        print "... a car bits you!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
    elif buy == "3":
        print "You bought a chocolate and came home..."
        print "Your mother told you that you must buy another things!"
        print "You are going to the shop again"
        print "When you walked on the street..."
        print "... a car bits you!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
    elif buy == "4":
        print "You bought meat and vegetables and came home..."
        print "Your mother made delicious dinner!"
        print "You had a dinner and went sleep"
        print " YOU ARE ALIVE! YOU WIN!" # you win but it is the end of the game
    else:
        print "You didn't open the door and went with friends to play soccer"
        print "But on your way became a lot of zombies"
        print "And they ate your brain!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game

elif door == "2":
    print "Shop is close/ what would you do?" # you must choose one of options
    print "1. Go home"
    print "2. Go to girlfriend"

    do = raw_input("> ")

    if do == "1":
        print "You went home and then you went to your girlfriend"
        print "When you walked on the street..."
        print "... a car bits you!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
    elif do == "2":
        print "On the way to your girlfriend..."
        print "... a car bits you!"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
    else:
        print "You went to play soccer with your friends"
        print "But there were a lot of zombies"
        print "And they ate your brain"
        print " YOU ARE DEAD! GAME OVER!" # the end of the game
else:
    print "You are standing in front of the shop and try to understand"
    print "What happened with shop"
    print "Because there is NO shop on the place where it was"
    print "And around you became a lot of zombies"
    print "And they ate your brain!"
    print " YOU ARE DEAD! GAME OVER!" # the end of the game