# i have no idea what the fuck i'm doing
# video game/text adventure time!!!
#shoutout Alta3 Research on yt for help and inspiration
#inspired by Zork & Incubus song Segue 1 & The Avalanches' Frontier Psychiatrist & Paprika (movie) & the Matrix trilogy

print("\n\n\nyou're in a hallway. you are walking. you see doors. \ngrey walls and concrete? linolieum? tile? \nit's  cool and comfortable. \nyou lie down and the floor sinks around you. \nyou gleefully claw and  crawl forward. \nyou feel an odd tension in  the back of your  head")
print("\ncontrols:\n get [item] to pick up items,\ngo [direction] to move in a direction,\n")
print("\ndirections: north, south, east, west")



inventory = []

currentRoom = "hallway"

rooms = {
    "hallway": { "south": "room labelled 1-A"
             
               }, 
    "room labelled 1-A": { "north": "hallway",
                          "item": "pen"

                         }


        }

print (f"\n\nyou are in the {currentRoom}")

directions = rooms["hallway"]
print(inventory)
print(directions)

while True:

    move = input(">")

    move = move.split(" ", 1)
    # "go north" -> ["go", "north"]
    # move[0] -> "go"

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            print(f"\n\nyou are in the {currentRoom}")
            if "item" in rooms[currentRoom]:
                print(f"\n\nthere is a {rooms[currentRoom]['item']} here.")
        else:
            print("\n\nreality imposes itself on your will. you don't get anywhere.")
            print(inventory)
            print(directions)

    # "get pen" -> ["get", "pen"]
    # move[0] -> "get"

    if  move[0] == "get":
        if move[1] in rooms[currentRoom]["item"]:
            print(f"you have picked up the {move[1]}.")
            inventory.append(move[1])
            rooms[currentRoom]["item"] = ""
            print(inventory)
            print(directions)

        else:
            print(f"you grab at empty space. there is nothing here.")
            print(inventory)
            print(directions)




