
def input_validity_checker(user_input:str , expected_inputs:list[str]):
    while user_input not in expected_inputs:
        user_input = input(f"Wrong input choose from {', '.join(expected_inputs)} \n").strip().lower()
    return user_input


if __name__ == '__main__':
    print("Welcome to the Treasure Island")
    print("Your misson is to find the Treasure")


    print("You are ata cross road, Where do you want to go?")
    cross_road_decision = input("type 'left' or 'right' \n").strip().lower()
    cross_road_decision = input_validity_checker(cross_road_decision,['left','right'])
  
        
    if cross_road_decision == 'left':
        print("You've come to a lake. There is an island in the middle of the lake.")
        lake_choice = input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").strip().lower()
        input_validity_checker(lake_choice,['wait','swim'])

        
        if lake_choice == 'wait':
            print("You arrive at the island unharmed. There is a house with 3 doors.")
            island_choice = input("One red, one yellow and one blue. Which colour do you choose? \n").strip().lower()
            input_validity_checker(island_choice,['red','yellow','blue'])
            
            if island_choice == 'red':
                print("It's a room full of fire. Game Over.")
            elif island_choice == 'yellow':
                print("You found the treasure! You Win!")
            else:
                print("You enter a room of beasts. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    
    else:
        print("You Fell into the hole Game Over")
        

