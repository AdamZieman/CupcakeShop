# Adam Zieman
#
# CupcakeShop.py
# Completed: 5/9/2021
#
# Program Description: Simular to a cash register, a user will input the quantity of items wished
# to be purchased. The program will output the reciept: quantity of items (along with an image
# to the amount of items purchase); the sale price; a farewell.

# printHeading()
# print statements used as a heading for the program when executed
def printHeading():
    print("Welcome to the Cupcake Shoppe!")
    print("As a small shop, orders per customer are limited:")
    print("Each customer can order up to 3 cupcakes")
    print("and up to 6 cups of coffee.")
    print()
    print("You will be asked for number of cups of coffee first,")
    print("then number of cupcakes.")
    print("Each cup of coffee costs $2 and each cupcake $1.75.")
    print("Your bill will be printed at the end.")
    print("#####################################################")


# getCount(item,maxToOrder)
# asks the user for a quantity within limitations
def getCount(item,maxToOrder):
    # user inputs how many <item> they would like and saves it in <order>
    print("How many " + item + " do you wish to order? ", end="")
    order = int(input())

    # sets <order> to zero if input is a negative integer
    if order < 0:
        print("Sorry, you cannot order a negative amount!")
        print("We will assume 0.")
        order = 0
    # set <order> to the max amount of <items> available to be purchased
    elif order > maxToOrder:
        print("Sorry, you can only order up to " + str(maxToOrder) + ".")
        print("We will prepare " + str(maxToOrder) + " for you.")
        order = maxToOrder

    # outputs <order>
    return order


# calculateBill(coffees,cupcakes)
# Tells the user their purchased quantity with a respective amount of drawings
# Calculates the final sale price
def calculateBill(coffees,cupcakes):
    print("Your order:")

    # COFFEE SECTION
    # runs only if the user purchased coffee
    if coffees > 0:
        # prints the numeric value to the amount of coffees purchased
        # followed by the singular or plural tense of coffee
        print(coffees, end="")
        if coffees == 1:
            print(" coffee")
        else:
            print(" coffees")
            
        # draws a coffee cup image for the amount of coffees purchased
        for coffeeRepeat in range(coffees):
            drawCoffee()

    # thin-line to seperate coffee section from cupcake section
    print("----------------")
    
    # CUPCAKE SECTION
    # runs only if the user purchased cupcakes
    if cupcakes > 0:
        # prints the numeric value to the amount of cupcakes purchased
        # followed by the singular or plural tense of cupcake
        print(cupcakes, end="")
        if cupcakes == 1:
            print(" cupcake")
        else:
            print(" cupcakes")
        
        # draws a decorated cupcake image for the amount of cupcakes purchased
        for cupcakeRepeat in range(cupcakes):
            drawCupcake()

    # thick-line to seperate cupcake section from sale section
    print("=========================")

    # SALE SECTION
    # Calculate and prints the total sale price
    # total = [(price of ordered coffees) + (price of ordered cupcakes)] * (price after sales tax)
    total = round(((coffees * 2) + (cupcakes * 1.75)) * 1.055, 2)
    print("Your total is $", total, sep="")

    # farewell
    print("Enjoy your treats!")


# drawCoffee()
# Coffee Image
def drawCoffee():
    print(" .-'---------|")
    print("( C *********|")
    print(" '-.*********|")
    print("   '_________'")
    print("    '-------'")


# drawCupcake()
# Cupcake Image
def drawCupcake():
    print("   .--@@@--._")
    print("  ^-' *~-'@ ^.")
    print(" @@ . @ . ~ @")
    print(" \ ~  ^  @ @_/")
    print("[***-*-*-*-***]")
    print(" \| | | | | |/")
    print("  \ | | | | /")
    print("   ---===---")


# main()
def main():
    # print heading to start the program
    printHeading()

    # ask for number of each item to order, specifying item and maximum
    numCoffees = getCount("cups of coffee",6)
    numCupcakes = getCount("cupcakes",3)    

    # dividing line between ordering and printing bill
    print("=====================================")

    # calculate and print bill including visuals of items ordered
    calculateBill(numCoffees,numCupcakes)
    
main()

