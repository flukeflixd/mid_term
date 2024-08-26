n = 0
hot = ice = frap = 0
done = True
while done:
    print("="*25)
    print("\t Drinks menu\t")
    print("="*25)
    print("| 0. Quit\t\t|")
    print("| 1. Hot Coffee\t\t|")
    print("| 2. Ice Coffee\t\t|")
    print("| 3. Frappe Coffee\t|")
    print("| 4. Caculate Cost\t|")
    print("="*25)
    menu = input("Select Item : ")
    if menu == '0':
        done = False
    if menu == '1':
        hot = int(input("Hot Coffee, how many glasses : "))
    if menu == '2':
        ice = int(input("Ice Coffee, how many glasses : "))
    if menu == '3':
        frap = int(input("Frappe Coffee, how many glasses : "))
    if menu == '4':
            print()
            n += 1
            print(f"Order #{n}:")
            print("-"*30)
            print("Qty Item\tPrice   Total")
            print("-"*30)
            ph = hot * 30.00
            pi = ice * 50.00
            pf = frap * 60.00
            total = ph + pi + pf
            if hot > 0:
                print(f"{hot} Hot Coffee\t 35.00  %.2f"%ph)
            if ice > 0:
                print(f"{ice} Ice Coffee\t 50.00  %.2f"%pi)
            if frap > 0:
                print(f"{frap} Frappe Coffee\t 60.00  %.2f"%pf)
            print("-"*30)
            print(f"Total: %.2f"%total,"Bath")
            total = ph = pi = pf = hot = ice = frap = 0
            print()