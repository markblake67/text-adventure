inventory = []

print("You find yourself in front of a spooky looking house. \n Here, if I was a writer I would aptly and eerily describe a desolute and disturbing house. \n Alas This is it.")
direction = input("\nWhat would you like to do? \n[1] Go forward \n[2] Leave?\n")
direction = int(direction)



def living_room():
    print("Welcome to the living room.")
    print("Inside you see a creepy Skeleton or something")
    skeleton_choice =  input("What do you do?\n [1] Inspect the creepy skeleton\n [2] Leave\n [3] Throw a lamp at the creepy skeleton\n")
    skeleton_choice = int(skeleton_choice)
	
    if skeleton_choice == 1:
        print("That was a silly idea, the skeleton kills you. You lose")
    elif skeleton_choice == 2: 
        print("Probably the most sensible option")
        leave_living_room()
    elif skeleton_choice == 3:
        print("You showed that skeleton, now you get it's scary dagger.")	
        inventory.append("Scary Dagger")
        leave_living_room()
        return inventory
    else:
        living_room()
	
def leave_living_room():	#condition created to deal with issue of having more text appear after 'skeleton encounter'
    living_room_direction = input("where next?\n[1] Leave?\n[2] Kitchen?\n")
    living_room_direction = int(living_room_direction)
    if living_room_direction == 1:
        print("Probably sensible, you leave the house")
        if "Scary Dagger" in inventory: #test condition for checking whether the Scary Dagger is in the inventory. 
            print("You also get a scary dagger")
    elif living_room_direction == 2:
        kitchen()	
        
def kitchen():
    print("You're in the Kitchen")		
	
if direction == 1:
    living_room()
elif direction == 2:
    print("How brave. You leave and have no adventures")		
