# Write a program to find out whether a given post is talking about “sometimes” or not.
a = """Sometimes we want to play pubg on our phone if the day is Sunday.

Sometimes we order Ice-cream online if the day is sunny.

Sometimes we go hiking if our parents allow.

All these are decisions that depend on the condition being met."""

if("sometimes" in a):
    print("sometimes is present")
elif("Sometimes" in a):
    print("sometimes is present")
else:
    print("sometimes is not present")