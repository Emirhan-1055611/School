from ast import Delete


games = ["Player’s Unknown Battle Ground (PUBG) 50 Million 2018",
"Fortnite Battle Royale 39 Million 2017",
"Apex Legends 50 Million (1 Month) 2019",
"Leauge of Legends (LOL) 27 Million 2009",
"Counter Strike; Global Offensive 32 Million 2014",
"Heartstone 29 Million 20120",
"Minecraft 91 Million 2011",
"DOTA 2 5 million 2015",
"The Division 2 N/A 2019",
"The Splatoon 2",]

#A

print("Nummer 5: ", games[4])

#B

print(f"Lengte van Game Nummer 7 ({games[6]}): ", len(games[6]))

#C

print(f"Er zitten ", len(games), " games in de lijst.")

#D

games.insert(1, "Snake")
print(games[1])

#E
print(games)
print("Helaas heeft de game ", games[10], " het niet gered om in de top 10 te blijven. We nemen waardig afscheid van ", games[10])
games.remove(games[10])

#F

index_heartstone = games.index("Heartstone 29 Million 20120")
games[index_heartstone] = "Heartstone 29 Million 2012"
print(games[index_heartstone])

##

computer_suppliers = ("Apple", 
"Asus", 
"Dell", 
"Lenovo",
"Acer",
"Samsung",
"MSI",
"Hewlett-Packard (HP)",
"Toshiba",
"Microsoft",
"Chuwi",
"Sony")

#A

print("De tuple bevat ", len(computer_suppliers), " computer leveranciers")

#B

computer_supplier = computer_suppliers[7]
characters_in_name = len(computer_supplier)
print(f"De naam van {computer_supplier} bestaat uit {characters_in_name} karakters.")
print(computer_suppliers)

#C

print(f"De computer leverancier op de 10e plek is {computer_suppliers[9]}")

###

phone_numbers = {"The Simpsons": "636-555-3226",
"Vegas Vacation": "555-0100",
"Ghostbusters": "555-23678",
"Billy Madison": "555-0840",
"Swingers": "213-555-4679",
"Bruce Almighty": "555-0123",
"Seinfeld": "555-FILK",
"Arrested Development": "555-0113",
"Die Hard With a Vengeance": "555-0001",
"The A-Team": "555-6162"}

#A

print({phone_numbers["Bruce Almighty"]})

#B

phone_numbers["Harry Potter"] = "605-475-6961"

#C

print("Oude Telefoonnummer Ghostbusters: ", phone_numbers["Ghostbusters"])
phone_numbers["Ghostbusters"] = "555-2368"
print("Nieuwe Telefoonnummer Ghostbusters: ", phone_numbers["Ghostbusters"])

#D
phone_numbers.pop("Seinfeld")
print("Telefoonnummer van Sienfeld is verwijderd.")

#E

print(f"In de dictionary zitten {len(phone_numbers)} telefoonnummers.")

