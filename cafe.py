
Done = True
number_order = 0
hot = 0
ice = 0
frappe = 0

while Done:
    print("="*25)
    print("\tDrinks menu\t")
    print("="*25)
    
    print("| 0. Quit\t\t|")
    print("| 1. Hot Coffee\t\t|")
    print("| 2. Ice Coffee\t\t|")
    print("| 3. Frappe Coffee\t|")
    print("| 4. Caculate Cost\t|")

    select_item = int(input("Select Item : "))
    if select_item == 0:
        print("Quit")
        Done = False             

    elif select_item == 1:
        hot = int(input("Hot Coffee, how many glasses : "))
        

    elif select_item == 2:
        ice = int(input("Ice Coffee, how many glasses : "))

    elif select_item == 3:
        frappe = int(input("Frappe Coffee, how many glasses : "))

    if  select_item == 4:
        hot_price = 35
        ice_price = 50
        frappe_price = 60
        number_order += 1

        price_1 = hot_price * hot
        price_2 = ice_price * ice
        price_3 = frappe_price * frappe

        print()
        print(f"Order #{number_order}")
        print("-"*40)
        print(f"Qty Item\t\tPrice\tTotal")
        print("-"*40)

        if hot > 0:
            print(f"{hot} Hot Coffee\t\t35.00\t{price_1:.2f}")
        if ice > 0:
            print(f"{ice} Ice Coffee\t\t50.00\t{price_2:.2f}")
        if frappe > 0:
            print(f"{frappe} Frappe Coffee\t\t60.00\t{price_3:.2f}")
        
        print("-"*40)
        print(f"Total : {price_1 + price_2 +price_3 :.2f} Bath")
