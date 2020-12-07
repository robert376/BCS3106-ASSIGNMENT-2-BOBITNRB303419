print("\n" * 5)                  

import datetime                    #SHOW THE  Real Date data andinformation.
import os                          #OS checking the OS best compatibility

foodlist = []                    #Variable  both  foodlist, drinklist names + prices.
drinklist = []              

pricelist = [0] * 100        #Variable for pricelist
                                  
                     
var_commission_2 = 200                                  
vardiscount2 = 0.20                
 

navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" # making theprogram runnable on Windows


def def_default():
    global  foodlist,drinklist,orderlist, pricelist     
    orderlist = [0] * 100                 
def_default()                                      
                                                   


def defmain():
    while True : #menu is repeated
        print("*" * 31 + "RESTAURANT ORDERING SYSTEM MENU" + "*" * 32 + "\n"     #Design of restaurant ordering ordering system menu.
              "\t(O) ORDER\n"                      
              "\t(P) PAYMENT\n"
              "\t(C) CANCEL\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        inputx = str(input("Select Your Operation: ")).upper()    
        if (len(inputx) == 1):                                           
            if (inputx == 'O'):                                          
                print("\n" * 10)                                         
                def_ordermenu()                                         
                break                                                     
                                                 
            elif (inputx == 'P'):                                        
                print("\n" * 10)                                         
                def_payment()                                             
                break
            elif (inputx == 'C'):
               print ("*" * 32 + "CANCEL THE ORDER" + "*" * 31 + "\n")
               break                                                           
            elif (inputx == 'E'):                                        
                print("*" * 32 + "THANK YOU,WELCOME" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                               
                print("\n" * 10 + "ERROR: WRONG Input (" + str(inputx) + "). Try again!")     
        else:                                                                                     
            print("\n" * 10 + "ERROR: WRONG Input (" + str(inputx) + "). Try again!")         

def def_ordermenu():                                                                            
    while True:                                             
        print("*" * 31 + "ORDER MENU PAGE" + "*" * 31 + "\n"     
              "\t(F) FOODS AND DRINKS\n"
              "\t(R) RESTAURANT ORDERING SYSTEM MENU\n"
              "\t(C) CANCEL\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input(" Select Your Operation: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 10)
                def_food_drink_order() 
                break
            elif (input_1 == 'R'):
                print("\n" * 10)
                defmain() 
                break
            elif (input_1 == 'C'):
                 print("*" * 32 + "CANCEL THE ORDER" + "*" * 31 + "\n")
                 break

            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU,WELCOME" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 10 + "ERROR: WRONG Input (" + str(inputy) + "). Try again!")  
        else:
            print("\n" * 10 + "ERROR: WRONG Input (" + str(inputy) + "). Try again!")

def def_full_file_reader():                                                             
    file_foods = open('files'+navigator_symbol+'foodlist.fsd', 'r') #reading foodlist
    for i in file_foods: 
        foodlist.append(str(i.strip())) 
    file_foods.close()

    file_drinks = open('files'+navigator_symbol+'drinklist.fsd', 'r') #reading drinklist
    for i in file_drinks:
        drinklist.append(str(i.strip()))
    file_drinks.close()


    i = 0
    while i <= (len(foodlist) - 1): 
        if 'MR' in foodlist[i]:
            foodlist[i] = str(foodlist[i][:foodlist[i].index('MR') - 1]) + ' ' * (20 - (foodlist[i].index('MR') - 1)) + str(foodlist[i][foodlist[i].index('MR'):])
        i += 1

    i = 0
    while i <= (len(drinklist) - 1):
        if 'MR' in drinklist[i]:
            drinklist[i] = str(drinklist[i][:drinklist[i].index('MR') - 1]) + ' ' * (20 - (drinklist[i].index('MR') - 1)) + str(drinklist[i][drinklist[i].index('MR'):])
        i += 1
def_full_file_reader()

def def_file_sorter(): 
    global foodlist, drinklist
    foodlist = sorted(foodlist)
    drinklist = sorted(drinklist)
    
    i = 0
    while i < len(foodlist):
        pricelist[i] = float(foodlist[i][int(foodlist[i].index("MR") + 3):]) 
        i += 1

    i = 0
    while i < len(drinklist):
        pricelist[40 + i] = float(drinklist[i][int(drinklist[i].index("MR") + 3):]) 
        i += 1

    i = 0
   
def_file_sorter()

def def_food_drink_order():
    while True:
            print("*" * 26 + "ORDER FOODS & DRINKS" + "*" * 20)
            print(" |NO| |FOOD NAME|         |PRICE|   |  |NO| |DRINK NAME|        |PRICE|")

            i = 0
            while i < len(foodlist) or i < len(drinklist):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(foodlist):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(foodlist[i]) + "  | " 
                else:
                    food = " " * 40 + "| " 
                if i < len(drinklist):
                    drink = "(" + str(41 + i) + ")" + " " + str(drinklist[i])
                else:
                    drink = ""
                print(food, drink)
                i += 1

            print("\n (R) RESTAURANT ORDERING SYSTEM MENU                 (P) PAYMENT             (C)CANCEL          (E) EXIT\n" + "_" * 72)

            input_1 = input("Select Your Operation: ").upper() 
            if (input_1 == 'R'):
                print("\n" * 10)
                defmain() 
                break
            if (input_1 == 'C'):
                print("*" * 32 + "CANCEL THE ORDER" + "*" * 31 + "\n")
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU,WELCOME" + "*" * 31 + "\n") # says Exit and prints thank you
                break
            if (input_1 == 'P'):
                print("\n" * 10)
                def_payment() 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(foodlist) and int(input_1) > 0) or (int(input_1) <= len(drinklist) + 40 and int(input_1) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(foodlist[int(input_1) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(drinklist[int(input_1) - 41])) 
                     except:
                        pass

                     input_2 = input("How Many Do You Want to Order?: ").upper() 
                     if int(input_2) > 0:
                        orderlist[int(input_1) - 1] += int(input_2)
                        print("\n" * 10)
                        print("Success Ordered!")
                        def_food_drink_order() 
                        break
                     else:
                        print("\n" * 10 + "ERROR: Invalid Input (" + str(input_2) + "). Try again!")
            except:
                print("\n" * 10 + "ERROR: Invalid Input (" + str(input_1) + "). Try again!")



def def_payment():
    while True:
        print("*" * 32 + "PAYMENT" + "*" * 33 + "\n") 
        total_price = 0 

        report_new = "\n\n\n" + " " * 17 + "*" * 35 + "\n" + " " * 17 + "DATE: " + str(datetime.datetime.now())[:19] + "\n" + " " * 17 + "-" * 35 
        i = 0
        while i < len(orderlist):
            if(orderlist[i] != 0):
                if (i >= 0) and (i < 40):
                    report_new += "\n" + " " * 17 + str(foodlist[i]) + "  x  " + str(orderlist[i]) 
                    print(" " * 17 + str(foodlist[i]) + "  x  " + str(orderlist[i])) 
                    total_price += pricelist[i] * orderlist[i] 
                if (i >= 40) and (i < 80):
                    report_new += "\n" + " " * 17 + str(drinklist[i - 40]) + "  x  " + str(orderlist[i])
                    print(" " * 17 + str(drinklist[i - 40]) + "   x  " + str(orderlist[i]))
                    total_price += pricelist[i] * orderlist[i] 
                
                i += 1
            else:
                i += 1
        if total_price > var_commission_2:
            total_price -= total_price * vardiscount2 
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "DISCOUNT:      % " + str(vardiscount2 * 100) + "\n" \
                "" + " " * 17 + "DISCOUNT AMOUNTS:   MR " + str(round(total_price * vardiscount2, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "TOTAL PRICES:       MR " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "DISCOUNT:      % " + str(vardiscount2 * 100) + "\n"
                "" + " " * 17 + "DISCOUNT AMOUNTS:   MR " + str(round(total_price * vardiscount2, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "TOTAL PRICES:       MR " + str(round(total_price, 2)))      
        else:
            report_new += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       MR " + str(round(total_price, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "TOTAL PRICES:       MR " + str(round(total_price, 2)))

            print("\n (P) PAY           (R) RESTAURANT ORDERING SYSTEM MENU          (E) EXIT\n" + "_" * 72)                 
       
        input_1 = str(input("Select Your Operation: ")).upper()
        if (input_1 == 'P'):
            print("\n" * 10)
            print("Successfully Paid,THANK YOU!")
            def_default() 
        elif (input_1 == 'R'):
            print("\n" * 10)
            defmain()
            break
        elif ('E' in input_1) or ('e' in input_1):
            print("*" * 32 + "THANK YOU,WELCOME" + "*" * 31 + "\n")
            break
        else:
            print("\n" * 10 + "ERROR: WRONG Input (" + str(input_1) + "). Try again!")
defmain() # Execute the restaurant ordering system
