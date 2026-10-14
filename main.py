from campaign import Campaign
from player import Player
from npc import NPC
from location import Location
from note import Note
import database

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

            player.id = database.add_player(campaign.id, player_name, character_name, character_class, level, race)

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
                database.delete_player(current_player.id)
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

                database.update_player(
                    current_player.id,
                    current_player.player_name,
                    current_player.character_name,
                    current_player.character_class,
                    current_player.level,
                    current_player.race
                )
                break
        else:
            print("Player was not found. Check your input and try again.")

# OPTION 5: function that lists the campaign info
def campaign_info(campaign):
    print(f"Your campaign name: {campaign.name}")
    print(f"Your DM's name: {campaign.dm_name}")
    print(f"Your campaign system: {campaign.system} \n\n")

# OPTION 7: Load an exisiting campaign. This option also exists at the start menu
def load_campaign():
    campaigns = database.get_campaigns()

    if len(campaigns) <= 0:
        print("There are no campaigns saved to load!")
        return None

    for i, campaign_data in enumerate(campaigns, 1):
        print(f"{i}. {campaign_data[1]}")
    
    while True:
        try:
            option = int(input("Enter the campaign you want to load: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if option < 1 or option > len(campaigns):
            print("Invalid choice. Please input a number associated with a campaign.")  
        else: 
            break

    selected_campaign = campaigns[option - 1]

    campaign = Campaign(
        selected_campaign[1],
        selected_campaign[2],
        selected_campaign[3],
        selected_campaign[0]
    )

    players = database.get_players(campaign.id)

    for player_data in players:
        player = Player(
            player_data[2],
            player_data[3],
            player_data[4],
            player_data[5],
            player_data[6],
            player_data[0],
        )

        campaign.add_player(player)

    npcs = database.get_npcs(campaign.id)

    for npc_data in npcs:
        npc = NPC(
            npc_data[2],
            npc_data[3],
            npc_data[4],
            npc_data[5],
            npc_data[0],
        )

        campaign.add_npc(npc)

    locations = database.get_locations(campaign.id)

    for location_data in locations:
        location = Location(
            location_data[2],
            location_data[3],
            location_data[4],
            location_data[5],
            location_data[0],
        )

        campaign.add_location(location)

    notes = database.get_notes(campaign.id)
    for note_data in notes:
        note = Note(
            note_data[2],
            note_data[3],
            note_data[4],
            note_data[5],
            note_data[0],
        )

        campaign.add_note(note)

    print("Load completed")

    return campaign

def new_campaign():
    campaign_name = input("Enter your campaign name: ")
    dm_name = input("What is the DM's name? ")
    system = input("What is the campaign system? ")
    campaign = Campaign(campaign_name, dm_name, system)

    campaign.id = database.add_campaign(campaign_name, dm_name, system)
    print(f"Database ID: {campaign.id}")

    return campaign

def add_npc(campaign):
    while True:
        npc_name = input("Enter the NPC's name (or 'done' to finish): ")
        if npc_name != "done":
            npc_class = input(f"Enter the class for {npc_name}'s character: ")
            npc_level = int(input(f"Enter the level for {npc_name}'s character: "))
            npc_race = input(f"Enter the race for {npc_name}'s character: ")
            print("\n")

            npc = NPC(npc_name, npc_class, npc_level, npc_race)
            npc.id = database.add_npc(campaign.id, npc_name, npc_class, npc_level, npc_race)

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
                database.delete_npc(current_npc.id)
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

                database.update_npc(
                    current_npc.id,
                    current_npc.npc_name,
                    current_npc.npc_class,
                    current_npc.npc_level,
                    current_npc.npc_race
                )
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

def add_location(campaign):
    while True:
        location_name = input("Enter the name of the location (or 'done' to finish): ")
        if location_name != "done":
            location_type = input(f"What type of location is {location_name}? ")
            location_region = input(f"What region is {location_name} in? ")
            location_description = input(f"Enter a description for {location_name}: ")
            print("\n")

            location = Location(location_name, location_type, location_region, location_description)
            location.id = database.add_location(campaign.id, location_name, location_type, location_region, location_description)

            campaign.add_location(location)

        elif location_name == "done":
            break

def remove_location(campaign):
    while True:
        inputted_location = input("Enter a location you want to remove (or 'done' to finish): ")

        if inputted_location == "done":
            break
        for current_location in campaign.locations:
            if inputted_location == current_location.location_name: 
                database.delete_location(current_location.id)
                campaign.remove_location(current_location)
                break
        else:
            print("Location was not found. Check your input and try again.")

def edit_location(campaign):
    while True:
        inputted_location = input("Enter a location you want to edit (or 'done' to finish): ")

        if inputted_location == "done":
            break
        for current_location in campaign.locations:
            if inputted_location == current_location.location_name:
                while True:
                    choice = input(f"""What would you like to edit for {current_location.location_name}?
                    1. Location Name
                    2. Location Type
                    3. Location Region
                    4. Location Description
                    5. Exit Editing
                    """)
                        
                    if choice == "1":
                        new_name = input("Input the location's new name: ")
                        current_location.location_name = new_name

                    elif choice == "2":
                        new_type = input("Input the location's new type: ")
                        current_location.location_type = new_type

                    elif choice == "3":
                        new_region = input("Input the location's new region: ")
                        current_location.location_region = new_region

                    elif choice == "4":
                        new_description = input("Enter the character's new description: ")
                        current_location.location_description = new_description

                    elif choice == "5":
                        break

                    else:
                        print("Invalid choice. Please choose one of the options listed.")
                database.update_location(
                    current_location.id,
                    current_location.location_name,
                    current_location.location_type,
                    current_location.location_region,
                    current_location.location_description
                )
                break
        else:
            print("Location was not found. Check your input and try again.")

def view_locations(campaign):
    print("Locations:\n")
    for current_location in campaign.locations:
        print(f"Location Name: {current_location.location_name} ")
        print(f"Location Type: {current_location.location_type}")
        print(f"Location Region: {current_location.location_region}")
        print(f"Location Description: {current_location.location_description}")
        print("\n")

    print("\n")

def add_note(campaign):
    while True:
        note_title = input("Enter the title of the note (or 'done' to finish): ")
        if note_title != "done":
            note_category = input(f"What category is {note_title}? ")
            note_content = input(f"Content: ")
            note_visibility = input(f"Visibility: ")
            print("\n")

            note = Note(note_title, note_category, note_content, note_visibility)
            note.id = database.add_note(campaign.id, note_title, note_category, note_content, note_visibility)

            campaign.add_note(note)

        elif note_title == "done":
            break

def remove_note(campaign):
    while True:
        inputted_note = input("Enter a note you want to remove (or 'done' to finish): ")

        if inputted_note == "done":
            break
        for current_note in campaign.notes:
            if inputted_note == current_note.note_title: 
                database.delete_note(current_note.id)
                campaign.remove_note(current_note)
                break
        else:
            print("Note was not found. Check your input and try again.")

def edit_note(campaign):
    while True:
        inputted_note = input("Enter a note you want to edit (or 'done' to finish): ")

        if inputted_note == "done":
            break
        for current_note in campaign.notes:
            if inputted_note == current_note.note_title:
                while True:
                    choice = input(f"""What would you like to edit for {current_note.note_title}?
                    1. Note Title
                    2. Note Category
                    3. Note Content
                    4. Note Visibility
                    5. Exit Editing
                    """)
                        
                    if choice == "1":
                        new_title = input("Input the notes new title: ")
                        current_note.note_title = new_title

                    elif choice == "2":
                        new_category = input("Input the note's new category: ")
                        current_note.note_category = new_category

                    elif choice == "3":
                        new_content = input("Input the new content: ")
                        current_note.note_content = new_content

                    elif choice == "4":
                        new_visibility = input("Input the new visibility: ")
                        current_note.note_visibility = new_visibility

                    elif choice == "5":
                        break

                    else:
                        print("Invalid choice. Please choose one of the options listed.")

                database.update_note(
                    current_note.id,
                    current_note.note_title,
                    current_note.note_category,
                    current_note.note_content,
                    current_note.note_visibility
                )
                break
        else:
            print("Note was not found. Check your input and try again.")

def view_notes(campaign):
    print("Notes:\n")
    for current_note in campaign.notes:
        print(f"Note Title: {current_note.note_title} ")
        print(f"Note Category: {current_note.note_category}")
        print(f"Note Content: {current_note.note_content}")
        print(f"Note Visibility: {current_note.note_visibility}")
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
   1. Player Menu
   2. NPC Menu
   3. Location Menu
   4. Notes Menu
   5. View campaign info
   6. Load campaign
   7. New campaign
   8. Quit \n""")
   
    if option == "1":
        while True:
            choice = input("""What would you like to access?
            1. Add Player
            2. Remove Player
            3. Edit Player
            4. View Players
            5. Exit Editing
            \n""")

            if choice == "1":
                add_player(campaign)

            elif choice == "2":
                remove_player(campaign)

            elif choice == "3":
                edit_player(campaign)

            elif choice == "4":
                view_players(campaign)

            elif choice == "5":
                break

            else:
                print("Invalid input. Please choose between the given options.")
        
    elif option == "2":
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

    elif option == "3":
        while True:
            choice = input("""What would you like to access?
            1. Add Location
            2. Remove Location
            3. Edit Location
            4. View Locations
            5. Exit Editing
            \n""")

            if choice == "1":
                add_location(campaign)

            elif choice == "2":
                remove_location(campaign)

            elif choice == "3":
                edit_location(campaign)

            elif choice == "4":
                view_locations(campaign)

            elif choice == "5":
                break

            else:
                print("Invalid input. Please choose between the given options.")

    elif option == "4":
        while True:
            choice = input("""What would you like to access?
            1. Add Note
            2. Remove Note
            3. Edit Note
            4. View Notes
            5. Exit Editing
            \n""")

            if choice == "1":
                add_note(campaign)

            elif choice == "2":
                remove_note(campaign)

            elif choice == "3":
                edit_note(campaign)

            elif choice == "4":
                view_notes(campaign)

            elif choice == "5":
                break

            else:
                print("Invalid input. Please choose between the given options.")

    elif option == "5":
        campaign_info(campaign)

    elif option == "6":
        loaded_campaign = load_campaign()

        if loaded_campaign is not None:
            campaign = loaded_campaign

    elif option == "7":
        campaign = new_campaign()

    elif option == "8":
        break

    else:
        print("Invalid input. Please choose between the given options.")
            

