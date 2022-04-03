name = input("enter name: ")
date = input("enter date: ")
print("\n")
letter = '''Dear <|NAME|>,

You are selected!

<|DATE|>'''

letter = letter.replace("<|NAME|>",name) 
letter = letter.replace("<|DATE|>",date)
print(letter)