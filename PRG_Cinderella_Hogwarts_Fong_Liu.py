# PRG Inventory -- Fong Liu
# This program will create two inventories for my text-based adventure game.



# This inventory will list what clothes and accessories Cinderella needs
# In order to look like a princess.
princess_items = ['glass slippers', 'blue dress', 'gloves']
print(princess_items)
print(f"The fairy godmother moved her wand. Cinderella is now wearing"
      f" a pair of beautiful {princess_items[0]}!")
print(f"The fairy godmother moved her wand again. Cinderella is now"
      f" wearing a sparkling {princess_items[1]}!")
print(f"The fairy godmother moved her wand once more. Cinderella is"
      f" now wearing a pair of elegant {princess_items[2]}!\n")

# Insert item: headband.
princess_items.insert(0, 'headband')
print(princess_items)
print(f"Oh, I forgot to mention. The fairy godmother gives her a"
      f" speacial {princess_items[0]} first.\n")

# Append item: choker
princess_items.append('choker')
print(princess_items)
print(f"As Cinderella is about to head to the ball dance, the fairy "
      f"godmother gives her a {princess_items[4]} that makes her look "
      f"even more gorgeous!\n")

# Pop item: choker
popped_choker = princess_items.pop()
print(princess_items)
print(f"The midnight arrives, and Cinderella's {popped_choker} "
      f"disappears first!\n")

# Remove all items except for glass slippers.
princess_items.remove('headband')
princess_items.remove('blue dress')
princess_items.remove('gloves')
print(princess_items)
print(f"Cinderella speeds to her house, and once she gets home, "
      f"all the things the fairy godmother has given "
      f"her are slowly disappearing. However, one of her "
      f"{princess_items[0]} does not disappear.\n")

# Delete the last item: glass slippers.
del(princess_items[0])
print(princess_items)
print(f"She realizes this is because the prince has the other shoe. "
      f"So she goes to the prince asking for it, and prince tells her "
      f"how much he loves her. They live happily after, and "
      f"Cinderella's glass slippers disppear completely.\n\n\n")

# This inventory will list the four houses in Hogwarts school that will 
# be used by the giant in order to introduce Hogwarts to Harry Potter.
hogwarts_houses = ['Hufflepuff', 'Ravenclaw', 'Slytherin', 'Gryffindor']
print(hogwarts_houses, f"\n")

# The giant will first introduce the number of houses in Hogwarts school
# and what they are alphabetically.
print(len(hogwarts_houses))
print(sorted(hogwarts_houses))
print(hogwarts_houses)
print(f"The giant tells Harry Potter that there are "
      f"{len(hogwarts_houses)} houses in Hogwarts school. Then, he "
      f"lists them alphabetically: ", sorted(hogwarts_houses), f"\n")

# The giant then introduces each of it alphabetically.
hogwarts_houses.sort()
print(hogwarts_houses)
msg1 = (f"{hogwarts_houses[0]} is founded by Godric Gryffindor. He "
        f"values students with characteristics such as courage, "
        f"chivalry, and determination. The emblematic animal is a "
        f"lion.")
msg2 = (f"{hogwarts_houses[1]} is founded by Helga Hufflepuff. She "
        f"values students with characteristics such as hard work, "
        f"dedication, patience, and loyalty. The emblematic animal "
        f"is a badger.")
msg3 = (f"{hogwarts_houses[2]} is founded by Rowena Ravenclaw. She "
        f"values students' wit, learning, and wisdom. The emblematic "
        f"animal is an eagle.")
msg4 = (f"{hogwarts_houses[3]} is founded by Salazar Slytherin. He "
        f"values students with characteristics such as cunning, "
        f"resourcefulness, and ambition. The emblematic animal is "
        f"a snake.")
print(f"The giant introduces:", msg1, msg2, msg3,msg4, f"\n")

# The giant asks Harry Potter to repeat the houses unalphabetically.
hogwarts_houses.reverse()
print(hogwarts_houses)
print(f"The giant says to Harry Potter: 'Now, repeat them "
      f"unalphabetically.'")
print(f"Harry Potter goes: {hogwarts_houses}.")

