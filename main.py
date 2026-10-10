from campaign import Campaign
from player import Player
from npc import NPC
import json
import os

# OPTION 1: function that will add players and their attributes
def add_player(campaign):
    while True:
        player_name = input("Enter a player's name (or 'done' to finish): ")
        if player_name != "done":

            character_name = input(f"Enter a name for {player_name}'s character: ")
            character_class = input(f"Enter the class for {player_name}'s character: ")
            level = int(input(f"Enter the level for {player_name}'s character: "))
            race = input(f"Enter the race for {player_name}'s character: ")
            print("\n")

            player = Player(player_name, character_name, character_class, level, race)

            campaign.add_player(player)

        elif player_name == "done":
            break

# OPTION 2: function that will remove player objects
def remove_player(campaign):
    while True:
        inputted_player = input("Enter a player you want to remove (or 'done' to finish): ")

        if inputted_player == "done":
            break
        for current_player in campaign.players:
            if inputted_player == current_player.player_name: 
                campaign.remove_player(current_player)
                break
        else:
            print("Player was not found. Check your input and try again.")
    
# OPTION 3: function that will view your current list of players
def view_players(campaign):
    print("Players:\n")
    for current_player in campaign.players:
        print(f"Player: {current_player.player_name} ")
        print(f"Character: {current_player.character_name}")
        print(f"Class: {current_player.character_class}")
        print(f"Level: {current_player.level}")
        print(f"Race: {current_player.race}")
        print("\n")

    print("\n")

# OPTION 4: function that will edit player attributes
def edit_player(campaign):
    while True:
        inputted_player = input("Enter a player you want to edit (or 'done' to finish): ")

        if inputted_player == "done":
            break
        for current_player in campaign.players:
            if inputted_player == current_player.player_name:
                while True:
                    choice = input(f"""What would you like to edit for {current_player.player_name}?
                    1. Player Name
                    2. Character Name
                    3. Character Class
                    4. Character Level
                    5. Character Race
                    6. Exit Editing
                    """)
                        
                    if choice == "1":
                        new_name = input("Input the player's name: ")
                        current_player.player_name = new_name

                    elif choice == "2":
                        new_chname = input("Input the character's new name: ")
                        current_player.character_name = new_chname

                    elif choice == "3":
                        new_class = input("Input the character's new class: ")
                        current_player.character_class = new_class

                    elif choice == "4":
                        new_level = int(input("Input the character's new level: "))
                        current_player.level = new_level

                    elif choice == "5":
                        new_race = input("Enter the character's new race: ")
                        current_player.race = new_race

                    elif choice == "6":
                        break

                    else:
                        print("Invalid choice. Please choose one of the options listed.")
                break
        else:
            print("Player was not found. Check your input and try again.")

# OPTION 5: function that lists the campaign info
def campaign_info(campaign):
    print(f"Your campaign name: {campaign.name}")
    print(f"Your DM's name: {campaign.dm_name}")
    print(f"Your campaign system: {campaign.system} \n\n")

# OPTION 6: Save campaign info to JSON file
def save_campaign(campaign):
    filename = campaign.name.lower().replace(" ", "_")

    with open(f"{filename}.json", "w") as file:
        json.dump(campaign.to_dict(), file, indent=4)

    print("Saved!")

# OPTION 7: Load an exisiting campaign. This option also exists at the start menu
def load_campaign():
    campaign_titles = [
        file for file in os.listdir()
        if file.endswith(".json")
        ]
    
    if len(campaign_titles) <= 0:
        print("There are no campaigns saved to load!")
        return None
    
    while True:
        for i, title in enumerate(campaign_titles, 1):
            with open(title, "r") as file:
                title_data = json.load(file)

                print(f"{i}. {title_data['campaign_name']}")

        try:
            option = int(input("Enter the campaign you want to load: "))

        except ValueError:
            print("Please enter a number.")
            continue

        if option < 1 or option > len(campaign_titles):
            print("Invalid choice. Please input a number associated with a campaign.")
        
        else: 
            selected_campaign = campaign_titles[option - 1]
            break


    with open(f"{selected_campaign}", "r") as file:
        data = json.load(file)

        campaign = Campaign(
            data["campaign_name"], 
            data["dm_name"], 
            data["system"])

        for player_data in data["players"]:
            player = Player(
                player_name = player_data["player_name"],
                character_name = player_data["character_name"],
                character_class = player_data["character_class"],
                level = player_data["level"],
                race = player_data["race"]
            )
            campaign.add_player(player)

        for npc_data in data.get("npcs", []):
            npc = NPC(
                npc_name = npc_data["npc_name"],
                npc_level = npc_data["npc_level"],
                npc_race = npc_data["npc_race"],
                npc_class = npc_data["npc_class"]
            )
            campaign.add_npc(npc)

        print("Load completed")

        return campaign

