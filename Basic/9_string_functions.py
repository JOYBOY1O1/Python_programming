story = "Hello my name is Joy"

print("\nlength of the story len(story) = ",len(story))
print("\n")

print('story.endswith("joy") = ',story.endswith("joy")) # False becuase J is capital in story
print("\n")

print('story.count("o") = ',story.count("o"))
print("\n")

print(story.capitalize()) #makes first letter of first word capital
print("\n")

print(story.find("Joy"))#finds the first occurance of your word
print("\n")

print(story.replace("Joy","Joy khulbe")) # will replace every joy from story