# Assignment
# Instructions
# For this assignment, you will implement a program that asks the user for a series of words and 
#then displays the story with the user's words inserted into the appropriate places.

# The program should begin by asking the user for each of the words. It should then, fill those words 
#into the appropriate places in the story.

# To begin, please use the following story:

# The other day, I was really in trouble. It all started when I saw a very
# [adjective] [animal] [verb] down the hallway. "[exclamation]!" I yelled. But all
# I could think to do was to [verb] over and over. Miraculously,
# that caused it to stop, but not before it tried to [verb]
# right in front of my family.

# Make sure to match the punctuation and spacing of the original story exactly (for example, you should not 
#put your words on their own line, they should fit naturally into the story).

# Also, make it so that the "exclamation" word is automatically capitalized, because it starts a new sentence.

adjective = "huge"
animal = "racoon"
verb = "run"
exclamation = input("type the exclamation here:")
verb_1 = "kick"
verb_2 = "attack me"
output = ("The other day,I was really in trouble.It all started when I saw a very " + 
adjective + " " + animal + " " + verb + "down the hallway. " +  " " + 
exclamation.upper() + "! " + "I yelled. But all I could think to do was to " + verb_1 + " " + "over and over. Miraculously, that caused it to stop, but not before it tried to " +
verb_2 + " " + "right in front of my family.")
print(output)

# ("The other day, I was really in trouble. It all started when I saw a very " +
# adjective + " " + animal + " " + verb + " down the hallway. " +
# exclamation.upper() + "! " +
# "I yelled. But all I could think to do was to " + verb_1 + " over and over. " +
# "Miraculously, that caused it to stop, but not before it tried to " + verb_2 +
# " right in front of my family.")

# ambush = "shout"
# output = ("I was happy so I " + ambush.upper() + str("!"))
# print(output)