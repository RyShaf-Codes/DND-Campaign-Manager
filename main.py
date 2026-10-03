from campaign import Campaign
from player import Player
import json

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
    with open("campaign.json", "w") as file:
        json.dump(campaign.to_dict(), file, indent=4)

    print("Saved!")

def load_campaign():
    with open("campaign.json", "r") as file:
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

        return campaign


print("=== Campaign Manager === \n \n")

while True:
    option = input("""Choose an option:
    1. Create a new campaign
    2. Load campaign
    3. Quit
    """)

    if option == "1":
        campaign_name = input("Enter your campaign name: ")
        dm_name = input("What is the DM's name? ")
        system = input("What is the campaign system? ")
        campaign = Campaign(campaign_name, dm_name, system)
        break

    elif option == "2":
        campaign = load_campaign()
        print("Load completed")
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
   7. Load Campaign
   8. Quit \n""")
   
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
        campaign = load_campaign()

    elif option == "8":
        break

    else:
        print("Invalid input. Please choose between the given options.")
            

