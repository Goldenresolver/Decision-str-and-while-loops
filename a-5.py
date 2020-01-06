#Jason Polanco
#assignment 4
#11/6/19
#A program that allos user to choose from a menu
# until he/she decides to exit
#program should keep a running total of the charges
# add 6% sales to calculate the final bill
# display the total to the user


#define main

def main():
# declare and intialize variables
# Use constants for menu choices
    PIZZA= 6.00
    PRETZEL=2.50
    CHIPS=1.25
    HOTDOG=3.75
    EXIT=""
    total=0

    SALESTAX= 0.6
    
    userInput = 0
    option_1=int(1)
    option_2=int(2)
    option_3=int(3)
    option_4=int(4)
    option_5=int(5)

# intro
    print("Welcome to the Seahawk Snack Bar menu!\n")

    # Use a while loop to repeat menu and set a condition
    # to ask allow user to exit out of loop

    while  userInput != 5:
        # Use a try and except to prevent user from using invaild inputs
        try:
                
            print("""\nPlease choose from the following menu:
                1)Personal Pizza $6.00
                2)Pretzel $2.50
                3)Chips $1.25
                4)Hot Dog $3.75
                5)Exit""")

            # Prompt user input for choices 1 and 2
            userInput= int(input("\nPlease enter your choice: "))
              #Use a while loop for Input validation:
            #The user must choose a valid choice from the menu a choice between 1 thru 5   
            while userInput < 0 or userInput > 5:
                    print("\nNumber invalid, try again, enter between 1-5")
                    print("""\nPlease choose from the following menu:
                    1)Personal Pizza $6.00
                    2)Pretzel $2.50
                    3)Chips $1.25
                    4)Hot Dog $3.75
                    5)Exit""")
                    # If user selects a number outside of the choices
                    #prompt again to reenter choice.
                    option_0= int(input("\nPlease enter your choice: "))
            
        #Use conditional statments with userinput variable to
        # to set conditions based on menu options
        # Once conditions are set, do something( examples, display, calculate, etc)
            if userInput== option_1:
                # use an accumlator variable to total up the menu prices
                total+= PIZZA
                
                #Display accumlator to user, along with the $ symbol
                # to show user the price of the item
                
                print("\nCurrent Total:","$%.2f"%total)

            elif userInput== option_2:

                # use an accumlator variable to total up the menu prices
                #  to keep a running total of the charges
                total+= PRETZEL

                #Display accumlator to user, along with the $ symbol
                # display user the price of the item 
                print("\nCurrent Total:","$%.2f"%total)

                
              #Use conditional statments with userinput variable to
        # to set conditions based on menu options
        # Once conditions are set, do something( examples, display, calculate, etc)    

            elif userInput== option_3:
                
                # use an accumlator variable to total up the menu prices
                #  to keep a running total of the charges
                total+= CHIPS

                #Display accumlator to user, along with the $ symbol
                # display user the price of the item 
                print("\nCurrent Total:","$%.2f"%total)

               
              #Use conditional statments with userinput variable to
        # to set conditions based on menu options
        # Once conditions are set, do something( examples, display, calculate, etc)    
            elif userInput== option_4:
                
                # use an accumlator variable to total up the menu prices
                #  to keep a running total of the charges
                total+= HOTDOG

                #Display accumlator to user, along with the $ symbol
                # display user the price of the item 
                print("\nCurrent Total:","$%.2f"%total)


        #Use conditional statments with userinput variable to
        # to set conditions based on menu options
        # Once conditions are set, do something( examples, display, calculate, etc)
        # This is the exit of the conditional statments
        # display total to user along with sales tax
        
            else:
                print("\nCurrent total:","$%.2f"%total)

                print("\nSales Tax:","$%.2f"%SALESTAX)
                #Mutiply final total bill with sales tax
                # To add that number to final bill
                totalTax= total*SALESTAX

                #add 6% sales to calculate the final bill
                totalwithTax=totalTax+total

                 #display total to user along with sales tax and $ symbol
                print("\nTotal Bill inculding sales Tax:","$%.2f"%totalwithTax)

                #Outro
                print("\nHave a wonderful day!")

# Use a try and except to prevent user from using invaild inputs
# Display to user the error message and restart program
        except ValueError:
            print("\nInput not vaild")
            
                

main()



    


              
            
