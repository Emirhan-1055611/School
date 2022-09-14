#Les 3

from re import L


age_str = input("What is your age? ")
print(f"Your age is {age_str}")

#

connection_choice_str = input("Welke verbinding wilt U gebruiken [4G, 5G, Wifi open]: ")

connection_choice = connection_choice_str.upper()

if connection_choice == "4G":
    print(f"U bent verbonden via {connection_choice}")
elif connection_choice == "5G":
    print(f"U bent verbonden via {connection_choice}")
elif connection_choice == "WIFI OPEN":
    print(f"U heeft de voor de Wifi open gekozen, wij wijzen u erop dat de data door de eigenaar van dit netwerk is te lezen.")
    answer_str = input("Wilt u nog steeds een verbinding maken? [ja/nee]")
    answer = answer_str.upper()
    if answer == "JA":
        print(f"U bent verbonden via {connection_choice}!")
    else:
        print("U bent niet verbonden!")
else:
    print("Onbekende invoer, er wordt geen verbinding tot stand gebracht.")

#

print("Is Hello with a capital 'H' within the string 'Hello, everyone!'")
if "Hello" in "Hello, everyone!":
    print("Yes, Hello is within the 'Hello everyone!' string")

print("Is Hello with a lower case 'h' within the string 'Hello, everyone!'")
if "hello" in "Hello, everyone!":
    print("Yes, hello is within the 'Hello, everyone!' string.")
else:
    print("No, hello with small letters is not within the string.")

#

print("Patient exposed to TB")

adult_child = input("Adult of Child? ")
adult_child_input = adult_child.upper()

if adult_child_input == "ADULT":
    common_TB = input("Has common TB symtoms? ")
    common_TB_input = common_TB.upper()

    if common_TB_input == "YES":
        print("Have patient report back if unwell; return in 1 month for checkup. ")
    elif common_TB_input == "NO":
        print("Treat likely TB patient and perform full TB exam. ")
    else:
        print("Unknown Input")
elif adult_child_input == "CHILD":
    can_give_test = input("Can TB test be given? [Yes/No] ")
    can_give_test_input = can_give_test.upper()

    if can_give_test_input == "YES":
        print("Administer TB test")
        print("Assess TB test results and child's condition")
    elif can_give_test_input == "NO":
        child_well = input("Child Well? [Yes/No] ")
        child_well_input = child_well.upper()

        if child_well_input == "YES":
            print("6 months preventive isonizaid")
            print("Have parent bring in if child shows any symptoms")
        elif child_well_input == "NO":
            print("Take fulle history. Examine for TB")
            print("If TB likely diagnosis treat for TB")
            print("If other diagnosis more likely, treat as needed and watch for TB symptoms")
        else:
            input("Unkown Input")
    else:
        input("Unkown Input")
else:
    input("Unkown Input")
#

print("Shopping Cart")

payment_method = input("Payment Method [Online/Offline] ")

payment_input = payment_method.upper()

if payment_input == "ONLINE":
    print("Place Purchase Order")

    is_admin_user = input("Admin User? [Yes/No] ")

    is_admin_input = is_admin_user.upper()

    if is_admin_input == "YES":
        print("Enter Payment Details.")
        print("Place Order")
    elif is_admin_input == "NO":
        approval_rules = input("Approval Rules [Approved/Rejected] ")
        approval_rules_input = approval_rules.upper()

        if approval_rules_input == "APPROVED":
            print("Enter Payment Details.")
            print("Place Order")
        elif approval_rules_input == "REJECTED":
            print("Purchase Order Rejected")
        else:
            print("Unknown input")


elif payment_input == "OFFLINE":
    print("Place Purchase Order")
    
    is_admin_user = input("Admin User? [Yes/No] ")

    is_admin_input = is_admin_user.upper()

    if is_admin_input == "YES":
        print("Order Created Automatically")
    elif is_admin_input == "NO":
        approval_rules = input("Approval Rules [Approved/Rejected] ")
        approval_rules_input = approval_rules.upper()

        if approval_rules_input == "APPROVED":
            print("Order Created Automatically")
        elif approval_rules_input == "REJECTED":
            print("Purchase Order Rejected")
        else:
            print("Unknown input")

else:
    print("Unknown Payment Method")

#

opeten_meenemen = input("Hier opeten of meenemen? ")
opeten_meenemen_input = opeten_meenemen.upper()

print(opeten_meenemen_input)

burgers_drankjes = input("Burgers of drankjes? ")
burgers_drankjes_input = burgers_drankjes.upper()

if burgers_drankjes_input == "BURGERS":
    burger_keuze = input("Wat voor burger? [Hamburger/Cheese Burger/Big Mac/Quarter Pounder] ")
    burger_keuze_input = burger_keuze.upper()

    if burger_keuze_input == "QUARTER POUNDER":
        quarter_pounder_keuze = input("Quarter Pounder met of zonder kaas? [Met/Zonder] ")
        quarter_pounder_keuze_input = quarter_pounder_keuze.upper()

        if quarter_pounder_keuze_input == "MET":
            burger_keuze = "Quarter Pounder met kaas"
        elif quarter_pounder_keuze_input == "ZONDER":
            burger_keuze = "Quarter Pounder zonder kaas"
        else:
            print("Unknown Input")

        burger_keuze_input = burger_keuze.upper()
        print(burger_keuze_input)

elif burgers_drankjes_input == "DRANKJES":
    drankjes_keuze = input("Warme of koude drankjes? ")
    drankjes_keuze_input = drankjes_keuze.upper()

    if drankjes_keuze_input == "WARME":
        drankje = input("Wat voor warme drankje? [Koffie/Cappucino/Chocolademelk] ")
        drankje_input = drankje.upper()
        print(drankje_input)
    elif drankjes_keuze_input == "KOUDE":
        drankje = input("Wat voor koude drankje? [Coca Cola/Cola Zero/7-up/Fanta/Fristi] ")
        drankje_input = drankje.upper()
        print(drankje_input)
    else:
        print("Unknown Input")
else:
    print("Unknown Input")