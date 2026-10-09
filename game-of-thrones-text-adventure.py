# Tyler Jordan

# Show the game instructions and move commands
def show_instructions():
    print('========================================')
    print('    Game of Thrones - Text Adventure    ')
    print('========================================')
    print('Collect 6 items to defeat the Night King,')
    print('or face him unprepared and lose!')
    print('Move commands: go North, go South, go East, go West')
    print('Pick up items: get item')
    print('========================================')

# Show the player's current status
def show_status(current_room, inventory, rooms):
    print('----------------------------------------')
    print('You are in:', current_room)
    print('Inventory:', inventory)
    if 'item' in rooms[current_room]:
        print('You see:', rooms[current_room]['item'])
    else:
        print('No item here.')
    print('----------------------------------------')

def main():

    # Dictionary linking rooms, directions, and items
    rooms = {
        'Winterfell':     {'South': "King's Landing", 'West': 'Riverrun', 'East': 'The Eyrie'},
        'Riverrun':       {'East': 'Winterfell',  'item': 'Direwolf Pelt'},
        'The Eyrie':      {'West': 'Winterfell',  'item': 'Raven Scroll'},
        "King's Landing": {'North': 'Winterfell', 'South': 'Dragonstone', 'item': 'Iron Throne Key'},
        'Dragonstone':    {'North': "King's Landing", 'West': 'Dorne', 'East': 'Essos Port', 'South': 'Harrenhal', 'item': 'Dragon Egg'},
        'Dorne':          {'East': 'Dragonstone', 'item': 'Sun Spear'},
        'Essos Port':     {'West': 'Dragonstone', 'item': 'Poison Vial'},
        'Harrenhal':      {'North': 'Dragonstone'}  # villain room - no item
    }

    # Track player state
    current_room = 'Winterfell'
    inventory = []
    all_items = ['Direwolf Pelt', 'Raven Scroll', 'Iron Throne Key', 'Dragon Egg', 'Sun Spear', 'Poison Vial']
    game_over = False

    show_instructions()

    # Main gameplay loop
    while not game_over:
        show_status(current_room, inventory, rooms)

        # Check win or lose when entering Harrenhal
        if current_room == 'Harrenhal':
            if len(inventory) == len(all_items):
                print('You have all 6 items! You face the Night King and DEFEAT him!')
                print('Congratulations! You have won the game!')
            else:
                print('The Night King catches you unprepared...')
                print('NOM NOM...GAME OVER!')
            print('Thanks for playing. Hope you enjoyed it!')
            game_over = True
            break

        command = input('Enter your move: ').strip()

        # Handle move commands
        if command in ['go North', 'go South', 'go East', 'go West']:
            direction = command.split()[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print('You moved to', current_room)
            else:
                print("You can't go that way!")

        # Handle get item command
        elif command == 'get item':
            if 'item' in rooms[current_room]:
                item = rooms[current_room]['item']
                inventory.append(item)
                print('You picked up:', item)
                # Remove item from room so it can't be picked up again
                del rooms[current_room]['item']
            else:
                print('There is no item here.')

        # Exit the game
        elif command == 'exit':
            print('Thanks for playing. Goodbye!')
            game_over = True

        # Invalid command
        else:
            print('Invalid command. Try: go North, go South, go East, go West, get item, or exit.')

main()
input('Press Enter to exit...')
