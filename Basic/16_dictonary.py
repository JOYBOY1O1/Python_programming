my_dictonary = { 
    "key":"value",
    "joy":"student",
    "marks":"6969",
    "roll no":"20011463",
    "another dictonary":{'joy':'boy'},
               }
#cannot have duplicate entries
print("\n")

print(my_dictonary.keys())
print(my_dictonary.values())
print(my_dictonary.items())
print(type(my_dictonary))
#type casting of keys: print(list(my_dictonary))

update_dictonary ={"Valo": "Game",
                   "Csjo": "Game"}

my_dictonary.update(update_dictonary)
print(my_dictonary)
print("\n")
print(my_dictonary.get("joy"))
print(my_dictonary["joy"])
print("\n")
print(my_dictonary.get("joy2")) #returns none as joy2 is not  present
print(my_dictonary["joy2"])  #returns an error as joy2 is not  present