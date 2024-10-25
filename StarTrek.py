import random 
# Constants
global score

MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 

	if action == "1": 
		score += run_mission() 
	elif action == "2": 
		repair_system() 
	elif action == "3": 
		add_crew_member() 
	elif action == "4": 
		print(f"Simulation ended. Final score: {score}")
		break 
	else: 
		print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew
	print(ship["systems"])

def get_user_action(): 
# TODO: Implement function to get and return user's chosen action


def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}")
# TODO: Implement mission logic for different mission types
	if mission_type is 'Exploration':
		print(mission_type)

	elif mission_type is 'Diplomacy':
		print(mission_type)

	elif mission_type is 'Combat':
		print(mission_type)

	elif mission_type is 'Rescue':
		print(mission_type)	

	elif mission_type is 'Scientific Research':
		print(mission_type)	

	else:
		print("Please try again")

	# Return the score earned from the mission
	return score 

def repair_system(): 
# TODO: Implement system repair functionality

 
def add_crew_member(): 
# TODO: Implement functionality to add a new crew member
	new_member_name = input("Please enter the name of the crew member: ")
	new_member_position = input("What is the crew member's role on the ship: ")
	ship["crew"][new_member_name] = new_member_position

def handle_random_event():
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 
# TODO: Implement resource replenishment logic
	if ship["resources"]["energy"] < 200 :
		refill_option1 = input("EMERGENCY, energy levels are too low! Would you like to refill energy? Y/N ").upper()
		if refill_option1 == "Y":
			ship["resources"]["energy"] += 1000
			print("Energy refill complete")
		elif refill_option1 == "N":
			print("Be aware of your energy levels!")
		else:
			print("Option to renew energy content failed. Please try again another time.")
	if ship["resources"]["torpedoes"] == 0:
		refill_option2 = input("EMERGENCY, weapon inventory depleted! Would you like to add a single torpedo to inventory? Y/N ").upper()
		if refill_option2 == "Y":
			ship["resources"]["torpedoes"] += 1
			print("Emergency Torpedo has successfully been added to inventory")
		elif refill_option2 == "N":
			print("Be aware of your energy levels!")
		else:
			print("Option to renew energy content failed. Please try again another time.")

main()
