#Write a program to create a dictionary of Hindi words with values as their English translation. Provide the user with an option to look it up!

my_dict = {
    "pankha": "fan",
    "dabba" :"box",
    "vastu":"item"
}
print("options are:",my_dict.keys())
a = input("\nenter hindi word: ")
# print("The meaning of",a,"is",my_dict[a])

# below line will not get error if key is not present
print("The meaning of",a,"is",my_dict.get(a))