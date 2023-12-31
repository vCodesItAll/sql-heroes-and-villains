from database.db_connection import execute_query

# Define a function to add a hero to the database
def add_hero(name, about_me, biography, image_url):
    # Create an SQL query to insert a new hero into the 'heroes' table
    query = f"""
        INSERT INTO heroes (name, about_me, biography, image_url)
        VALUES ('{name}', '{about_me}', {biography}, '{image_url}')
    """
    execute_query(query)

# Update a hero's information in the database
def update_hero(hero_id, name=None, about_me=None, biography=None, image_url=None):
    set_values = []
    if name:
        set_values.append(f"name = '{name}'")
    if about_me:
        set_values.append(f"about_me = '{about_me}'")
    if biography:
        set_values.append(f"biography = {biography}")
    if image_url:
        set_values.append(f"image_url = '{image_url}'")
    set_values_str = ", ".join(set_values)
    # Update a hero's information in the 'heroes' table
    query = f"""
        UPDATE heroes
        SET {set_values_str}
        WHERE id = {hero_id}
    """
    # Execute the SQL query using the execute_query function
    execute_query(query)

# Define a function to delete a hero from the database
def delete_hero(hero_id):
    # Create an SQL query to delete a hero from the 'heroes' table
    query = f"""
        DELETE FROM heroes
        WHERE id = {hero_id}
    """
    # Execute the SQL query using the execute_query function
    execute_query(query)

# Define a function to select and display all heroes and their friends
def select_all_heroes():
    # Create an SQL query to select hero names and their friends from the 'heroes' and 'friends' tables
    # alias relationships as r

    query = """
        SELECT hero1.name, hero2.name, rt.name FROM relationships
        JOIN heroes hero1 ON relationships.hero1_id = hero1.id
        JOIN heroes hero2 ON relationships.hero2_id = hero2.id
        Join relationship_types rt ON relationships.relationship_type_id = rt.id
        

    """
   
    # Execute the SQL query using the execute_query function and store the results in 'returned_items'
    returned_items = execute_query(query)
    # print(returned_items,"full item list")
    # Create an empty dictionary to store the heroes and their friends
    hero_friends = {}
    hero_enemies = {}
    
    for item in returned_items:
        # If the friend is not None (i.e., it exists), add it as a key-value pair 
        #    to the hero_friends
        hero_name = item[0]
        friend_name=""
        enemy_name =""
        if item[2] == 'Friend':
            friend_name = item[1]
        elif item[2] == 'Enemy':
            enemy_name = item[1]
            
        if hero_name not in hero_friends:
            # Add hero category
            hero_friends[hero_name] = []
        if friend_name:
            hero_friends[hero_name].append(friend_name)
  
        if hero_name not in hero_enemies:
            # Add hero category
            hero_enemies[hero_name] = []
        if enemy_name:
            hero_enemies[hero_name].append(enemy_name) 

    # print(hero_friends)
    # print(hero_enemies)
    # print(returned_items)
    for hero_name, enemy in hero_enemies.items():
        # Print the hero's name and their friends/enemies
        print(f"{hero_name} has enemies: {', '.join(enemy) }")
    for hero_name, friend in hero_friends.items():
        print(f"{hero_name} has friends: {', '.join(friend) }")
        



# Define a function to interact with the user and perform various operations
def prompt_user():
    while True:
        print("What do you want to do?")
        print("1. Add a hero")
        print("2. Update a hero")
        print("3. Delete a hero")
        print("4. View all heroes and their friends")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter hero name: ")
            about_me = input("Enter about me: ")
            biography = (input("Enter biography: "))
            image_url = input("Enter image_url: ")
            # Call the add_hero function to add a hero to the database
            add_hero(name, about_me, biography, image_url)
        elif choice == "2":
            hero_id = int(input("Enter hero ID: "))
            name = input("Enter hero name (leave blank to skip): ")
            about_me = input("Enter about me (leave blank to skip): ")
            biography = input("Enter biography (leave blank to skip): ")
            image_url = input("Enter image_url (leave blank to skip): ")
            # Call the update_hero function to update a hero's information in the database
            update_hero(hero_id, name, about_me, biography, image_url)
        elif choice == "3":
            hero_id = int(input("Enter hero ID: "))
            # Call the delete_hero function to delete a hero from the database
            delete_hero(hero_id)
        elif choice == "4":
            # Call the select_all_heroes function to display hero information
            select_all_heroes()
        elif choice == "5":
            # Exit the loop and end the program
            break
        else:
            print("Invalid choice")

# Start the user interaction by calling the prompt_user function
prompt_user()