def new_campaign():
    campaign_name = input("Enter your campaign name: ")
    dm_name = input("What is the DM's name? ")
    system = input("What is the campaign system? ")
    campaign = Campaign(campaign_name, dm_name, system)

    save_campaign(campaign)

    return campaign

def add_npc(campaign):
    while True:
        npc_name = input("Enter the NPC's name (or 'done' to finish): ")
        if npc_name != "done":
            npc_class = input(f"Enter the class for {npc_name}'s character: ")
            npc_level = int(input(f"Enter the level for {npc_name}'s character: "))
            npc_race = input(f"Enter the race for {npc_name}'s character: ")
            print("\n")

            npc = NPC(npc_name, npc_level, npc_race, npc_class)

            campaign.add_npc(npc)

        elif npc_name == "done":
            break

def remove_npc(campaign):
    while True:
        inputted_npc = input("Enter a npc you want to remove (or 'done' to finish): ")

        if inputted_npc == "done":
            break
        for current_npc in campaign.npcs:
            if inputted_npc == current_npc.npc_name: 
                campaign.remove_npc(current_npc)
                break
        else:
            print("NPC was not found. Check your input and try again.")

def edit_npc(campaign):
    while True:
        inputted_npc = input("Enter a NPC you want to edit (or 'done' to finish): ")

        if inputted_npc == "done":
            break
        for current_npc in campaign.npcs:
            if inputted_npc == current_npc.npc_name:
                while True:
                    choice = input(f"""What would you like to edit for {current_npc.npc_name}?
                    1. NPC Name
                    2. NPC Class
                    3. NPC Level
                    4. NPC Race
                    5. Exit Editing
                    """)
                        
                    if choice == "1":
                        new_name = input("Input the NPC's name: ")
                        current_npc.npc_name = new_name

                    elif choice == "2":
                        new_class = input("Input the NPC's new class: ")
                        current_npc.npc_class = new_class

                    elif choice == "3":
                        new_level = int(input("Input the NPC's new level: "))
                        current_npc.npc_level = new_level

                    elif choice == "4":
                        new_race = input("Enter the character's new race: ")
                        current_npc.npc_race = new_race

                    elif choice == "5":
                        break

                    else:
                        print("Invalid choice. Please choose one of the options listed.")
                break
        else:
            print("NPC was not found. Check your input and try again.")

def view_npcs(campaign):
    print("NPC's:\n")
    for current_npc in campaign.npcs:
        print(f"NPC Name: {current_npc.npc_name} ")
        print(f"NPC Class: {current_npc.npc_class}")
        print(f"NPC Level: {current_npc.npc_level}")
        print(f"NPC Race: {current_npc.npc_race}")
        print("\n")

    print("\n")

print("=== Campaign Manager === \n \n")

# Give the option to make a new campaign or load an existing one
while True:
    option = input("""Choose an option:
    1. Create a new campaign
    2. Load campaign
    3. Quit
    """)

    if option == "1":
        campaign = new_campaign()
        break

    elif option == "2":
        loaded_campaign = load_campaign()

        if loaded_campaign is not None:
            campaign = loaded_campaign
            break

    elif option == "3":
        exit()

    else:
        print("Invalid input. Please choose between the given options.")

while True:
    option = input("""Choose an option: 
   1. Add player
   2. Remove player
   3. View players
   4. Edit players
   5. View campaign info
   6. Save campaign
   7. Load campaign
   8. New campaign
   9. NPC Menu
   10. Quit \n""")
   
    if option == "1":
        add_player(campaign)
        
    elif option == "2":
        remove_player(campaign)

    elif option == "3":
        view_players(campaign)

    elif option == "4":
        edit_player(campaign)

    elif option == "5":
        campaign_info(campaign)

    elif option == "6":
        save_campaign(campaign)

    elif option == "7":
        loaded_campaign = load_campaign()

        if loaded_campaign is not None:
            campaign = loaded_campaign

    elif option == "8":
        campaign = new_campaign()

    elif option == "9":
        while True:
            choice = input("""What would you like to access?
            1. Add NPC
            2. Remove NPC
            3. Edit NPC
            4. View NPC's
            5. Exit Editing
            \n""")

            if choice == "1":
                add_npc(campaign)

            elif choice == "2":
                remove_npc(campaign)

            elif choice == "3":
                edit_npc(campaign)

            elif choice == "4":
                view_npcs(campaign)

            elif choice == "5":
                break

            else:
                print("Invalid input. Please choose between the given options.")

    elif option == "10":
        while True:
            choice = input("Would you like to save before exiting? (y/n)\n")

            if choice == 'y':
                save_campaign(campaign)
                break

            elif choice == 'n':
                break

            else:
                print("Invalid input. Please choose between the given options.")

        break

    else:
        print("Invalid input. Please choose between the given options.")
            

